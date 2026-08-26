import logging

import pandas as pd
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    balanced_accuracy_score,
    f1_score,
    precision_recall_curve,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def load_data(cfg):
    train = pd.read_csv(cfg["data"]["train_path"])
    test = pd.read_csv(cfg["data"]["test_path"])
    target = cfg["data"]["target_column"]
    X_train, y_train = train.drop(columns=[target]), train[target]
    X_test, y_test = test.drop(columns=[target]), test[target]
    return X_train, y_train, X_test, y_test


def apply_imbalance_handling(cfg, X_train, y_train):
    method = cfg["imbalance_handling"]["method"].lower()
    if method == "none":
        logging.info("No imbalance handling applied (training on raw data).")
        return X_train, y_train
    from imblearn.combine import SMOTETomek  # noqa: F401  # placeholder, ganti sesuai metode

    raise NotImplementedError(
        f"Imbalance method '{method}' belum diimplementasikan. "
        "Gunakan SMOTE/ADASYN dari imblearn pada data train saja."
    )


def build_preprocessor(cfg):
    num_cols = cfg["data"]["numeric_features"]
    cat_cols = cfg["data"]["categorical_features"]
    num_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )
    cat_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    return ColumnTransformer(
        transformers=[
            ("num", num_transformer, num_cols if num_cols else "passthrough"),
            ("cat", cat_transformer, cat_cols),
        ]
    )


def evaluate(y_true, y_pred, y_score):
    metrics = {
        "roc_auc": roc_auc_score(y_true, y_score),
        "pr_auc": None,  # hitung manual via average_precision bila perlu
        "balanced_accuracy": balanced_accuracy_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
    }
    precision, recall, _ = precision_recall_curve(y_true, y_score)
    metrics["pr_auc"] = float(recall.sum() / (len(recall)))  # placeholder aproksimasi
    return metrics


def run_pipeline():
    cfg = load_config()
    logging.info(f"Starting experiment: {cfg['experiment_name']} (seed={cfg['seed']})")

    # 1. Load Data
    X_train, y_train, X_test, y_test = load_data(cfg)

    # 2. Optional split jika belum ada split terpisah
    # (default: menggunakan test_path yang sudah disediakan)

    # 3. Imbalance handling
    X_train, y_train = apply_imbalance_handling(cfg, X_train, y_train)

    # 4. Preprocess
    preprocessor = build_preprocessor(cfg)
    model = XGBClassifier(
        n_estimators=cfg["model"]["n_estimators"],
        max_depth=cfg["model"]["max_depth"],
        learning_rate=cfg["model"]["learning_rate"],
        subsample=cfg["model"]["subsample"],
        colsample_bytree=cfg["model"]["colsample_bytree"],
        eval_metric=cfg["model"]["eval_metric"],
        scale_pos_weight=cfg["model"]["scale_pos_weight"],
        random_state=cfg["seed"],
    )
    pipeline = Pipeline(steps=[("prep", preprocessor), ("clf", model)])

    # 5. Fit
    pipeline.fit(X_train, y_train)

    # 6. Evaluate & Log
    y_score = pipeline.predict_proba(X_test)[:, 1]
    y_pred = pipeline.predict(X_test)
    metrics = evaluate(y_test, y_pred, y_score)
    for k, v in metrics.items():
        logging.info(f"  {k}: {v:.4f}")

    logging.info("Baseline run completed.")


if __name__ == "__main__":
    run_pipeline()