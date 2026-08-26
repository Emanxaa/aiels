import yaml
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_config(config_path="config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def run_pipeline():
    config = load_config()
    logging.info(f"Starting experiment: {config['experiment_name']}")
    # 1. Load Data
    # 2. Preprocess
    # 3. Train Baseline
    # 4. Evaluate & Log Metrics
    logging.info("Baseline run completed.")

if __name__ == "__main__":
    run_pipeline()
