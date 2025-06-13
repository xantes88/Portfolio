# 📊 Advanced Analytics for Invoice Payment Risk
 
**Proactive Invoice Monitoring with Machine Learning, SHAP & SAP-like Simulation**

> Predict which vendor invoices are at risk of late payment and prioritize action before financial damage occurs.

---

## 💼 Executive Summary

Companies often lose thousands of euros every month due to late invoice payments. This project simulates a real-world Shared Services Center scenario using SAP-like data fields (e.g., `gl_code`, `company_code`, `vendor_region`, `invoice_block_reason`) and builds an ML-based risk detection system.

With predictive analytics, explainable AI (SHAP), and Power BI reporting, the solution enables **proactive intervention** and **cash flow optimization** — even before the due date hits.

---

## 🔍 Business Scenario

**🧾 Company Profile**  
- Mid-sized enterprise with 5 business units and 50K+ invoices/year  
- AP team of 6 using SAP and multiple vendor regions  
- Frequent issues with blocked invoices, missing PO, delayed vendor replies

**🚨 Problem**  
- ~20% of invoices paid late  
- Lost early payment discounts and penalties (~€1.2M/year)  
- Manual reviews consume time, no clear visibility on invoice risk

**✅ Solution**  
This project builds a machine learning classifier to flag at-risk invoices **before** due date and assigns a `priority_action`. Example output:

| invoice_id | vendor_name     | risk_score | priority_action         |
|------------|------------------|------------|--------------------------|
| 145        | Vendor IT S.p.A  | 0.82       | Immediate Reminder       |
| 288        | Office Srl       | 0.77       | Monitor – Response Delay |
| 391        | General Maint.   | 0.35       | Low Risk – No Action     |

---

## 💰 Estimated ROI – Simulation

📊 **Annual Impact:**
- 50,000 invoices/year × 20% late = 10,000 at risk
- If 12% of them are corrected → 6,000 timely payments
- Avg. saving per invoice = €80 (discounts, penalties, workload)
- 💸 **€480,000/year recovered** (cash flow + avoided penalties)

---

## 🔧 Features & Pipeline

- ✅ **SAP-like Fields**: `gl_code`, `company_code`, `vendor_region`, `invoice_block_reason`, `payment_term`
- 📈 **Modeling**: Random Forest & XGBoost + SMOTE + Stratified K-Fold
- 🧠 **Explainability**: SHAP Summary plots for both models
- 📊 **Power BI Dashboard**: Regional KPI, Vendor ranking, Action tracking
- 🔁 **Retraining Logic**: Auto-retrain monthly when `new_data.csv` is added
- 🛠️ **Deployment-Ready Output**: CSV with actionable alerts

---

## 🧠 Workflow

1. **Data Simulation** of 1,000 invoices (realistic SAP-style fields)
2. **Feature Engineering** (urgency score, overdue flag, vendor risk)
3. **Model Training** (SMOTE + Cross-Validation)
4. **Explainability** (SHAP for RF and XGBoost)
5. **Output CSV + Dashboard** (risk, priority, action type)
6. **Retraining block** (`if new_data: retrain()`)

---

## 📊 Dashboard Preview (Power BI)

![powerbi](images/powerbi_dashboard.png)

> Real-time visual of invoice risk by vendor, region, GL account, and total exposure. Designed for AP managers and controllers.

---

## 🛠 Deployment & Integration

📥 **Input**  
`invoices_enhanced.csv`: all SAP-like features and labels  
`new_data.csv`: optional for future retraining

📤 **Output**  
- `alerts.csv` → for action tracking  
- `shap_summary_rf.png`, `shap_summary_xgb.png`  
- `PowerBI .pbix` or dashboard image

🧩 **To Integrate**  
- Upload alerts to ServiceNow or ERP  
- Embed Power BI dashboard in finance portal  
- Automate retraining monthly via cron/GitHub Actions


## 📌 Summary for Business

**If you're a CFO or Finance Ops Lead, here’s what this project offers you:**

- ✔️ Visibility on upcoming payment risks  
- ✔️ Prioritized action list to avoid penalties  
- ✔️ Estimated savings: €480K/year (mid-size org)  
- ✔️ Immediate dashboard integration with Power BI  
- ✔️ Ready for production or advanced analysis

---

## 🤖 Future Improvements

- Add LLM-based extraction from raw invoices (PDF)
- Integrate with SAP BTP or Esker API
- Build Streamlit/Gradio UI for operator workflow

---
