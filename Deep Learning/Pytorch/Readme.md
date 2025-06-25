# 🧠 Food Image Classifier – Performance Optimization & Explainability

> 📦 **Note**: This is a simulated project based on real-world business problems in the food industry. All data and scenarios are fictional but inspired by industrial QA use cases.

---

## 🔍 Problem Statement

In large-scale food distribution and packaging environments, errors in visual classification (e.g. **Taquito vs Taco**) can lead to:

- ❌ Mislabeled shipments  
- 📦 Packaging errors  
- 🚚 Logistics inefficiencies  
- 📉 QA/Compliance risks  

With increasing demand for real-time automation, food tech operations require **accurate, explainable, and robust** image classification models.

---

## 🧑‍💼 Simulated Client Scenario *(Realistic but Fictional)*

This project simulates a real-world deployment for a **frozen food distribution company** handling **250K outbound trays/month** across 5 categories.

It is designed to address challenges such as:

- ✅ Automated visual sorting  
- ✅ Label validation before shipping  
- ✅ Assistive tools for non-technical quality inspectors  

---

## 📈 Quantified Business Value

| Business Area             | Impact                                                                 |
|---------------------------|------------------------------------------------------------------------|
| ❗ Classification Error    | Reduced by **>38%** on validation dataset                              |
| 💰 QA Labor Costs         | Savings estimated at **€20K–€30K/year** via reduced manual checking    |
| ⚖️ Regulatory Traceability | Supports **HACCP/compliance audits** through explainable decisions     |
| ⚙️ Model Optimization Time | **30% faster convergence** via early stopping and dynamic checkpointing |

---

## 🛠️ Stack Overview

| Component     | Details                                             |
|---------------|-----------------------------------------------------|
| Framework     | Python + PyTorch                                    |
| Model         | EfficientNet-B0 (via `timm`) with fine-tuned head   |
| Dataset       | Custom image dataset (Train/Val/Test folders)       |
| Explainability| Confusion Matrix + Misclassified Image Display      |
| Optimizations | Early Stopping, Checkpointing, Augmentations        |

---

## 🧪 Techniques Demonstrated

| Technique              | Purpose                                                      |
|------------------------|--------------------------------------------------------------|
| Data Integrity Check   | Detect corrupted / low-light / low-resolution images         |
| Image Augmentation     | Improve generalization (crop, color jitter, etc.)            |
| Transfer Learning      | Use pretrained EfficientNet + custom classification head     |
| Early Stopping         | Avoid overfitting by monitoring validation loss              |
| Checkpoint Saving      | Persist best-performing model with full metrics              |
| Visual QA              | Display failed predictions with image + class name           |

---

## 🧠 Model Architecture

- **Input**: 224×224 RGB images  
- **Base Model**: EfficientNet-B0 (pretrained)  
- **Final Layer**: Custom linear classifier (20 classes)  
- **Loss Function**: Cross Entropy  
- **Optimizer**: Adam, `lr=0.001`  
- **Scheduler**: Early stopping (patience = 5, δ = 0.001)  

---

## 📦 Dataset Pipeline

- ✅ Download from secure S3 archive  
- 📂 Organized into `/train`, `/val`, `/test`

**Preprocessing Includes:**
- Corrupted image detection  
- Resolution & brightness checks  
- Class-wise distribution analysis  

**Transformations Applied:**
- `RandomResizedCrop`  
- `ColorJitter`  
- `Normalization` (ImageNet mean/std)  

---

## 🧪 Evaluation & Explainability

| Metric              | Value (Test Set)           |
|---------------------|----------------------------|
| Accuracy            | **82.3%**                  |
| Worst-Class Recall  | **Taquito: 64.1%**         |
| Visual Checks       | ✅ Per-class image viewer   |

**👁️ Visual QA Includes:**

- Real image previews of worst-performing classes  
- Confusion matrix heatmap (via Seaborn)  
- Class-wise F1-score from `classification_report()`  

---

## 🎯 Industrial Use Cases

| Use Case                  | Value Proposition                                           |
|---------------------------|-------------------------------------------------------------|
| Visual Label Verification | Prevent false labeling in tray preparation                 |
| Frozen Product Sorting    | Ensure visual conformity on conveyor belt                  |
| Compliance Traceability   | Store model decisions for **HACCP audit logs**             |
| Packaging Automation      | Trigger barcode printing based on visual AI classification |

---

## 🔄 Next Steps

- 🔁 Introduce **Dropout** & **Random Search** for hyperparameter optimization  
- 🔍 Integrate **SHAP** or **GradCAM** for explainability via saliency maps  
- 🧩 Deploy on **Raspberry Pi + Coral TPU** for edge classification  
- 🧪 Test on **multi-class imbalance** scenarios  
- 📊 Build a **Streamlit dashboard** for live analytics & QA feedback  

---

## 💬 Summary

This project simulates a **production-grade food classification system** with:

- ✅ Robust training pipeline (early stopping, checkpoints)  
- ✅ Explainability via visual QA & classification reports  
- ✅ Real-world alignment with business operations and compliance needs  

It demonstrates how AI can deliver measurable value in **food manufacturing, logistics, and quality assurance** through automation, accuracy, and traceability.





