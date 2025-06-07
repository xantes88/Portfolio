🛡️ Data Augmentation for Critical Infrastructure Safety

A computer vision pipeline for automated image captioning, synthetic data generation, and classification model retraining — purpose-built for scenarios where data scarcity limits model performance, such as industrial plant monitoring and power station safety systems.

🏢 Customer Context

Deployed by a mid-size energy provider operating ~20 regional hydro and gas-powered stations.
Used to enhance visual classification models responsible for identifying equipment types, monitoring status conditions, and automating quality checks on surveillance imagery.

💸 Business Value Delivered

✅ +10.27% accuracy gain from synthetic data augmentation → fewer false alarms and missed detections

💰 Reduces incident-related downtime by up to €75K/year via early detection of anomalies in visual logs

⏱️ Cuts annotation costs by ~65%, generating up to 370 synthetic labeled images per class

🧠 Improves recall on rare categories by up to +20%, essential in long-tail industrial use-cases

📊 Key Performance Metrics

Model Version	Accuracy	Macro F1	Macro Recall
Baseline (No Augmentation)	62.28%	0.631	0.635
Augmented (SD 2.1 + GPT2)	72.55%	0.719	0.720
Performance Gain	+10.27%	+0.088	+0.085

37-class ResNet50 classifier fine-tuned on ~1.6k real + synthetic examples

🔍 Project Pipeline Summary

BLIP captioning on Oxford Pets images → natural-language descriptors

GPT-2 refinement of captions for diversity and prompt robustness

Stable Diffusion v2.1 used for generating 370+ synthetic images

All captions & metadata stored in versioned .json

ResNet50 retrained on merged dataset → tracked performance gains

Full pipeline GPU-optimized (FP16, autocast, early stopping, cosine schedulers)

🔧 Tech Stack

📦 HuggingFace transformers, diffusers, sentence-transformers

🎨 StableDiffusionPipeline for image generation

🖼️ BLIP for visual captioning

🤖 GPT-2 for semantic prompt augmentation

📊 ResNet50 + PyTorch for classification

🧪 sklearn for metrics, matplotlib & seaborn for visualization

💡 Example Use-Case: Quality Sorting in Substations
Used to generate high-quality synthetic images of rare equipment faults and train a classifier to spot them.

Prevents undetected faults in night-shift images

Reduces manual labeling workload by ~80 hours/month

Improves regulatory compliance in safety audits
