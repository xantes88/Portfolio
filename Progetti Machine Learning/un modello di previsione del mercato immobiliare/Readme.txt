# Housing Price Prediction Using Regularized Linear Models

## Introduction

Accurate estimation of housing prices is a significant challenge in the field of data analysis and machine learning. The availability of complex datasets containing both numerical and categorical variables requires robust techniques to effectively model the relationships between property features and their market value.

In this project, we develop regularized linear regression models to predict house prices based on a real-world dataset. The goal is to create predictive models that are reliable, generalizable, and interpretable by optimizing both accuracy and complexity through advanced preprocessing, feature engineering, and hyperparameter tuning.

---

## Dataset

The dataset used in this analysis contains detailed information about residential properties, including:

- **Numerical variables:** area (square footage), number of bedrooms, bathrooms, stories, and parking spaces.
- **Categorical variables:** presence of main road, guest room, basement, hot water heating, air conditioning, preferred area, and furnishing status.
- **Target variable:** price of the property.

The dataset includes missing values that are handled using appropriate imputation strategies to maintain data integrity without introducing bias.

---

## Methodology

### Preprocessing

- **Imputation:** For numerical variables, missing values are replaced with the median; for categorical variables, a constant value 'missing' is used.
- **Encoding:** Categorical variables are converted using One-Hot Encoding to create binary indicator features.
- **Scaling:** Numerical features are standardized using StandardScaler to ensure equal weighting in the models.
- **Feature Engineering:** Polynomial features of degree 2 are generated to capture potential nonlinear interactions between variables.
- **Data Splitting:** The dataset is split into training (80%) and test (20%) sets with a fixed random seed to ensure reproducibility.

### Models Considered

- **Ridge Regression:** Linear regression with L2 regularization to prevent overfitting and shrink coefficients.
- **Lasso Regression:** Linear regression with L1 regularization that promotes sparsity, effectively performing feature selection.
- **Elastic Net Regression:** Combines L1 and L2 penalties to balance feature selection and coefficient shrinkage.

### Hyperparameter Optimization and Validation

- **Search Procedure:** RandomizedSearchCV with 5-fold cross-validation is applied to identify optimal regularization parameters.
- **Evaluation Metrics:** Root Mean Squared Error (RMSE) and R-squared (R²) scores are computed on both training and test datasets.
- **Model Complexity:** Assessed by counting the number of non-zero coefficients to understand feature relevance.
- **Visualization:** Residual plots and coefficient paths provide insights into model performance and behavior.

---

## Results

### Performance on Training and Test Sets

| Model             | Dataset  | RMSE          | R-squared | Number of Non-zero Coefficients |
|-------------------|----------|---------------|-----------|---------------------------------|
| Ridge Regression  | Training | 875,436.67    | 0.7514    | 90                              |
| Ridge Regression  | Test     | 1,394,364.27  | 0.6153    | 90                              |
| Lasso Regression  | Training | 798,409.85    | 0.7933    | 82                              |
| Lasso Regression  | Test     | 1,404,576.09  | 0.6097    | 82                              |
| Elastic Net       | Training | 854,360.18    | 0.7633    | 90                              |
| Elastic Net       | Test     | 1,383,832.28  | 0.6211    | 90                              |

### Cross-Validation Results (mean ± standard deviation)

| Model            | Mean Squared Error           | R-squared               |
|------------------|------------------------------|-------------------------|
| Ridge Regression | 1.08 × 10¹² ± 2.23 × 10¹¹    | 0.6422 ± 0.0562         |
| Lasso Regression | 1.64 × 10¹² ± 5.97 × 10¹¹    | 0.4777 ± 0.1152         |
| Elastic Net      | 1.08 × 10¹² ± 2.18 × 10¹¹    | 0.6445 ± 0.0550         |

---

## Interpretation of Results

- Both Ridge and Elastic Net models exhibit similar and relatively strong performance, with good generalization ability on the test dataset.
- Lasso regression produces sparser models by zeroing out more coefficients, which aids interpretability but results in a slight decrease in predictive accuracy on the test set.
- R-squared values above 0.6 suggest that these models explain a significant portion of the variance in housing prices.
- The moderate gap between training and test scores indicates an appropriate balance between bias and variance, reflecting moderate model complexity.
- Residual analysis and coefficient path tracking across regularization parameters validate the stability and robustness of the models.

---

## Conclusions

This project demonstrates how combining advanced preprocessing techniques, regularization methods, and hyperparameter optimization leads to effective and interpretable regression models for housing price prediction.

Among the tested models, Elastic Net offers a balanced trade-off between prediction accuracy and model complexity. Lasso regression can be preferred when feature selection and model interpretability are the primary objectives.

Future improvements could include:

- Incorporating additional external or temporal features to enrich the dataset.
- Exploring nonlinear models and ensemble techniques for potentially improved performance.
- Applying interpretability frameworks such as SHAP to quantify the impact of individual features on predictions.

---

## How to Run

1. Clone the repository to your local machine.
2. Install the required Python dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn scipy joblib
