# -*- coding: utf-8 -*-
"""Classificazione di frutti esotici

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17iPF9xI7SWDHX0rjN22x95XzMHE5Ke83

###Loading And Preprocessing of Dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, RepeatedStratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, StackingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from typing import Tuple, Dict
from pandas import DataFrame
from imblearn.over_sampling import SMOTE
from sklearn.utils.class_weight import compute_class_weight

# Function to load the dataset
def load_data(url: str) -> DataFrame:
    return pd.read_csv(url)

# Function to preprocess the data
def preprocess_data(data: DataFrame) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, LabelEncoder]:
    # Remove outliers before processing
    data = remove_outliers(data)

    X = data.drop('Frutto', axis=1)
    y = data['Frutto']

    # Encode categorical labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, label_encoder

# Function to remove outliers using the IQR method
def remove_outliers(data: DataFrame) -> DataFrame:
    for column in data.select_dtypes(include=[np.number]).columns:
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return data

# Function to visualize the dataset
def visualize_data(data: DataFrame) -> None:
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Peso (g)', y='Diametro medio (mm)', hue='Frutto', data=data, palette='viridis', s=100)
    plt.title("Weight vs. Average Diameter Distribution")
    plt.show()

    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Peso (g)', y='Lunghezza media (mm)', hue='Frutto', data=data, palette='viridis', s=100)
    plt.title("Weight vs. Average Length Distribution")
    plt.show()

    plt.figure(figsize=(12, 8))
    sns.heatmap(data.drop('Frutto', axis=1).corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

# Function to evaluate the model performance
def evaluate_model(model, X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, y_test: np.ndarray, label_encoder: LabelEncoder) -> None:
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    print("\nClassification report for training set:")
    print(classification_report(y_train, y_pred_train, target_names=label_encoder.classes_))

    print("\nClassification report for test set:")
    print(classification_report(y_test, y_pred_test, target_names=label_encoder.classes_))

    conf_matrix = confusion_matrix(y_test, y_pred_test)
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

# Function to create a KNN pipeline
def create_knn_pipeline(k: int) -> Pipeline:
    return Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=k))
    ])

# Function to create a Random Forest pipeline
def create_rf_pipeline(class_weights=None) -> Pipeline:
    return Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42,
                                      class_weight=class_weights,
                                      min_samples_split=5,
                                      min_samples_leaf=2))
    ])

# Function to create an SVM pipeline
def create_svm_pipeline(class_weights=None) -> Pipeline:
    return Pipeline([
        ('scaler', StandardScaler()),
        ('svm', SVC(kernel='linear', random_state=42, class_weight=class_weights))
    ])

# Function to perform hyperparameter optimization
def optimize_hyperparameters(model, param_grid: Dict, X_train: np.ndarray, y_train: np.ndarray) -> GridSearchCV:
    # Use repeated stratified K-Fold for more robust validation
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=42)
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv,
                               scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search

# Load the dataset
url = 'https://proai-datasets.s3.eu-west-3.amazonaws.com/fruits.csv'
data = load_data(url)

# Dataset overview
print("This dataset contains information about fruits with the following columns:")
print("1. Peso (g): Fruit weight in grams.")
print("2. Diametro medio (mm): Average diameter in millimeters.")
print("3. Lunghezza media (mm): Average length in millimeters.")
print("4. Frutto: Type of fruit (target label).")
print(f"\nDataset size: {data.shape}")
print("\nFirst rows:\n", data.head())
print("\nDataset info:\n", data.info())
print("\nDescriptive statistics:\n", data.describe())
print("\nMissing values:\n", data.isnull().sum())

# Visualize distribution of numerical variables
plt.figure(figsize=(18, 12))
data.hist(bins=30, edgecolor='black', linewidth=1.2)
plt.tight_layout()
plt.show()

# Visualize outliers
plt.figure(figsize=(18, 12))
sns.boxplot(data=data)
plt.title("Outlier Visualization")
plt.xticks(rotation=90)
plt.show()

# Preprocess data
X_train, X_test, y_train, y_test, label_encoder = preprocess_data(data)

# Balance dataset using SMOTE with reduced number of neighbors
smote = SMOTE(random_state=42, k_neighbors=1)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Compute class weights
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights_dict = {i: class_weights[i] for i in range(len(class_weights))}

# Visualize processed dataset
visualize_data(data)

"""📊 Dataset Description

