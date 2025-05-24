## Project Overview

This project aims to classify handwritten digits from the MNIST dataset using a pre-trained DenseNet121 convolutional neural network model. The core objective extends beyond classification accuracy: it focuses on interpreting and explaining the model's decisions using state-of-the-art Explainable AI (XAI) techniques, such as LIME and Integrated Gradients. These approaches provide insights into which parts of the input image influence the model’s prediction, promoting transparency, trust, and opportunities for model refinement.

---

## Dataset Description

- **Dataset:** MNIST (Modified National Institute of Standards and Technology)  
- **Content:** 70,000 grayscale images of handwritten digits (0-9), each of size 28x28 pixels.  
- **Split:**  
  - Training set: 60,000 images  
  - Test set: 10,000 images  
- **Labels:** Each image is labeled with the corresponding digit class (0 to 9).  
- **Challenge:** The dataset is widely used for benchmarking image classification models, offering a simple yet effective environment for evaluating classification and interpretability methods.

---

## Data Preprocessing

The MNIST images, originally single-channel grayscale, must be adapted for the DenseNet121 model, pre-trained on RGB ImageNet images.

1. **Channel Conversion:**  
   Grayscale images (1 channel) are converted to RGB by duplicating the grayscale channel into 3 channels to meet the input format expected by DenseNet121.

2. **Resizing:**  
   Images are resized from 28x28 to 224x224 pixels using bilinear interpolation to comply with DenseNet121 input requirements.

3. **Normalization:**  
   Images are normalized using ImageNet’s mean and standard deviation values per channel, matching the normalization used during the DenseNet121 pre-training phase. This ensures consistent input scaling and better transfer learning performance.

---

## Model Architecture and Training

- **Base Model:** DenseNet121, a densely connected convolutional neural network known for efficient feature reuse and strong performance on image classification tasks.  
- **Pre-training:** The model is initialized with weights pre-trained on ImageNet.  
- **Fine-tuning:** The final classification layer is adjusted to output 10 classes corresponding to digits 0–9, and the model is fine-tuned on the MNIST training set.  
- **Loss Function:** Cross-entropy loss for multi-class classification.  
- **Optimizer:** Adam or SGD with appropriate learning rate scheduling.  
- **Training Metrics:** Accuracy on training and test sets, loss convergence.

---

## Explainability Techniques

### LIME (Local Interpretable Model-agnostic Explanations)

- **Goal:** Explain individual model predictions by approximating the model locally with interpretable, linear models.  
- **Process:**  
  - Select an input image (e.g., a digit 4 or 5).  
  - Perturb the image by randomly masking segments (superpixels).  
  - Observe the effect of perturbations on the prediction probability.  
  - Fit a weighted linear model to approximate the black-box model behavior around that input.  
- **Output:** A heatmap highlighting which parts of the image contributed most to the model’s prediction.  
- **Findings:**  
  - For correctly classified digits, LIME focuses on the digit strokes and ignores background noise.  
  - For misclassified images, LIME reveals the model’s sensitivity to irrelevant regions, explaining prediction errors.

### Integrated Gradients

- **Goal:** Attribute the model's prediction to its input features by integrating gradients along a path from a baseline (black) image to the actual input.  
- **Process:**  
  - Choose a baseline image (typically all zeros).  
  - Compute gradients of the output w.r.t. the input, integrated over a sequence of interpolated inputs between baseline and input.  
- **Output:** Attribution maps that highlight pixel importance for the predicted class.  
- **Findings:**  
  - Attribution maps emphasize critical digit features such as loops, edges, and corners.  
  - Attributions are smooth and continuous, providing an intuitive explanation.  
  - In incorrect predictions, attributions scatter over irrelevant areas, indicating model confusion.

---

## Results and Analysis

### Classification Performance

- The fine-tuned DenseNet121 achieves high accuracy (>98%) on the MNIST test set, confirming its suitability for digit recognition.

### Explainability Insights

- **Correct Predictions:**  
  - Both LIME and Integrated Gradients highlight meaningful digit features consistent with human interpretation (e.g., closed loops in 6, straight strokes in 1).  
  - The model relies primarily on relevant pixels, demonstrating robustness to noise.

- **Incorrect Predictions:**  
  - Saliency maps show dispersed or misplaced focus, explaining why the model errs.  
  - LIME perturbation reveals which pixel regions cause the model to change its prediction, informing possible areas for data augmentation or model tuning.

- **Comparison:**  
  - LIME provides local, interpretable explanations by simplifying the model behavior near specific inputs.  
  - Integrated Gradients offers a gradient-based attribution approach that captures feature importance in a more continuous manner.

---

## Considerations for a Fully Explainable System

To enhance explainability, future development could include:

1. **Transparency in Preprocessing:**  
   - Explicit visualization and explanation of image conversion and resizing impacts on predictions.

2. **Intermediate Feature Explanations:**  
   - Use Layer-wise Relevance Propagation (LRP) or Grad-CAM to visualize internal feature activations and identify which learned features influence the decision.

3. **Interactive User Feedback:**  
   - Allow users to modify image regions and observe real-time prediction changes, fostering deeper understanding of model sensitivity.

4. **Error Analysis & Suggestions:**  
   - When predictions fail, provide detailed attribution maps and suggest potential corrective actions (e.g., highlight ambiguous digit shapes).

5. **Natural Language Summaries:**  
   - Generate accessible explanations summarizing model decisions for non-expert users.

---

## Future Improvements and Extensions

- **Global Explanation Techniques:**  
  - Implement Grad-CAM and Class Activation Mapping (CAM) for class-level attention visualization.  
  - Use t-SNE or UMAP to analyze class distributions in feature space.  
  - Generate adversarial examples to test model robustness and boundary clarity.

- **Model Optimization:**  
  - Perform hyperparameter tuning (learning rate, batch size, dropout).  
  - Fine-tune deeper layers of DenseNet121 for better feature adaptation to MNIST.

- **Real-Time Monitoring:**  
  - Develop systems to monitor interpretability metrics dynamically during training for early insight.

- **Extend Dataset Scope:**  
  - Apply the methodology to more complex handwritten character datasets (e.g., EMNIST, Fashion-MNIST).

