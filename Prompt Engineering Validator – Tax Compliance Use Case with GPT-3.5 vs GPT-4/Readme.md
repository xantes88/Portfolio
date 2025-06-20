# 🤖 Prompt Evaluation System for Business Use Cases (GPT-3.5 vs GPT-4)

_A simulated AI project benchmarking GPT-3.5 and GPT-4 for tax compliance prompt evaluation with automated relevance scoring._

---

## 🧠 Executive Summary

Many companies face challenges validating the quality and business relevance of LLM-generated content in complex regulatory workflows.  
This project simulates how a Prompt Engineer can design, test, and automatically evaluate AI outputs for **accuracy, compliance, and keyword relevance** in the domain of Italian VAT obligations for SRLs (limited liability companies).

We implemented a dual-model evaluation pipeline using GPT-3.5-turbo and GPT-4, enriched by a tailored keyword matching algorithm and output diagnostics, to objectively measure content quality.

> 📌 **Disclaimer**: This is a personal, simulated project for educational and portfolio use. It is not affiliated with any real client or production environment.

---

## 💼 Business Context & Problem Statement

- **Industry**: Finance / Tax Compliance  
- **Problem**: Manual tax compliance processes are time-consuming, error-prone, and lack automation.  
- **Opportunity**: Leverage Large Language Models to dynamically generate compliant, accurate, and structured guidance for tax obligations.  
- **Solution**: An automated prompt evaluation system to compare LLM outputs, validate content relevance, and optimize prompt engineering workflows.

---

## ⚙️ Project Features

- Dual model inference: GPT-3.5-turbo and GPT-4  
- Business-critical keyword-based automated output scoring  
- Detailed output diagnostics: word count, keyword match score, relevance status  
- Robust error handling and fallback for GPT-4 access limitations  
- Clear separation of prompt design, model inference, and evaluation logic

---

## 🧪 Prompt Used

> You are an Italian tax expert. Briefly list the main VAT obligations for an SRL (limited liability company) under the standard tax regime in 2024. Reply with 5 concise bullet points.

---

## 📥 Real Model Outputs & Evaluation

### 🔹 GPT-3.5-Turbo Output

Charging VAT on sales of goods or services at the standard rate of 22%.

Issuing invoices that comply with the Italian VAT regulations.

Submitting periodic VAT returns (usually monthly or quarterly).

Keeping proper VAT records and documentation for at least 10 years.

Complying with Intrastat reporting requirements for intra-EU trade.

**Evaluation:**  
- Word count: 55  
- Keyword match: 2/5  
- Relevance: ❌ Low  

---

### 🔷 GPT-4 Output

VAT Registration: The SRL must be registered for VAT (Value Added Tax) with the Italian Revenue Agency. This includes obtaining a VAT number which must be used in all tax-related transactions.

VAT Reporting: The company must prepare and submit periodic VAT returns (monthly, quarterly, or annually depending on the company's turnover) to the Italian tax authorities, detailing all taxable transactions carried out during the period.

VAT Payment: The SRL is obliged to calculate and pay the net VAT due (output VAT minus input VAT) on a regular basis - usually monthly or quarterly. If the input VAT is higher than the output VAT, the company can carry the excess forward to the next period or request a refund.

Issuance of VAT Invoices: For each sale of goods or services, the company must issue a VAT invoice to the buyer, showing the amount of VAT charged. The invoice must comply with the requirements of the Italian VAT law.

Record Keeping: The company must keep detailed records of all taxable transactions for a period of 10 years. This includes sales and purchase invoices, VAT returns, and any other documents related to VAT. These records must be available for inspection by the tax authorities at any time.


**Evaluation:**  
- Word count: 209  
- Keyword match: 3/5  
- Relevance: ✅ Sufficient  

---

## 📊 Impact Simulation & KPIs

| Metric                         | Manual Process | LLM-Augmented Process |
|-------------------------------|----------------|-----------------------|
| Average Response Time          | 20–30 minutes  | < 30 seconds          |
| Manual Review Effort           | High           | Medium–Low            |
| Accuracy on Business Keywords  | N/A            | 90%+                  |
| Content Validation Speed       | N/A            | 10× Faster            |

*Simulated results demonstrating the potential operational efficiency improvements in tax advisory workflows.*

---

## 🚀 How to Run

1. Clone this repository.  
2. Install the required Python package:  
```bash

pip install openai==0.28

Run the prompt evaluation script or open the Colab notebook.

Enter your OpenAI API key securely when prompted.

Review the generated outputs and automatic relevance scores.

📘 Tech Stack
Python 3.11+

OpenAI API (GPT-3.5 and GPT-4)

Prompt engineering best practices

Keyword-based automated scoring

Compatible with Google Colab and Jupyter Notebooks

📢 Closing Statement

🧠 Built on a solid foundation of SAP Finance operations experience, now driving AI-powered business automation to unlock new efficiency and innovation.
If you’re looking for a professional who can bridge traditional finance with cutting-edge LLM solutions to transform compliance and operational workflows, let’s connect and create real impact together.

