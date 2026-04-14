#!/usr/bin/env python3

from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import argparse
import logging
import socket
import pickle
import sys

# -------------------------
# Logging setup
# -------------------------

parser = argparse.ArgumentParser(
    description="Train plain and normalized SGDClassifier models on breast cancer dataset"
)

parser.add_argument(
    '-l', '--loglevel',
    required=False,
    default='WARNING',
    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    help='Set log level'
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

def train_plain_model(X_train, X_test, y_train, y_test) -> None:
    """
    Train a plain SGDClassifier, evaluate it, and save it to disk.

    Args:
        X_train: Training feature data
        X_test: Testing feature data
        y_train: Training labels
        y_test: Testing labels

    Returns:
        None
    """
    logging.info("Training plain model")

    model = SGDClassifier(loss="perceptron", alpha=0.01, random_state=1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Plain Model Results")
    print(f'accuracy = {accuracy_score(y_test, y_pred)}')
    print(classification_report(y_test, y_pred, digits=4))

    logging.info("Saving plain model to classifier.pkl")
    with open('classifier.pkl', 'wb') as f:
        pickle.dump(model, f)


def train_pipeline_model(X_train, X_test, y_train, y_test) -> None:
    """
    Train a pipeline with StandardScaler and SGDClassifier, evaluate it,
    and save it to disk.

    Args:
        X_train: Training feature data
        X_test: Testing feature data
        y_train: Training labels
        y_test: Testing labels

    Returns:
        None
    """
    logging.info("Training pipeline model")

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SGDClassifier(loss="perceptron", alpha=0.01, random_state=1))
    ])

    pipeline.fit(X_train, y_train)
    y_pred_pipeline = pipeline.predict(X_test)

    print("\nPipeline Model Results")
    print(f'accuracy = {accuracy_score(y_test, y_pred_pipeline)}')
    print(classification_report(y_test, y_pred_pipeline, digits=4))

    logging.info("Saving pipeline model to normalizer_and_data_classifier_pipeline.pkl")
    with open('normalizer_and_data_classifier_pipeline.pkl', 'wb') as f:
        pickle.dump(pipeline, f)


def main() -> None:
    logging.info("Starting training workflow")

    try:
        # fetch dataset
        UCI_data = fetch_ucirepo(id=17)

        # features and target
        X = UCI_data.data.features
        y = UCI_data.data.targets['Diagnosis'].map({'M': 1, 'B': 0})

        # split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, stratify=y, random_state=123
        )
        
        # call both model functions
        train_plain_model(X_train, X_test, y_train, y_test)
        train_pipeline_model(X_train, X_test, y_train, y_test)

    except FileNotFoundError:
        logging.error("Dataset file not found. Exiting.")
        sys.exit(1)

    logging.info("Training workflow complete")


if __name__ == '__main__':
    main()