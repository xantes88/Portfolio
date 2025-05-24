# Fruit Classification with Machine Learning Models

## Project Description

This project implements an automated classification system for different types of fruits based on their physical measurements (weight, dimensions, sensory characteristics). It applies data preprocessing, balancing, hyperparameter optimization, and supervised learning models to achieve high predictive performance.

---

## Dataset

The dataset contains 500 fruit samples with the following features:

- **Weight (g)**: Weight of the fruit in grams.
- **Average Diameter (mm)**: Average diameter of the fruit.
- **Average Length (mm)**: Average length of the fruit.
- **Peel Hardness (1-10)**: Peel hardness rating.
- **Sweetness (1-10)**: Sweetness rating.
- **Fruit**: Fruit type (target variable).

The dataset contains no missing values but includes some outliers which are removed using the Interquartile Range (IQR) method.

---

## Techniques Implemented

### Preprocessing
- Outlier removal via IQR method.
- Target encoding using `LabelEncoder`.
- Feature scaling with `StandardScaler`.
- Dataset balancing using SMOTE with reduced neighbors (`k=1`) to prevent overfitting.
- Class weight calculation to handle residual class imbalance during training.

### Data Visualization
- Histograms of numeric variable distributions.
- Boxplots for outlier detection.
- Scatter plots to examine relationships between physical features.
- Correlation matrix heatmap to analyze feature dependencies.

### Machine Learning Models
- K-Nearest Neighbors (KNN)
- Random Forest
- Support Vector Machine (SVM)
- XGBoost (Gradient Boosting)

Hyperparameters are optimized using `GridSearchCV` with `RepeatedStratifiedKFold` for robust cross-validation.

### Ensemble Learning
- **Voting Classifier:** Combines KNN, Random Forest, SVM, and XGBoost using hard voting.
- **Stacking Classifier:** Uses the same base models with Logistic Regression as the meta-model.

---

## Model Evaluation

Metrics used include accuracy, precision, recall, and F1-score. Performance is analyzed via classification reports and confusion matrices.

### Sample Classification Reports

**K-Nearest Neighbors (KNN)**

| Class   | Precision | Recall | F1-score | Support |
|---------|-----------|--------|----------|---------|
| Arancia | 0.88      | 0.90   | 0.89     | 83      |
| Banana  | 1.00      | 1.00   | 1.00     | 3       |
| Kiwi    | 0.90      | 0.89   | 0.90     | 82      |
| Mela    | 0.93      | 0.92   | 0.93     | 74      |
| Uva     | 1.00      | 1.00   | 1.00     | 78      |

**Training Accuracy:** 93%

**Test Set Performance**

| Class   | Precision | Recall | F1-score | Support |
|---------|-----------|--------|----------|---------|
| Arancia | 0.71      | 0.71   | 0.71     | 17      |
| Banana  | 1.00      | 1.00   | 1.00     | 1       |
| Kiwi    | 0.70      | 0.78   | 0.74     | 18      |
| Mela    | 1.00      | 0.92   | 0.96     | 26      |
| Uva     | 1.00      | 1.00   | 1.00     | 18      |

**Test Accuracy:** 86%

*(Similar detailed reports are available for Random Forest, SVM, XGBoost, Voting, and Stacking classifiers.)*

---

## Final Considerations

- Models demonstrate high precision and recall on the training set, indicating good learning ability.
- Test results show slightly lower performance for some classes (e.g., Arancia, Kiwi), suggesting room for improvement in generalization.
- Ensemble methods (Voting and Stacking) generally improve overall accuracy and robustness by leveraging strengths of individual classifiers.
- Size-related features (weight, diameter, length) consistently emerge as the most important predictors.
- SMOTE balancing with a low number of neighbors (k=1) effectively mitigates class imbalance without inducing overfitting.
- Future work may include advanced feature engineering, testing additional classifiers, or employing deep learning techniques.

---

## How to Use This Project

### Requirements

- Python 3.7+
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `imbalanced-learn`

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn
