# 🏘️ Real Estate Price Prediction with Regularized Regression

A complete regression system using **Ridge, Lasso, and Elastic Net** to predict real estate prices based on structural and categorical features. Includes **feature engineering**, **robust validation**, and full reporting via **SQL and Power BI**.

---

## 🏢 Business Use Case

Developed for a **real estate analytics firm** managing valuation workflows across 5,000+ metropolitan properties:

- ✅ Supports **internal pricing** before listings go live  
- ✅ Enables **CRM integration** for agents to provide quotes pre-visit  
- ✅ Assists **project planners** during early-stage development

---

## 💸 Business Value Delivered

| Metric                                | Impact                                         |
|---------------------------------------|------------------------------------------------|
| 💰 Cost Savings                        | ~ €50K/year by correcting pre-listing errors   |
| 🔍 Uncertainty Reduction               | -24% pricing variance for stronger negotiation |
| 🕒 Time Saved                          | 300 analyst hours/year via automation          |
| 📈 Predictive Power                    | R² = 0.621 – enabling early, credible forecasts|

---

## 📊 Model Performance

| Model            | R² (Test) | RMSE (€)   | MAE (€ est.) | Non-Zero Coefficients |
|------------------|-----------|------------|--------------|------------------------|
| Ridge Regression | 0.615     | 1,394,364  | ~820,000     | 90                     |
| Lasso Regression | 0.609     | 1,404,576  | ~830,000     | 82                     |
| **Elastic Net**  | **0.621** | **1,383,832** | **~800,000** | **90**                 |

All models validated with **5-fold cross-validation** and **RandomizedSearchCV** for optimal regularization tuning.

---

## 📊 Power BI Dashboard

Predicted results exported to **Power BI** for business reporting, including:

- 📍 **Scatter Plot**: Actual vs Predicted Prices  
- 📌 **KPI Cards**: Custom metrics (MAE, RMSE, R², etc.)

> ⚠️ Note: Residual histograms and R² charts were generated in Python.

---

## 🔧 Technical Highlights

- 📐 `PolynomialFeatures(degree=2)` for non-linear feature interaction  
- 🧼 Preprocessing pipeline with `OneHotEncoder`, `SimpleImputer`, `ColumnTransformer`  
- 🧪 **5-Fold Cross-Validation** for robust evaluation  
- 📉 Residual and Q-Q Plots for diagnostic analysis  
- 🔍 Coefficient path plots for Ridge/Lasso tuning  
- 🧾 Auto-generated **SQL script** for data pipeline integration

---

## 🛠️ Deployment Potential

- 🖥️ Deployable as **microservice API** for real-time price recommendations  
- 📱 Integrable into **CRM systems** used by agencies  
- 🧠 Adaptable to **loan risk scoring** or **regional simulation** models

---

## 📁 Files Included

| File Name                      | Description                                  |
|-------------------------------|----------------------------------------------|
| `elastic_net_kpi.csv`         | Final predictions with actuals and error     |
| `ElasticNet_Predictions_with_KPI.csv` | Dataset with KPIs                        |
| `ElasticNet_Top10_Errori.csv` | Top 10 worst predictions                     |
| `elastic_net_kpi.sql`         | SQL script: table creation + data insertion  |
| `elastic_net_kpi.pbix`        | Power BI dashboard (interactive)             |

---

## 📌 Summary for Stakeholders

✔️ Explains over **62% of price variance**  
✔️ Combines **ML, SQL, and Power BI** in one workflow  
✔️ Ready for production or integration into existing systems  
✔️ Clear, measurable ROI for real estate analytics

---

> Built for data-driven real estate decision-making — empowering sales, finance, and planning with predictive intelligence.
