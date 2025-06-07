🏠 Real Estate Price Evaluation with Regularized Regression

📌 Project Summary

This project builds a machine learning pipeline to predict house prices using regularized linear regression models and advanced feature engineering.

Through a rigorous process of preprocessing, model optimization, and residual analysis, this solution provides actionable insights into real estate price dynamics.

📊 Dataset Overview
Source: Housing dataset (500+ samples)

Target: price — sale price of residential properties

Features:

Numerical: area, bedrooms, bathrooms, stories, parking

Categorical: mainroad, guestroom, basement, airconditioning, furnishing status, etc.

All categorical variables are handled via one-hot encoding, while missing values are imputed and features are polynomially expanded to improve model expressiveness.

🛠 Techniques & Models Used
🔧 Preprocessing
One-hot encoding of categorical variables

Missing value imputation (SimpleImputer)

Feature scaling (StandardScaler)

Polynomial feature expansion (degree = 2)

📈 Regression Models
Ridge Regression (L2 regularization)

Lasso Regression (L1 regularization)

Elastic Net (L1 + L2 hybrid)

⚙️ Optimization
Hyperparameter Tuning via RandomizedSearchCV

Cross-validation using 5-Fold KFold

Coefficient path visualization

Residual analysis: histograms, Q-Q plots, and scatterplots

📐 Model Performance
Model	Train R²	Test R²	Regularization
Ridge Regression	~0.69	~0.61	L2
Lasso Regression	~0.68	~0.61	L1
Elastic Net	~0.68	~0.61	L1 + L2

All models explained approximately 61% of price variance on the test set — a solid baseline given the limited dataset size and features.

📉 Residual & Coefficient Analysis
Each model was thoroughly evaluated through:

✅ Residual distribution plots (to validate normality and homoscedasticity)

✅ Coefficient sparsity (especially with Lasso and ElasticNet)

✅ Stability of coefficients across varying alpha values

This adds interpretability and confidence for stakeholders — particularly valuable in domains like finance, real estate, or operations.

💼 Business Value
✅ Shows capability to model real estate pricing with interpretable and explainable models
✅ Demonstrates fluency in end-to-end regression pipelines, including tuning, diagnostics, and visual reporting
✅ Enables better data-driven decisions for stakeholders (real estate agencies, investors, etc.)

🔍 Key Learnings
All three models performed comparably on this dataset.

Regularization helped reduce overfitting, especially for Lasso.

Despite limited data, a properly engineered pipeline yields robust insights.

🔮 Next Steps
Add geospatial features (e.g., proximity to services, transport)

Integrate external macroeconomic variables

Deploy model as an interactive web app with Streamlit or FastAPI
