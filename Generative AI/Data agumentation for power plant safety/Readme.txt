Image Classification Project with Synthetic Data Augmentation
Table of Contents
Introduction

Problem Statement

Dataset Description

Synthetic Image Generation and Dataset Augmentation

Methodology

Model Architecture

Training Procedure

Evaluation Metrics

Results and Analysis

How to Use

Dependencies

Introduction
In real-world image classification tasks, datasets often suffer from class imbalance and limited sample sizes, leading to biased models that perform poorly on minority classes. This project addresses these challenges by leveraging synthetic data augmentation to balance class distributions and enrich the training data. By generating AI-synthesized images, this project demonstrates how synthetic data can improve model robustness and classification performance across all classes.

Problem Statement
The project targets the following challenges:

Class imbalance: Some classes are underrepresented, making it difficult for the model to learn distinguishing features.

Limited data size: Small datasets limit the ability to train deep learning models effectively, causing overfitting.

Generalization issues: Models trained on imbalanced or small datasets tend to overfit, resulting in poor performance on unseen data.

The goal of this project is to:

Generate synthetic images for underrepresented classes.

Create an augmented dataset by combining original and synthetic images.

Evaluate model performance on both original and augmented datasets to assess the impact of synthetic data.

Dataset Description
The dataset used for this project consists of approximately 1,100 images across 37 classes. Each class represents a distinct label relevant to the classification task. The key characteristics of the dataset include:

Class distribution: The dataset is highly imbalanced, with some classes containing fewer than 25 images and others exceeding 40 images.

Image variability: The images show varying backgrounds, lighting conditions, and object orientations, which makes the classification task more challenging.

Splitting: The dataset is divided into training, validation, and test sets to ensure reliable performance evaluation.

Synthetic Image Generation and Dataset Augmentation
To address the data limitations, synthetic images were generated using generative models such as GANs or diffusion models. These synthetic images:

Mimic the visual style and key features of the original images.

Increase the number of samples in minority classes to enhance class balance.

Improve intra-class variability, aiding the model's ability to generalize.

The augmented dataset combines the original images with the synthetic ones, providing a more balanced class distribution and a larger dataset for training.

Methodology
The project follows these key steps:

Data Preprocessing:

Images were resized and normalized for input into the model.

The data was split into training, validation, and test sets, ensuring each set preserves the class distribution.

Synthetic Image Generation:

Generative models were employed to produce synthetic images for underrepresented classes.

The synthetic images were validated for realism and relevance to the target classes.

Dataset Augmentation:

The synthetic images were merged with the original dataset, creating an augmented training dataset.

Model Training:

A CNN model was trained on both the original dataset and the augmented dataset.

Training protocols and hyperparameters were kept consistent across experiments for fair comparison.

Model Evaluation:

Model performance was evaluated using accuracy, precision, recall, and F1-score metrics.

A detailed analysis of per-class performance was conducted to measure improvements, especially for minority classes.

Solution Overview
The approach integrates synthetic data augmentation with deep learning-based image classification to improve the robustness of models trained on imbalanced datasets. By leveraging AI-generated images, the model benefits from a larger, more balanced dataset, reducing the bias towards majority classes and enhancing generalization across all categories.

Model Architecture
A Convolutional Neural Network (CNN) architecture was used for classification, consisting of the following layers:

Convolutional layers (with ReLU activation) to extract hierarchical features from the images.

Max-pooling layers for dimensionality reduction.

Dropout layers to prevent overfitting during training.

Fully connected layers with a softmax output layer for multi-class classification (37 classes).

The architecture balances model complexity and computational efficiency, suitable for the task and dataset size.

Training Procedure
Optimizer: Adam optimizer, with a learning rate that promotes stable convergence.

Batch size: Consistent across experiments for fairness.

Epochs: Early stopping based on validation loss to prevent overfitting.

Loss function: Categorical cross-entropy loss, which is ideal for multi-class classification problems.

Evaluation Metrics
Performance was evaluated using several key metrics:

Accuracy: The percentage of correct predictions out of all predictions.

Precision: The proportion of true positives among predicted positives.

Recall: The proportion of true positives among all actual positives.

F1-score: The harmonic mean of precision and recall, providing a balanced metric.

Metrics were calculated for each class and averaged using both macro and weighted approaches to assess overall performance.

Results and Analysis
Performance on Augmented Dataset
Test Accuracy: 72.55%

Macro Precision: 75.89%

Macro Recall: 72.02%

Macro F1-Score: 71.86%

The inclusion of synthetic images improved model performance across the board, with the largest gains observed in minority classes. The augmented data allowed the model to learn more diverse features, leading to better classification accuracy.

Performance on Original Dataset
Test Accuracy: 62.28%

Macro Precision: 69.64%

Macro Recall: 63.48%

Macro F1-Score: 63.09%

Without synthetic augmentation, the model struggled with minority classes due to class imbalance, resulting in lower performance metrics.

Detailed Interpretation
Improved recall for minority classes: Synthetic data augmentation significantly improved recall for underrepresented classes, allowing the model to identify more true positives.

Balanced precision: The model made fewer false-positive errors across all classes.

Enhanced robustness: The model trained on the augmented dataset exhibited more stability and better generalization, making it less prone to overfitting.

These findings demonstrate the effectiveness of synthetic data augmentation for imbalanced image classification tasks.

How to Use
Install dependencies: Ensure you have Python 3.8+ and the following libraries installed:

PyTorch

scikit-learn

numpy

matplotlib (optional for visualization)

pandas (optional for data handling)

Run the training script: The provided Python script includes everything needed to train the model:

Load the dataset.

Generate synthetic images.

Train the CNN model on both the original and augmented datasets.

Evaluate the model's performance.

Generate your own synthetic data: Modify the image generation function to suit your dataset or use a pre-trained generative model.

Dependencies
Python 3.8+

PyTorch or TensorFlow

scikit-learn

numpy

matplotlib (optional)

pandas (optional)
