🌼 Flower Recognition with EfficientNet for AgriTech Applications

This project focuses on building a high-performance deep learning model capable of distinguishing between Daisy and Dandelion flowers using real-world image data. The goal is to enable scalable, automated image recognition for environmental monitoring, precision agriculture, and biodiversity tracking.

🚀 Project Overview

Use case: Flower species classification in natural environments

Model: Transfer learning with EfficientNet-B0

Data: Custom dataset with Daisy and Dandelion images

Key focus: Class imbalance handling, data augmentation, training optimization

Accuracy achieved: ~96% on test set

🧠 Core Technologies

Component	Tool / Library
Framework	PyTorch
Model	EfficientNet-B0 (timm)
Data Handling	torchvision, PIL, OpenCV
Evaluation	sklearn, seaborn
Augmentation	torchvision transforms

📁 Dataset Structure

/progetto-finale-flowes/
├── train/
│   ├── daisy/
│   └── dandelion/
├── valid/
├── test/
Each class contains JPEG/PNG flower images

Resolution: Most images are high quality (~512x512)

Class imbalance observed: dandelion is overrepresented

🔍 Preprocessing & Augmentation

Image Cleaning: Removed corrupted and low-quality images

Resize: All images scaled to 224x224

Normalization: Based on ImageNet stats

Data Augmentation:

Rotation, color jitter for Daisy

No augmentation for Dandelion

Brightness & Resolution Checks:

Low-brightness images flagged

Resolution < 128x128 marked for review

⚖️ Addressing Class Imbalance

Class	Sample Count	Strategy
Daisy	Fewer	Augmentation, weighting
Dandelion	More	Baseline normalization

Used WeightedCrossEntropyLoss to emphasize underrepresented class

Created a balanced training set using Subset and ConcatDataset

🏗️ Model Architecture

Backbone: EfficientNet-B0 (pretrained)

Final Layer: Replaced classifier for 2-class output

Loss Function: Weighted CrossEntropyLoss

Optimizer: Adam (lr=0.001)

Early Stopping: Triggered after 5 stagnant epochs

Checkpoints: Saved best validation model (best_model.pth)

📊 Performance Summary

Metric	Value
Validation Accuracy	~95%
Test Accuracy	96%
Daisy Precision	0.96
Dandelion Precision	0.97
Total Misclassifications	6

Confusion matrix reveals most errors are from misclassifying Daisy as Dandelion – a sign of remaining class imbalance bias.

🖼️ Visual Outputs

📉 Training/validation loss & accuracy charts

🧾 Classification report

🔍 Confusion matrix heatmap

🔍 Per-class count stats

💡 Business Applications
🌿 Environmental Monitoring: Detect floral species across regions

🧑‍🌾 AgriTech: Automate flora recognition in precision farming

🏞️ Biodiversity: Support ecological surveys with image-based classification

🛰️ Remote Sensing: Integrate with drone imagery pipelines

🛠️ Future Enhancements

🧪 Add fine-tuning with learning rate schedulers

🔁 Test ensemble models for robustness

🧭 Expand dataset to include more flower types

🧱 Add explainability (e.g., GradCAM)

⚖️ Further reduce bias using SMOTE or GAN augmentation

📌 Conclusion
This project showcases a complete deep learning pipeline:

Clean dataset ➝ Explore ➝ Augment ➝ Train ➝ Evaluate

Tackles real-world data imbalance, preprocessing, and model optimization challenges

Yields production-ready accuracy with EfficientNet's lightweight power

Ideal for scaling into mobile, web, or cloud-based AgriTech solutions.
