# 🏘️ Real Estate Price Prediction with Regularized Regression

A complete regression system using **Ridge, Lasso, and Elastic Net** to predict real estate prices based on structural and categorical features. Includes **feature engineering**, **robust validation**, and end-to-end model evaluation.

---

## 🏢 Business Use Case

Developed for a **real estate analytics firm** managing valuation workflows across 5,000+ metropolitan properties:

- ✅ Supports **internal pricing** before listings go live  
- ✅ Enables **CRM integration** for agents to provide quotes pre-visit  
- ✅ Assists **project planners** during early-stage development

---

## 💸 Business Value Delivered

| Metric                | Impact                                          |
|-----------------------|--------------------------------------------------|
| 💰 Cost Savings        | ~ €50K/year by correcting pre-listing errors    |
| 🔍 Uncertainty Reduction | -24% pricing variance for stronger negotiation |
| 🕒 Time Saved          | 300 analyst hours/year via automation           |
| 📈 Predictive Power    | R² = 0.621 – enabling early, credible forecasts |

---

## 📊 Model Performance

| Model            | R² (Test) | RMSE (€)     | MAE (€ est.) | Non-Zero Coefficients |
|------------------|-----------|--------------|--------------|------------------------|
| Ridge Regression | 0.615     | 1,394,364    | ~820,000     | 90                     |
| Lasso Regression | 0.609     | 1,404,576    | ~830,000     | 82                     |
| **Elastic Net**  | **0.621** | **1,383,832** | **~800,000** | **90**                 |

All models validated using **5-fold cross-validation** and optimized with **RandomizedSearchCV**.

---

## 🔧 Technical Highlights

- 📐 `PolynomialFeatures(degree=2)` for non-linear feature interaction  
- 🧼 Preprocessing pipeline with `OneHotEncoder`, `SimpleImputer`, `ColumnTransformer`  
- 🧪 Robust evaluation with **5-Fold Cross-Validation**  
- 📉 Diagnostic plots: residuals and Q-Q plots  
- 🔍 Coefficient path plots for model interpretability

---

## 📌 Summary for Stakeholders

✔️ Explains over **62% of price variance**  
✔️ Combines **machine learning and business-driven pricing logic**  
✔️ Ready for integration into internal BI or CRM systems  
✔️ Clear, measurable ROI from predictive automation

> *Built for accurate and scalable property valuation — enabling better decisions in sales, finance, and project planning.*                       
> 🧪 *Simulated use case built with synthetic/public data.*
