🍽️ Food Image Classification with Deep Learning
📌 Problem Introduction
🧠 Context
In the modern digital era, Computer Vision is revolutionizing the food industry in countless ways—from smart restaurant systems and calorie tracking apps to automated dietary assessments and intelligent menu generation. A fundamental requirement in these applications is the ability to accurately classify food items from images.

However, food classification presents several challenges:

High intra-class variability: The same dish may look drastically different depending on lighting, angle, garnishing, or even the region it comes from.

Inter-class similarity: Different dishes often share similar visual characteristics (e.g., tacos vs. taquitos or sandwiches vs. burgers).

Complex backgrounds: Many food images include distracting elements like cutlery, tablecloths, or other dishes.

The goal of this project is to develop a robust deep learning model capable of classifying food images into one of 14 categories, such as sushi, ice cream, donuts, sandwiches, etc., using PyTorch.

🧪 Dataset
The dataset consists of labeled food images across 14 categories, each with 200 samples for training, validation, and testing. All images are preprocessed to a uniform size and normalized.

Classes include:

Baked Potato

Crispy Chicken

Donut

Fries

Hot Dog

Sandwich

Taco

Taquito

Apple Pie

Cheesecake

Chicken Curry

Ice Cream

Omelette

Sushi

🧠 Model Architecture & Strategy
The project uses a custom or pretrained convolutional neural network (CNN) (replace this with ResNet, EfficientNet, etc. if used). The architecture is designed to extract robust spatial features and classify input images into their corresponding food categories.

Key features:

GPU-accelerated training (.to(device) support)

CrossEntropyLoss as loss function

Adam optimizer with standard hyperparameters

Softmax output activation for multi-class classification

🏋️‍♂️ Training Procedure
Training is carried out with several quality-of-life improvements for reproducibility and model robustness:

✅ Checkpointing
A custom save_checkpoint function stores:

Model weights

Optimizer state

Current epoch

Best validation accuracy and loss

Full classification report

This allows for recovery and analysis at any point in training.

⏸️ Early Stopping
An EarlyStopping class halts training when no significant validation loss improvement is observed after 5 consecutive epochs, with a minimum delta of 0.001. This prevents overfitting and saves compute resources.

📈 Final Evaluation & Results
After training, the model achieved the following performance on the test set (2800 samples):

Classification Report:

                                                                            
              precision    recall  f1-score   support

  Baked Potato       0.90      0.82      0.86       200
Crispy Chicken       0.80      0.84      0.82       200
         Donut       0.87      0.94      0.90       200
         Fries       0.83      0.89      0.86       200
       Hot Dog       0.81      0.78      0.79       200
      Sandwich       0.82      0.84      0.83       200
          Taco       0.76      0.61      0.68       200
       Taquito       0.71      0.81      0.76       200
     Apple Pie       0.86      0.63      0.73       200
    Cheesecake       0.79      0.83      0.81       200
 Chicken Curry       0.80      0.88      0.84       200
     Ice Cream       0.84      0.84      0.84       200
      Omelette       0.83      0.82      0.82       200
         Sushi       0.85      0.93      0.89       200

      Accuracy                           0.82      2800
     Macro Avg       0.82      0.82      0.82      2800
  Weighted Avg       0.82      0.82      0.82      2800
✅ Highlights:
Highest performance: Donut, Sushi, Chicken Curry

Lowest performance: Taco, Apple Pie—possibly due to visual similarity with other categories

📊 Confusion Matrix
A detailed confusion matrix was generated for further analysis. It reveals which classes the model confuses most frequently—helpful for understanding potential biases or limitations in the dataset.

Classes like Taco and Taquito, or Apple Pie and Cheesecake, show higher confusion, indicating a need for more distinctive features or better data representation.

🚀 How to Run the Project
1. Clone the repo and install dependencies:

git clone https://github.com/yourusername/food-classifier.git
cd food-classifier
pip install -r requirements.txt

2. Prepare your dataset:
Ensure the dataset is organized as:



dataset/
  train/
    class_1/
    class_2/
    ...
  val/
    class_1/
    ...
  test/
    ...

3. Train the model:


best_model, train_losses, val_losses, val_accuracies = train_model_with_early_stopping(
    model,
    train_loader,
    val_loader,
    criterion,
    optimizer,
    num_epochs=25,
    patience=5,
    checkpoint_path="best_model.pth"
)
4. Evaluate:


all_preds, all_labels = evaluate_model(best_model, test_loader, device)
print(classification_report(all_labels, all_preds, target_names=train_dataset.classes))
plot_confusion_matrix(all_labels, all_preds, train_dataset.classes)

                                                                            
🔮 Future Directions
Data Augmentation: Improve generalization using random flips, rotations, and color jittering.

Transfer Learning: Integrate pretrained models like ResNet50, EfficientNet, or ViT for better feature extraction.

Ensemble Methods: Combine multiple model outputs to boost performance.

Explainability: Use Grad-CAM or SHAP for visual interpretability of model predictions.

Mobile Deployment: Convert to ONNX or TensorFlow Lite for edge device use in mobile food apps.



