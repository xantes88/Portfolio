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

- Charging VAT on sales of goods or services at the standard rate of 22%.  
- Issuing invoices that comply with the Italian VAT regulations.  
- Submitting periodic VAT returns (usually monthly or quarterly).  
- Keeping proper VAT records and documentation for at least 10 years.  
- Complying with Intrastat reporting requirements for intra-EU trade.

**Evaluation:**  
- Word count: 55  
- Keyword match: 2/5  
- Relevance: ❌ Low  

---

### 🔷 GPT-4 Output

1. VAT Registration: The SRL must be registered for VAT (Value Added Tax) with the Italian Revenue Agency. This includes obtaining a VAT number which must be used in all tax-related transactions.

2. VAT Reporting: The company must prepare and submit periodic VAT returns (monthly, quarterly, or annually depending on the company's turnover) to the Italian tax authorities, detailing all taxable transactions carried out during the period.

3. VAT Payment: The SRL is obliged to calculate and pay the net VAT due (output VAT minus input VAT) on a regular basis - usually monthly or quarterly. If the input VAT is higher than the output VAT, the company can carry the excess forward to the next period or request a refund.

4. Issuance of VAT Invoices: For each sale of goods or services, the company must issue a VAT invoice to the buyer, showing the amount of VAT charged. The invoice must comply with the requirements of the Italian VAT law.

5. Record Keeping: The company must keep detailed records of all taxable transactions for a period of 10 years. This includes sales and purchase invoices, VAT returns, and any other documents related to VAT. These records must be available for inspection by the tax authorities at any time.

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

## 🌟 Expanded Use Cases & Future Developments

### Expanded Use Cases

This prompt evaluation framework can be extended beyond Italian VAT compliance to various domains where accuracy, compliance, and relevancy of LLM outputs are critical, such as:

- **Financial Reporting & Forecasting:** Automating the generation and validation of financial summaries and forecasts to assist CFOs and finance teams.  
- **Legal Document Analysis:** Supporting contract review and legal compliance checks by assessing the relevance and completeness of AI-generated summaries or clauses.  
- **Regulatory Risk Management:** Continuously evaluating AI outputs for adherence to industry regulations in sectors like banking, healthcare, and insurance.  
- **Customer Support Automation:** Ensuring chatbot or virtual assistant responses align with company policies and provide accurate, compliant information.  
- **Training & Onboarding:** Using prompt evaluation to build reliable AI tutors that provide consistent, accurate training materials in complex subjects.

### Potential Future Developments

- **Multi-language Support:** Extending prompt evaluation to support multiple languages, broadening applicability across global markets.  
- **Advanced Semantic Scoring:** Integrating NLP techniques like semantic similarity and entailment checks to complement keyword matching.  
- **User Interface Development:** Building an interactive dashboard for non-technical users to submit prompts, view outputs, and get automatic evaluations.  
- **Continuous Learning Pipelines:** Creating feedback loops where user validation improves prompt design and model selection over time.  
- **Integration with Enterprise Systems:** Connecting this framework with ERP or compliance software (e.g., SAP, Oracle) for end-to-end automation.  
- **Explainability Modules:** Adding explainable AI components to highlight why certain outputs scored higher or lower, increasing trust and auditability.

---

## 🔗 Related Projects

- **Advanced Analytics for Invoice Payment Risk**  
  [GitHub Repository](https://github.com/xantes88/Portfolio/tree/main/Progetti%20Machine%20Learning/Advanced%20Analytics%20for%20Invoice%20Payment%20Risk)  
  A machine learning project forecasting invoice payment delays to optimize cash flow and reduce operational risks.

- **Explainable AI for Banking Compliance**  
  [GitHub Repository](https://github.com/xantes88/Portfolio/tree/main/Explainable%20AI)  
  Implementation of explainable neural networks to increase transparency and trustworthiness of AI decisions in financial regulation.

- **Generative AI - Data Augmentation for Power Plant Safety**  
  [GitHub Repository](https://github.com/xantes88/Portfolio/tree/main/Generative%20AI/Data%20agumentation%20for%20power%20plant%20safety)  
  Synthetic data generation pipeline improving classification accuracy in industrial safety monitoring using generative models.

---

## 🚀 How to Run

1. Clone this repository.  
2. Install the required Python package:
3. pip install openai==0.28
4. Run the prompt evaluation script or open the Colab notebook.
5. Enter your OpenAI API key securely when prompted.
6. Review the generated outputs and automatic relevance scores.

```bash

📘 Tech Stack

Python 3.11+

OpenAI API (GPT-3.5 and GPT-4)

Prompt engineering best practices

Keyword-based automated scoring

Compatible with Google Colab and Jupyter Notebooks

📢 Closing Statement

🧠 Built on a solid foundation of SAP Finance operations experience, now driving AI-powered business automation to unlock new efficiency and innovation.

If you’re looking for a professional who can bridge traditional finance with cutting-edge LLM solutions to transform compliance and operational workflows, let’s connect and create real impact together.
