#!/usr/bin/env python3

import pickle
import pandas as pd
import argparse
import logging
import socket
import sys

# -------------------------
# Constants
# -------------------------

classifier_file = 'classifier.pkl'
pipeline_file = 'normalizer_and_data_classifier_pipeline.pkl'
sample_file = 'sample_data.csv'


# -------------------------
# Logging setup
# -------------------------

parser = argparse.ArgumentParser(
    description="Run inference using saved model and pipeline"
)

parser.add_argument(
    '-l', '--loglevel',
    required=False,
    default='WARNING',
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
)

parser.add_argument(
    '-s', '--sample_data',
    required=False,
    type=str,
    default=sample_file
)

args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)

logging.basicConfig(level=args.loglevel, format=format_str)


# -------------------------
# Functions
# -------------------------

def run_inference(sample_data_file: str) -> None:
    """
    Load trained models and make predictions on sample data.

    Args:
        sample_data_file: Path to input CSV file

    Returns:
        None
    """
    logging.info("Running inference")
    #Load model and pipeline
    with open(classifier_file, 'rb') as f:
        loaded_model = pickle.load(f)

    with open(pipeline_file, 'rb') as f:
        loaded_pipeline = pickle.load(f)
    
    #Load sample csv
    sample_data = pd.read_csv(sample_data_file)
    #Make preductions based on model
    plain_pred = loaded_model.predict(sample_data)
    pipeline_pred = loaded_pipeline.predict(sample_data)

    #Find nyumber of entries
    num_entries = len(sample_data)

    print(f"Your sample data contains {num_entries} entry(s):")
    print("Malignant tumors are classified as 1 and benign as 0")
    print(f"Non-normalized model predictions: {plain_pred}")
    print(f"Normalized model predictions: {pipeline_pred}")


def main() -> None:
    """
    Run inference workflow.

    Returns:
        None
    """
    logging.info("Starting inference script")

    try:
        run_inference(args.sample_data)

    except FileNotFoundError:
        logging.error("File not found. Exiting.")
        sys.exit(1)


if __name__ == '__main__':
    main()