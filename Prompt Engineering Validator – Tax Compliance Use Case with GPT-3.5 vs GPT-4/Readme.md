# 🤖 Prompt Evaluation System for Italian VAT Compliance

_Built for high-stakes finance workflows by a specialist in SAP AP, automation, and AI QA engineering._

**AI Prompt Benchmarking for Tax Compliance — GPT-3.5 vs GPT-4**

---

## 🧠 Executive Summary

Many companies struggle to validate the **regulatory accuracy** and **business relevance** of LLM-generated content.  
This project simulates how a **Prompt QA Specialist** can build an evaluation pipeline to automatically score, compare, and improve GPT outputs — using a real-world example: **VAT compliance for Italian SRLs (limited liability companies)**.

By combining GPT-3.5 and GPT-4 with a structured keyword-scoring system, this tool benchmarks performance across legal, fiscal, and linguistic dimensions. It reflects a **credible, deployable Prompt QA framework** aligned with business outcomes in compliance, finance, and ERP automation.

> 📌 Simulated for portfolio purposes. Not affiliated with any client or production system.

---

## 💼 Business Scenario

- **Industry**: Finance / Regulatory / Compliance  
- **Problem**: Manual compliance documentation is slow, error-prone, and inconsistent  
- **Solution**: Leverage LLMs to draft and validate structured tax content  
- **Goal**: Build a scalable **Prompt QA system** for high-stakes workflows (SAP, ERP, Audit)

---

## ⚙️ Key Features

- 🔁 **Multi-model execution** (GPT-3.5 & GPT-4)
- 🧠 **Automated scoring** across 5 keyword categories:
  - Compliance terms  
  - Legal references  
  - Accuracy & Precision  
  - Technical phrasing
- 📊 **Diagnostic reports** (.CSV, .PNG, .JSON, .MD)
- 🧰 **LangChain-powered modularity**
- ⏱️ **Fallback logic + timing benchmark**

---

## 🧪 Prompt Example

```text
You are an Italian tax expert. Briefly list the main VAT obligations for an SRL (limited liability company) under the standard tax regime in 2024. Reply with 5 concise bullet points.
```

---

## 📤 GPT Output Comparison

### 🔹 GPT-3.5-Turbo
- ✅ Avg Score: **89.8%**
- ⏱ Avg Time: 4.2s
- 📊 Score Range: 86.4% – 94.5%
- 🧠 100% Legal Structure (5-point)
- 💬 Proper Italian Language: 100%
- 📄 Keyword Accuracy: Strong technical terms, moderate compliance/legal terms

### 🔷 GPT-4
- ✅ Avg Score: **87.3%**
- ⏱ Avg Time: 47s
- 📊 Score Range: 85.4% – 90.8%
- 🧠 100% Legal Structure (5-point)
- 💬 Proper Italian Language: 100%
- 📄 Higher legal references but lower keyword precision overall

> 📌 GPT-3.5 consistently outperformed GPT-4 on keyword scoring (especially compliance terms), while GPT-4 excelled in legal depth and monetary precision.

---

## 📊 KPIs & ROI Simulation

| Metric                     | Manual Process | LLM-Augmented |
|---------------------------|----------------|----------------|
| Avg Response Time         | 20–30 min      | < 30 sec       |
| Review Effort             | High           | Low            |
| Keyword Accuracy          | N/A            | 90%+           |
| Evaluation Speed          | N/A            | 10× faster     |

> ⚙️ Designed for prompt QA in finance, tax advisory, ERP chatbots, or multilingual compliance support.

---

## 💡 Use Case Extensions

- 📈 **FP&A Reporting QA**: Validate structure and logic of generated insights
- ⚖️ **Legal Draft QA**: Score contractual or compliance clauses
- 🧾 **SAP Finance**: Evaluate invoice/tax prompt accuracy before API call
- 💬 **Customer Support QA**: Auto-evaluate chatbot accuracy (IT/EN)
- 🧠 **Training Material Check**: Score onboarding or compliance modules

---

## 💰 Simulated Business Impact

| Use Case                          | Estimated Savings     | Strategic Benefit                        |
|----------------------------------|-----------------------|------------------------------------------|
| VAT Compliance QA                | €15,000–25,000/year   | Reduced review time + higher accuracy    |
| Legal Prompt Validation          | €20,000+/year         | Lower risk of regulatory error           |
| FP&A Insight Evaluation          | 30% faster time-to-report | More confident decision-making     |
| Cross-border Prompt QA           | €40,000+/year         | Improved consistency across languages    |

> Based on simulated ROI models from SAP workflows and Prompt QA best practices.

---

## 📂 Output Files

- `vat_result_[model].csv`: Detailed scoring logs
- `chart_[model].png`: Visual keyword match comparison
- `diagnostic_[model].json`: JSON diagnostics per iteration
- `vat_comparison_[model].md`: Markdown report summary

---

## 👤 Author & Expertise

Developed by **Federico Petillo** — Finance Ops & AI Specialist combining 5+ years in SAP-driven Accounts Payable with hands-on AI deployment for automation, risk detection, and prompt evaluation.

- 📌 SAP AP Optimization & Invoice Workflow Efficiency
- 🤖 AI for Invoice Risk Detection (XGBoost, SHAP, Power BI)
- 🔍 Prompt QA Systems for Finance and Compliance
- 🧰 LangChain, GPT API, Python, SQL, ERP scenarios

🔗 [GitHub Portfolio](https://github.com/xantes88)

> From SAP to Smart Ops — This project blends prompt engineering with finance domain expertise to create scalable, high-trust AI automations.

---

## 🔮 Future Enhancements

- [ ] Add **RAG** for source-grounded answers
- [ ] Extend to **multi-language QA** (FR, DE, EN)
- [ ] Enable **PDF/Power BI export**
- [ ] Integrate with **ERP/Tax systems** as QA layer
- [ ] Include **semantic validation beyond keywords**

---

## 📌 Disclaimer

This is a **simulated, educational project** designed for portfolio presentation. Not intended for production use or legal compliance delivery.