This dataset contains 500 samples of fruits with the following 6 columns:
- Fruit: Type of fruit (categorical target)
- Weight (g): Weight of the fruit in grams
- Average Diameter (mm): Average diameter of the fruit in millimeters
- Average Length (mm): Average length of the fruit in millimeters
- Skin Hardness (1–10): Firmness of the fruit’s skin on a scale from 1 to 10
- Sweetness (1–10): Sweetness level of the fruit on a scale from 1 to 10

There are no missing values in the dataset, which simplifies preprocessing and eliminates the need for imputation.

---

🔍 Numerical Variable Distribution

- Histograms are used to visualize the distribution of numerical features.
- Boxplots reveal the presence of outliers in several numeric columns.

---

🧹 Outlier Handling

- Outliers are identified through boxplot inspection.
- The Interquartile Range (IQR) method is used to remove extreme values from the numerical variables during preprocessing.

---

🏷️ Label Encoding

- The categorical target column 'Fruit' is encoded using LabelEncoder to convert it into a numerical format suitable for machine learning algorithms.

---

⚖️ Feature Scaling

- Numerical variables are standardized using StandardScaler to normalize the feature space and improve model performance.

---

🔄 Dataset Balancing

- SMOTE (Synthetic Minority Over-sampling Technique) is applied with k_neighbors=1 to balance the dataset and reduce the risk of overfitting on synthetic examples.
- Class weights are calculated and passed to applicable classifiers to further address class imbalance during model training.

###Training and esecution of models
"""

#  Hyperparameter optimization for KNN, Random Forest, and SVM

# Define parameter grids for each model
knn_param_grid = {'knn__n_neighbors': range(1, 31)}
rf_param_grid = {
    'rf__n_estimators': [50, 100, 200],
    'rf__max_depth': [None, 10, 20, 30]
}
svm_param_grid = {
    'svm__C': [0.1, 1, 10],
    'svm__kernel': ['linear', 'rbf']
}

# Create pipelines with default or weighted settings
knn_pipeline = create_knn_pipeline(k=5)
rf_pipeline = create_rf_pipeline(class_weights=class_weights_dict)
svm_pipeline = create_svm_pipeline(class_weights=class_weights_dict)

# Perform hyperparameter tuning using GridSearchCV
knn_optimized = optimize_hyperparameters(knn_pipeline, knn_param_grid, X_train_res, y_train_res)
rf_optimized = optimize_hyperparameters(rf_pipeline, rf_param_grid, X_train_res, y_train_res)
svm_optimized = optimize_hyperparameters(svm_pipeline, svm_param_grid, X_train_res, y_train_res)

# Display the best parameters found for each model
print(" Best parameters for KNN:", knn_optimized.best_params_)
print(" Best parameters for Random Forest:", rf_optimized.best_params_)
print(" Best parameters for SVM:", svm_optimized.best_params_)

"""
🎯 Hyperparameter Optimization Summary

The hyperparameters for KNN, Random Forest, and SVM models were optimized using GridSearchCV
in combination with RepeatedStratifiedKFold. This approach enabled the following:

- Performed repeated stratified k-fold cross-validation to ensure more robust and reliable model evaluation.
- Explored multiple combinations of hyperparameters for each model, leading to improved overall performance.
"""

#  Training and Evaluation of Optimized Models
evaluate_model(knn_optimized.best_estimator_, X_train, y_train, X_test, y_test, label_encoder)
evaluate_model(rf_optimized.best_estimator_, X_train, y_train, X_test, y_test, label_encoder)
evaluate_model(svm_optimized.best_estimator_, X_train, y_train, X_test, y_test, label_encoder)

#  Gradient Boosting Implementation and Evaluation (XGBoost)
xgb_model = XGBClassifier(
    random_state=42,
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    reg_lambda=0.1
)

xgb_model.fit(X_train_res, y_train_res)
evaluate_model(xgb_model, X_train, y_train, X_test, y_test, label_encoder)

# 🤝Ensemble Learning: Voting Classifier (hard voting)
def create_voting_classifier(models: list) -> VotingClassifier:
    return VotingClassifier(estimators=models, voting='hard')

voting_clf = create_voting_classifier([
    ('knn', knn_optimized.best_estimator_),
    ('rf', rf_optimized.best_estimator_),
    ('svm', svm_optimized.best_estimator_),
    ('xgb', xgb_model)
])

voting_clf.fit(X_train_res, y_train_res)
evaluate_model(voting_clf, X_train, y_train, X_test, y_test, label_encoder)

#  Stacking Classifier using Logistic Regression as meta-model
stacking_clf = StackingClassifier(
    estimators=[
        ('knn', knn_optimized.best_estimator_),
        ('rf', rf_optimized.best_estimator_),
        ('svm', svm_optimized.best_estimator_),
        ('xgb', xgb_model)
    ],
    final_estimator=LogisticRegression(max_iter=1000)
)

stacking_clf.fit(X_train_res, y_train_res)
evaluate_model(stacking_clf, X_train, y_train, X_test, y_test, label_encoder)

#  Feature Importance Visualization (from Random Forest)
importances = rf_optimized.best_estimator_.named_steps['rf'].feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(12, 8))
plt.title("Feature Importances (Random Forest)")
plt.bar(range(X_train.shape[1]), importances[indices], align="center")
plt.xticks(range(X_train.shape[1]), [data.columns[i] for i in indices], rotation=90)
plt.xlim([-1, X_train.shape[1]])
plt.tight_layout()
plt.show()

"""
📈 Model Evaluation

