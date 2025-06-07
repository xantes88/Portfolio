⚡ Data Augmentation for Power Plant Security using Image Captioning & Stable Diffusion
This project explores the application of advanced data augmentation techniques using image captioning (BLIP) and image generation (Stable Diffusion 2.1) to improve classification accuracy in scenarios involving critical infrastructure security, such as power plants.

🔍 Objective
To enhance the model's ability to accurately classify different categories (e.g., pet breeds as a proxy dataset) by generating high-quality synthetic images and captions — simulating edge-case scenarios relevant to security in power systems.

🧠 Key Technologies
Image Captioning: BLIP for extracting contextual captions from images.

Text Generation: GPT-2 for refining and expanding image captions.

Image Generation: Stable Diffusion 2.1 for generating new synthetic images based on descriptive prompts.

Model Training: Fine-tuned ResNet50 for multi-class image classification.

Evaluation: Precision, recall, F1-score, confusion matrix, and test accuracy.

📊 Results
Dataset Version	Test Accuracy	Macro F1 Score
Original Dataset	62.28%	0.631
With Augmented Images	72.55%	0.719

📈 +10.27% accuracy improvement using synthetic images

🔄 Boosted performance on under-represented categories

🧪 Enhanced generalization to unseen data

🛠️ How It Works
Caption Extraction: Contextual captions are generated from real images using BLIP.

Prompt Enrichment: Captions are semantically expanded using GPT-2.

Image Generation: Stable Diffusion generates new, high-quality images from refined prompts.

Data Integration: Synthetic images and captions are merged into the original dataset.

Training & Evaluation: A ResNet50 classifier is trained and evaluated on the enriched dataset.

✅ Business Value
Reduced Labeling Costs: This technique can reduce reliance on manual annotation by synthesizing labeled data at scale.

Improved Model Robustness: Demonstrates how synthetic data can mitigate class imbalance and improve generalization — essential in real-world, high-risk environments like energy or defense.

Scalable & Repeatable: The architecture supports retraining with new classes, making it adaptable for new threat types, equipment anomalies, or surveillance contexts.

Real-World Analog: While trained on the Oxford-IIIT Pet dataset, this approach is directly transferable to domains like security camera feeds, drone imagery, and industrial inspections.

🔄 Potential Improvements
Domain-Specific Dataset: Replace pet images with actual security footage or power infrastructure datasets.

Human-in-the-loop Feedback: Introduce manual validation to ensure synthetic data quality.

Multimodal Risk Assessment: Extend the pipeline with text-to-text reasoning or audio-video inputs.

Model Monitoring: Integrate explainability tools (e.g., Grad-CAM) to monitor and debug decisions made by the trained model.

Edge Deployment: Optimize the model for real-time inference on edge devices used in industrial sites.

📁 Repository Structure

├── data/
│   └── original_images/
│   └── generated_images/
├── notebooks/
│   └── data_augmentation.ipynb
├── models/
│   └── resnet50_trained.pth
├── utils/
│   └── image_captioning.py
├── captions_dataset_blip.json
├── augmented_captions_dataset.json
└── README.md
💬 Why This Project Matters
This project demonstrates a full-stack machine learning pipeline from raw data ingestion to performance uplift via synthetic augmentation. It showcases:

🔍 Smart use of transformers and generative AI to solve data scarcity.

🎯 Real-world potential in security, infrastructure, and automation domains.

🛠️ Competence in vision-language integration, data engineering, and MLOps readiness.
