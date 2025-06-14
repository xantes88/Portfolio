# 📊 Advanced Analytics for Invoice Payment Risk

Proactive Invoice Monitoring with Machine Learning, SHAP & SAP-like Simulation

Predict which vendor invoices are at risk of late payment and prioritize action before financial damage occurs.

---

## 💼 Executive Summary

Companies lose substantial amounts monthly due to late invoice payments.  
This project simulates a real-world Shared Services Center environment using SAP-like invoice fields (e.g., `gl_code`, `company_code`, `vendor_region`, `invoice_block_reason`) and develops a machine learning-based risk detection system.

Leveraging predictive analytics, explainable AI (SHAP), and Power BI reporting, it enables proactive intervention and cash flow optimization — detecting payment risks **before due dates**.

---

## 🔍 Business Scenario

### 🧾 Company Profile  
- Mid-sized enterprise with 5 BUs processing 50,000+ invoices/year  
- AP team of 6 managing SAP workflows across multiple vendor regions  
- Common issues: blocked invoices, missing POs, delayed vendor responses  

### 🚨 Problem  
- ~20% of invoices paid late  
- Lost early payment discounts and penalties ≈ **€1.2M/year**  
- Manual reviews = slow, reactive, error-prone  

---

## ✅ Solution  
> **Machine learning model** to predict invoice payment risk and assign priority actions  
> Sample output:

| invoice_id | vendor_name     | risk_score | priority_action         |
|------------|------------------|------------|--------------------------|
| 145        | Vendor IT S.p.A   | 0.82       | Immediate Reminder       |
| 288        | Office Srl        | 0.77       | Monitor – Response Delay |
| 391        | General Maint.    | 0.35       | Low Risk – No Action     |

---

## 💰 Simulated ROI – Business Impact

- 50,000 invoices/year × 20% late = **10,000 at risk**  
- If 12% corrected → 6,000 timely payments  
- Average saving/invoice = **€80** (discounts + penalties + time)  
### 🟢 **€480,000/year recovered** in working capital & efficiency  

---

## 🔧 Technical Features

- ✅ SAP-like Fields: `gl_code`, `payment_term`, `invoice_block_reason`, `vendor_region`  
- 📈 Modeling: XGBoost + Random Forest, SMOTE, Stratified K-Fold  
- 🧠 Explainability: SHAP plots (`shap_summary_xgb.png`, `shap_summary_rf.png`)  
- 📊 **Power BI Dashboard**: vendor risk KPIs, exposure heatmaps, intervention alerts  
- 🔁 Retraining logic included (`if new_data.csv → retrain()`)  
- 🛠 Output: `alerts.csv`, `dashboard.pbix`, SHAP visuals

---

## 📊 Dashboard Preview (Power BI)

![Dashboard Preview](https://github.com/xantes88/Portfolio/raw/main/Progetti%20Machine%20Learning/Advanced%20Analytics%20for%20Invoice%20Payment%20Risk/invoice_dashboard_preview.png)

> Real-time visibility into vendor payment risk, GL account, and priority actions.  
Tailored for AP managers, controllers, and CFOs.

### 📥 Download the full `.pbix` dashboard: [Invoice_Risk_Dashboard.pbix](./Invoice_Risk_Dashboard.pbix)

---

## 🧠 Workflow

1. 🧾 **Data Simulation** – 1,000+ invoices with SAP-style features  
2. ⚙️ **Feature Engineering** – urgency, overdue flag, vendor history  
3. 🧠 **Model Training** – SMOTE balancing, cross-validation  
4. 📈 **Explainability** – SHAP plots for model transparency  
5. 📤 **Outputs** – risk scores, `alerts.csv`, dashboard  
6. 🔁 **Retraining Block** – continuous learning enabled  

---

## 🔗 Integration Options

- Push alerts to ERP / ServiceNow  
- Embed dashboard in Power BI service  
- Automate retraining via GitHub Actions  
- (Planned) LLMs for OCR invoice ingestion  
- (Planned) SAP BTP + Esker integration  

---

## 📌 Summary for Decision Makers

If you are a CFO, Controller or Finance Ops Lead, this project enables:

✔️ Early warning system for at-risk invoices  
✔️ Estimated savings: **€480K/year**  
✔️ ERP-ready outputs (CSV, dashboard)  
✔️ Seamless adoption in Shared Services  
✔️ Deployable & scalable with retraining logic