The optimized models were evaluated on both the training and test sets using classification metrics such as
precision, recall, and F1-score. Confusion matrices were also visualized to assess each model's ability
to distinguish between fruit classes.

🤝 Ensemble Learning

A Voting Classifier and a Stacking Classifier were implemented using the best-performing optimized models.
Logistic Regression (with max_iter=1000) was used as the meta-model for the stacking architecture.

📊 Feature Importance

Feature importances from the Random Forest model were visualized to identify the most influential variables
in the classification task.
"""

#  Model Accuracy Comparison
print("\n🔍 Model Accuracy Comparison:")

print("KNN - Training Set Accuracy:", accuracy_score(y_train, knn_optimized.predict(X_train)))
print("KNN - Test Set Accuracy:", accuracy_score(y_test, knn_optimized.predict(X_test)))

print("Random Forest - Training Set Accuracy:", accuracy_score(y_train, rf_optimized.predict(X_train)))
print("Random Forest - Test Set Accuracy:", accuracy_score(y_test, rf_optimized.predict(X_test)))

print("SVM - Training Set Accuracy:", accuracy_score(y_train, svm_optimized.predict(X_train)))
print("SVM - Test Set Accuracy:", accuracy_score(y_test, svm_optimized.predict(X_test)))

print("XGBoost - Training Set Accuracy:", accuracy_score(y_train, xgb_model.predict(X_train)))
print("XGBoost - Test Set Accuracy:", accuracy_score(y_test, xgb_model.predict(X_test)))

print("Voting Classifier - Training Set Accuracy:", accuracy_score(y_train, voting_clf.predict(X_train)))
print("Voting Classifier - Test Set Accuracy:", accuracy_score(y_test, voting_clf.predict(X_test)))

print("Stacking Classifier - Training Set Accuracy:", accuracy_score(y_train, stacking_clf.predict(X_train)))
print("Stacking Classifier - Test Set Accuracy:", accuracy_score(y_test, stacking_clf.predict(X_test)))

"""###Conclusions and Insights

📌 Model Performance Summary

🔹 Random Forest (Test Set Accuracy: 0.86):
The Random Forest model demonstrated solid performance with 86% accuracy on the test set.
It provided a good balance between precision and recall across all classes.

🔹 KNN (Test Set Accuracy: 0.865):
K-Nearest Neighbors achieved 86.5% accuracy on the test set. However, the model exhibited slight overfitting when compared to the training set.

🔹 SVM (Test Set Accuracy: 0.9666):
The Support Vector Machine showed strong generalization ability, with consistent performance between the training and test sets and an accuracy of 96.66% on the test set.

🔹 XGBoost (Test Set Accuracy: 0.8875):
XGBoost performed very well on the test set (88.75%) but showed signs of overfitting, having reached 100% accuracy on the training set.

🔹 Ensemble Models – Voting & Stacking Classifiers:
Both ensemble methods achieved high test accuracy (88.75% for Voting, 87.5% for Stacking), indicating solid performance.
However, the slight performance gap between training and test sets suggests mild overfitting.

---

✅ Conclusion

- The **Stacking Classifier** and **SVM** models delivered the best overall performance, maintaining a strong balance between precision and recall.
- The **handling of outliers** and **class balancing (SMOTE + class weights)** contributed significantly to improving model performance.
- **Ensemble learning techniques** further enhanced the stability and robustness of predictions.

🔁 Future Work:
Iterating on these models with **more advanced cross-validation strategies** and fine-tuning could lead to further performance improvements.
"""