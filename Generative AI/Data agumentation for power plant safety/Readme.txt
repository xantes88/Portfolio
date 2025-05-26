# Image Classification Project with Synthetic Data Augmentation

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Dataset Description](#dataset-description)
- [Synthetic Image Generation and Dataset Augmentation](#synthetic-image-generation-and-dataset-augmentation)
- [Methodology](#methodology)
- [Solution Overview](#solution-overview)
- [Model Architecture](#model-architecture)
- [Training Procedure](#training-procedure)
- [Evaluation Metrics](#evaluation-metrics)
- [Results and Analysis](#results-and-analysis)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)


---

## Introduction

Image classification is a core task in computer vision where an algorithm assigns labels to images based on their visual content. It has applications across numerous domains, including medical imaging, autonomous driving, retail, and security. However, real-world datasets often suffer from **class imbalance** and **limited samples**, which degrade model performance, especially on minority classes.

This project focuses on addressing these challenges by leveraging **synthetic data augmentation** through AI-generated images. By augmenting the dataset with realistic synthetic samples, the model learns more generalized and discriminative features, leading to improved classification accuracy and robustness.

---

## Problem Statement

The main challenges addressed in this project are:

- **Class imbalance:** Some classes have significantly fewer samples, making it difficult for the model to learn representative features.
- **Limited dataset size:** A small number of training images limits the ability to train deep learning models effectively.
- **Generalization:** Models trained on imbalanced or small datasets tend to overfit majority classes, resulting in poor generalization on unseen data.
  
The goal is to improve classification accuracy across all 37 classes by:

- Generating synthetic images for underrepresented classes.
- Creating an augmented dataset combining original and synthetic images.
- Training and evaluating CNN classifiers on both original and augmented datasets to quantify performance improvements.

---

## Dataset Description

The dataset consists of approximately 1,100 images categorized into 37 classes. Each class corresponds to a distinct label relevant to the classification task. Key characteristics include:

- **Class distribution:** Highly imbalanced, with some classes containing fewer than 25 images and others exceeding 40.
- **Variability:** Images vary in background, lighting conditions, and object orientation, posing a challenge for robust classification.
- **Splitting:** Dataset split into training, validation, and test sets to ensure reliable performance evaluation.

---

## Synthetic Image Generation and Dataset Augmentation

To address the imbalance and limited data, synthetic images were generated using advanced generative models (e.g., GANs or diffusion models). These images:

- Mimic the visual style and key features of their respective classes.
- Increase the number of samples in minority classes to improve class balance.
- Enhance intra-class variability, aiding the model's generalization capabilities.

The augmented dataset is a union of original and synthetic images, significantly increasing the total number of training samples and providing a more uniform class distribution.

---

## Methodology

The project methodology follows these steps:

1. **Data preprocessing:**
   - Images were resized and normalized.
   - Data was split into training, validation, and test sets maintaining class distribution.

2. **Synthetic image generation:**
   - Generative models were trained or utilized to produce synthetic images.
   - Synthetic images were quality-checked to ensure class relevance and realism.

3. **Dataset augmentation:**
   - Synthetic images were combined with original images to form the augmented training dataset.

4. **Model training:**
   - Two CNN models were trained independently:
     - One on the original dataset.
     - One on the augmented dataset.
   - Consistent hyperparameters and training protocols were applied to ensure fair comparison.

5. **Model evaluation:**
   - Performance was assessed using accuracy, precision, recall, and F1-score metrics.
   - Detailed per-class analysis was conducted to evaluate improvements, especially in minority classes.

---

## Solution Overview

The approach integrates synthetic data augmentation with deep learning-based image classification to improve model robustness on an imbalanced multi-class dataset. The use of generative AI techniques provides a scalable way to enrich training data and reduce bias introduced by uneven class representation.

---

## Model Architecture

A Convolutional Neural Network (CNN) was employed featuring:

- Multiple convolutional layers with ReLU activation to extract hierarchical features.
- Max-pooling layers for spatial dimensionality reduction.
- Dropout layers to reduce overfitting.
- Fully connected layers leading to a softmax output layer for 37-class classification.

This architecture balances model complexity and computational efficiency, suitable for the dataset size and classification task.

---

## Training Procedure

- **Optimizer:** Adam optimizer with a learning rate tuned for stable convergence.
- **Batch size:** Fixed across experiments to ensure consistency.
- **Epochs:** Early stopping based on validation loss to avoid overfitting.
- **Loss function:** Categorical cross-entropy suitable for multi-class classification.

---

## Evaluation Metrics

- **Accuracy:** Overall percentage of correct predictions.
- **Precision:** Measures exactness — the proportion of true positives among predicted positives.
- **Recall:** Measures completeness — the proportion of true positives detected among all actual positives.
- **F1-score:** Harmonic mean of precision and recall, providing a balanced measure.

Metrics were computed both per class and as macro and weighted averages to understand performance distribution.

---

## Results and Analysis

### Performance on Augmented Dataset

- **Test Accuracy:** 72.55%
- **Macro Precision:** 75.89%
- **Macro Recall:** 72.02%
- **Macro F1-Score:** 71.86%

The inclusion of synthetic images notably improved model performance. Minority classes benefited the most, as the augmented data provided more representative samples, allowing the model to learn better features and reduce bias towards majority classes.

### Performance on Original Dataset

- **Test Accuracy:** 62.28%
- **Macro Precision:** 69.64%
- **Macro Recall:** 63.48%
- **Macro F1-Score:** 63.09%

Lower scores reflect the difficulty imposed by the original class imbalance and limited samples, resulting in weaker generalization and poorer performance on minority classes.

### Detailed Interpretation

- **Improved recall on minority classes:** Synthetic augmentation helped the model detect more true positives in underrepresented classes.
- **Balanced precision:** The model made fewer false positive errors across classes.
- **Overall robustness:** The model trained on augmented data is more stable and less prone to overfitting majority classes.

These results highlight the effectiveness of synthetic data augmentation for imbalanced image classification problems.

---

## How to Use

- Original and synthetic datasets are provided in structured folders.
- Users can train their own models or fine-tune the provided CNN architecture on either dataset.
- Evaluation scripts can be adapted to generate performance metrics on custom splits.

---

## Dependencies

- Python 3.8+
- PyTorch or TensorFlow
- scikit-learn
- numpy
- matplotlib (optional)
- pandas (optional)

