🏘️ Real Estate Price Prediction with Regularized Regression
A complete regression system using Ridge, Lasso, and Elastic Net models to predict real estate prices based on structural and categorical features. The solution includes feature engineering, robust validation, and full reporting via SQL and Power BI.

🏢 Business Use Case
Developed for a real estate analytics firm managing valuation workflows across 5,000+ properties in metropolitan markets:

✅ Supports internal pricing recommendations before listings go live

✅ Enables CRM integration for agents to provide pre-visit quotes

✅ Assists project planners during early-stage development phases

💸 Business Value Delivered
💰 €50K/year saved by correcting pre-listing underpricing

🔍 24% reduction in pricing uncertainty for better negotiation leverage

🕒 300 analyst hours/year saved via automation

📈 62.1% of price variance explained, enabling early, credible forecasts

📊 Model Performance
Model	R² (Test)	RMSE (Test)	MAE (Est.)	Non-Zero Coeff.
Ridge Regression	0.615	€1,394,364	~€820,000	90
Lasso Regression	0.609	€1,404,576	~€830,000	82
Elastic Net (best)	0.621	€1,383,832	~€800,000	90

All models trained using 5-fold cross-validation and optimized via RandomizedSearchCV.

📊 Power BI Dashboard

Predicted results exported and visualized via Power BI, including:

📍 Scatter Plot: Actual vs Predicted Prices

📌 KPI Cards: Custom measures (e.g. MAE, RMSE) calculated and displayed for quick overview

Note: Residual Distribution Histogram and R² KPI card were generated in Python during model evaluation, not in Power BI.

🔧 Technical Highlights
📐 PolynomialFeatures(degree=2) for non-linear interactions

🧼 Preprocessing pipeline with one-hot encoding and imputation via ColumnTransformer

🧪 Robust 5-fold CV evaluation

📉 Residual plots and Q-Q plots to validate assumptions (Python)

🔍 Coefficient path plots to assess regularization impact

🧾 Auto-generated SQL script for table creation and data insertion

🛠️ Deployment Potential
🖥️ Deployable as a microservice API for real-time price suggestions

📱 Integrable with CRM systems used by real estate agencies

🧠 Adaptable for loan risk scoring or regional price simulation tools

📁 Files Included
File	Description
elastic_net_kpi.csv	Final predictions with actual prices and errors
ElasticNet_Predictions_with_KPI.csv	KPI-enhanced prediction dataset
ElasticNet_Top10_Errori.csv	Top 10 most inaccurate predictions
elastic_net_kpi.sql	SQL DDL + DML script for database integration
Valutazione Mercato Mobiliare.pbix	Power BI dashboard (interactive reporting)

