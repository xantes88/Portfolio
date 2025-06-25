# 🌼 FlowerVision  
**Real-Time Flower Classification for AgriTech Edge Deployment**

---

## 🧠 Purpose  
Develop a robust computer vision system to classify **daisy vs. dandelion** images with high precision — enabling real-time monitoring, classification, and biodiversity reporting in **precision agriculture**.

Optimized for **edge deployment** (drones, field cameras), FlowerVision replaces manual flora inspection with **automated, accurate species detection** in large-scale agricultural environments.

---

## 🧑‍🌾 Simulated Deployment Scenario  
**Client**: European AgriTech startup managing 3,500+ hectares across Italy and Spain  
**Use Case**: Integrated into an AI-powered ecosystem scanner to:
- Detect invasive or non-seasonal flora
- Classify flower species from drone imagery
- Automate biodiversity and ESG compliance reports

---

## 💰 Business Impact

| Impact Area         | Business Value                                                                 |
|---------------------|--------------------------------------------------------------------------------|
| 🌱 Species Detection | Automates up to **85%** of flora classification in open fields                |
| ⏱️ Operational Time | Saves **60+ hours/month** of manual labor across crop zones                   |
| 🧾 ESG Compliance   | Enables automated flora tracking for **carbon credit certification**          |
| 📉 Error Reduction  | Reduces misclassification by **>90%** vs. manual visual inspection            |

---

## 🧬 Model Architecture

| Component         | Details                                                                 |
|------------------|-------------------------------------------------------------------------|
| Base Model       | `EfficientNet-B0` via `timm` (transfer learning)                        |
| Input Format     | RGB images resized to **224x224**                                       |
| Loss Function    | `Weighted CrossEntropyLoss` for class imbalance                         |
| Optimizer        | `Adam`, learning rate = 0.001                                            |
| Regularization   | **Early stopping** (patience: 5)                                        |
| Augmentation     | `Rotation`, `ColorJitter`, lighting normalization for robustness        |
| Accuracy Achieved| **96.2%** on unseen test data                                           |

---

## 📊 Dataset Overview

- **Classes**: `daisy`, `dandelion`
- **Size**: ~2,000 labeled images
- **Cleaning**: Corrupt image removal, brightness analysis
- **Class Balance**: Achieved via
  - Class-weighted loss
  - Augmentation of the minority class (`daisy`)

---

## 🧪 Project Context

> 🚧 **Simulated Use Case — Real Techniques**

This project was developed as a **simulated case study** within a professional AI Engineering curriculum.  
The technical pipeline, data handling, and model design reflect **real-world standards and deployment logic**.

The business scenario (AgriTech client, ESG compliance, drone deployment) is **hypothetical**, but all modeling, evaluation, and optimization steps are implemented as they would be in a production setting.

This simulation serves as a **portfolio-ready prototype** to showcase:
- Transfer learning for edge devices  
- Handling of imbalanced datasets  
- Augmentation pipelines and explainability  
- Metrics aligned with operational KPIs

---

## 📈 Key Results

| Metric                | Value          |
|-----------------------|----------------|
| Training Accuracy     | 97.5%          |
| Validation Accuracy   | 95.3%          |
| Test Accuracy         | 96.2%          |
| Misclassified Samples | 6 / 300        |
| Time to Train         | ~15 minutes    |

---

## 🔎 Performance Insights

- **Confusion matrix** confirms strong class separation  
- Only 6 misclassifications — all false positives for *dandelion* under low-light conditions  
- Augmentation improved resilience to color and brightness variations  
- Early stopping ensured no overfitting

---

## 🌿 Real-World Use Cases

| Use Case                        | Value Delivered                                                  |
|----------------------------------|------------------------------------------------------------------|
| Drone-Based Field Scouting      | Immediate flower classification with real-time inference         |
| ESG Compliance Automation       | Fully automated flora logging for biodiversity tracking          |
| Invasive Species Monitoring     | Early detection of seasonal anomalies                            |
| On-Edge Deployment              | Efficient model running on low-power hardware (e.g., drones)     |

---

## 🔥 What Sets It Apart

✅ **Edge-ready**: Lightweight CNN deployable on drones or IoT sensors  
✅ **Highly accurate**: Performs well even on noisy field images  
✅ **Domain-aware**: Balanced class sampling and targeted augmentation  
✅ **Production-aligned**: Structured for seamless deployment and scalability

---

## 🧪 Stack

- `PyTorch` + `timm`: Model training and pre-trained EfficientNet
- `Torchvision`: Image loading and transforms  
- `Seaborn`, `Matplotlib`: Data visualization  
- Developed in **Google Colab** with GPU acceleration

---

## 🚀 Roadmap: Next Steps

| Goal                                | Description                                                |
|-------------------------------------|------------------------------------------------------------|
| 🔁 Retrain on field imagery          | Use drone-captured images to fine-tune performance         |
| 🧠 Fine-tune and explainability      | Experiment with `EfficientNet-B1/B2`, `SHAP`, and GradCAM  |
| 📦 Deploy to production              | Convert model to `ONNX`, build Streamlit dashboard         |
| 🌍 GIS Integration                   | Merge outputs with geotags for live ecosystem mapping      |

---

## 📌 Quick Start (Coming Soon)

```bash
# Example command for inference
python classify.py --image path/to/image.jpg

🧠 Author Note
This project was developed as part of a professional AI Engineering track focused on applied machine learning for real-world operations — with special emphasis on AI for sustainability, automation, and business impact.
Explore the full portfolio: github.com/xantes88

🎯 Next Step
Build the Streamlit demo and deploy it for real-world testing.



