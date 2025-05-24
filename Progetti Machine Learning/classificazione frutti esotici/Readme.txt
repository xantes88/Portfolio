# Fruit Classification with Machine Learning Models

## Project Description
This project implements an automated classification system for different types of fruits based on their physical measurements (weight, dimensions, sensory characteristics). It applies data preprocessing, balancing, hyperparameter optimization, and supervised learning models to achieve high predictive performance.

## Dataset
The dataset contains 500 fruit samples with the following columns:

- **Weight (g):** Weight of the fruit in grams.
- **Average Diameter (mm):** Average diameter of the fruit.
- **Average Length (mm):** Average length of the fruit.
- **Peel Hardness (1-10):** Peel hardness rating.
- **Sweetness (1-10):** Sweetness rating.
- **Fruit:** Fruit type (target variable).

The dataset contains no missing values and includes some outliers that are removed using the Interquartile Range (IQR) method.

## Techniques Implemented

### Preprocessing
- Outlier removal via IQR.
- Target encoding using `LabelEncoder`.
- Feature scaling with `StandardScaler`.
- Dataset balancing using SMOTE with reduced neighbors (k=1) to prevent overfitting.
- Class weight calculation for handling residual class imbalance during training.

### Data Visualization
- Histograms of numeric variable distributions.
- Boxplots for outlier visualization.
- Scatter plots for relationships between physical features.
- Correlation matrix heatmap to analyze feature dependencies.

### Machine Learning Models
Implemented and optimized models include:
- K-Nearest Neighbors (KNN)
- Random Forest
- Support Vector Machine (SVM)
- XGBoost (Gradient Boosting)

Hyperparameters are optimized using `GridSearchCV` with `RepeatedStratifiedKFold` for robust cross-validation.

### Ensemble Learning
- **Voting Classifier:** Combines KNN, Random Forest, SVM, and XGBoost using hard voting.
- **Stacking Classifier:** Uses the same base models with Logistic Regression as the meta-model.

### Model Evaluation
- Metrics: accuracy, precision, recall, F1-score.
- Classification reports for training and test sets.
- Confusion matrices for detailed performance analysis.
- Feature importance visualization (Random Forest).

## Classification Reports

### K-Nearest Neighbors (KNN)

**Training set:**

| Class   | Precision | Recall | F1-score | Support |
|---------|-----------|--------|----------|---------|
| Arancia | 0.88      | 0.90   | 0.89     | 83      |
| Banana  | 1.00      | 1.00   | 1.00     | 3       |
| Kiwi    | 0.90      | 0.89   | 0.90     | 82      |
| Mela    | 0.93      | 0.92   | 0.93     | 74      |
| Uva     | 1.00      | 1.00   | 1.00     | 78      |
| **Accuracy** |       |        | **0.93** | 320     |

**Test set:**

| Class   | Precision | Recall | F1-score | Support |
|---------|-----------|--------|----------|---------|
| Arancia | 0.71      | 0.71   | 0.71     | 17      |
| Banana  | 1.00      | 1.00   | 1.00     | 1       |
| Kiwi    | 0.70      | 0.78   | 0.74     | 18      |
| Mela    | 1.00      | 0.92   | 0.96     | 26      |
| Uva     | 1.00      | 1.00   | 1.00     | 18      |
| **Accuracy** |       |        | **0.86** | 80      |

*(Similar detailed classification reports are available for Random Forest, SVM, XGBoost, Voting, and Stacking classifiers.)*

## Final Considerations

- The models generally achieve high precision and recall on the training set, indicating good learning capacity.
- Test set results show slightly lower scores, especially for some classes like "Arancia" and "Kiwi," suggesting potential room for improvement in generalization.
- Ensemble methods (Voting and Stacking) typically improve overall accuracy and robustness by combining strengths of individual classifiers.
- Features related to fruit size (weight, diameter, length) are consistently the most important predictors.
- SMOTE balancing with a low number of neighbors (k=1) effectively mitigated class imbalance without causing overfitting.
- Future improvements could include more advanced feature engineering, testing additional classifiers, or using deep learning approaches.

## How to Use This Project

### Requirements
- Python 3.7+
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, imblearn

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn
