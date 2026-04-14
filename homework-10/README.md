# Homework 10: MLOps with a Linear Classifier

## Overview

This project builds and deploys two machine learning models using the UCI Breast Cancer Wisconsin dataset. The goal is to train a linear classifier, create a normalized pipeline, and deploy both models to make predictions on new sample data.

---

## Part 1: Model Training

### Data Preparation

The dataset was loaded using `ucimlrepo` and split into features (`X`) and labels (`y`).
The target variable (`Diagnosis`) was converted into numeric format:

* Malignant (M) → 1
* Benign (B) → 0

The data was then split into training and testing sets using:

* `train_test_split`
* Stratification to preserve class balance

---

### Model 1: Plain Linear Classifier

A linear classifier (`SGDClassifier`) was trained directly on the raw data without normalization.

**Steps:**

* Fit model on training data
* Predict on test data
* Evaluate using accuracy and classification report
* Save model as `classifier.pkl` using `pickle`

**Performance:**

* Accuracy ≈ 81.87%
* Slightly worse performance due to lack of feature scaling

---

### Model 2: Pipeline (StandardScaler + Classifier)

A pipeline was created to normalize the data before classification.

**Steps:**

* Apply `StandardScaler` for normalization
* Use `SGDClassifier` for classification
* Fit pipeline on training data
* Evaluate on test data
* Save pipeline as `normalizer_and_data_classifier_pipeline.pkl`

**Performance:**

* Accuracy ≈ 91.23%
* Improved performance due to normalization

---

## Part 2: Model Deployment

The `inference.py` script loads both the trained model and pipeline using `pickle`, then makes predictions on user-provided sample data.

### Input

* A CSV file (`sample_data.csv`)
* Must have the same feature columns as the original dataset

### Output

* Number of entries in the sample data
* Predictions from:

  * Plain model (non-normalized)
  * Pipeline model (normalized)

---

## How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train models

```
python training.py
```

### 3. Run inference

```
python inference.py --sample_data sample_data.csv
```

---

## AI Usage

ChatGPT was used to to help debug some of the script, generate a small sample dataset for testing by suggesting the approach below, and making the README aesthetic.

`sample_data = X.head(3)`
`sample_data.to_csv("sample_data.csv", index=False)`

This ensured the sample data matched the exact format of the original dataset. 