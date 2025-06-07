🧠 Interpretable Neural Network for Regulatory Compliance in Banking

This project explores how explainable AI (XAI) techniques can be integrated with neural networks to create transparent, trustworthy systems for highly regulated domains such as banking and finance. By training a CNN on the MNIST dataset and applying a suite of interpretability tools, we simulate a compliance-focused model audit pipeline.

🔍 Objective

To build a visual and interactive pipeline that:

Trains a convolutional neural network on digit classification

Applies LIME, Integrated Gradients, Occlusion, and Grad-CAM

Provides human-interpretable insights into model decisions

Demonstrates how interpretability can support compliance and model auditing

🧠 Technologies Used

Category	Tools & Libraries
Framework	PyTorch, Torchvision
Explainability	Captum, LIME, TorchCAM, Grad-CAM
Visualization	Matplotlib, NumPy
Dataset	MNIST (converted to RGB for CNNs)
Model	Custom CNN + DenseNet121 (pretrained)

💡 Why This Project Matters

✅ Business Value
Regulatory Readiness
Simulates how models can be audited in finance (e.g. credit scoring, fraud detection) using explainability techniques aligned with GDPR, ECB, and EU AI Act.

Model Transparency
LIME and Integrated Gradients allow analysts and auditors to verify if models are focusing on relevant input features, improving trust and accountability.

Explainability Skills
Demonstrates deep understanding of black-box model interpretation — increasingly in demand across regulated industries.

📁 Project Structure
├── data/
│   └── MNIST RGB formatted
├── models/
│   └── trained_classifier.pth
├── notebooks/
│   └── interpretability_pipeline.ipynb
├── utils/
│   └── visualization_helpers.py
├── explainability/
│   └── gradcam_output/
│   └── lime_heatmaps/
│   └── integrated_gradients/
└── README.md
🧪 Methodology Overview

1. Preprocessing

Convert MNIST grayscale images to RGB

Resize to 224×224 for compatibility with pretrained DenseNet

2. Training
Train both a custom CNN and a transfer learning model (DenseNet121)

Evaluate performance on test set

3. Explainability

Technique	Purpose

Integrated Gradients	Attribute pixel importance per class

LIME	Perturb local pixels, visualize decision

Grad-CAM / TorchCAM	Visualize CNN attention maps

Occlusion	Test robustness to input masking

📊 Results

🔥 High interpretability of predictions on digits 0–9

💬 Clear explanation maps for correct and incorrect predictions

🧠 Local and global insights into what features drive decisions

🧩 Modular pipeline that supports rapid compliance testing

🔄 Next Steps
✅ Add SHAP for global feature importance

✅ Visualize decision boundaries with t-SNE

🔄 Integrate Streamlit for real-time interactive model audit

🔄 Use adversarial examples to test explanation stability

🏁 Conclusion
This project provides a transparent and reproducible explainability pipeline for neural network interpretability. It highlights how data scientists and ML engineers can build responsible AI systems — especially critical in banking, insurance, healthcare, and other compliance-heavy industries.
