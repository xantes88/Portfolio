🥭 Exotic Fruit Classification with Advanced Machine Learning
📌 Project Overview
This project focuses on the classification of exotic fruits using a full machine learning pipeline, including:

Exploratory data analysis

Data preprocessing and outlier removal

Class balancing using SMOTE

Training and hyperparameter tuning for multiple classifiers (KNN, Random Forest, SVM, XGBoost)

Ensemble learning using Voting and Stacking models

Evaluation with robust metrics and visualizations

📊 Dataset Description
Samples: 500 rows

Features:

Weight (g)

Average Diameter (mm)

Average Length (mm)

Skin Hardness (scale 1–10)

Sweetness (scale 1–10)

Target: Fruit type

The dataset contains no missing values. Outliers were handled using the Interquartile Range (IQR) method.

🧠 Models Trained
Model	Accuracy (Test Set)
K-Nearest Neighbors	86.5%
Random Forest	86.0%
SVM (Linear Kernel)	88.7%
XGBoost	88.7%
Voting Classifier	88.7%
Stacking Classifier	87.5%

🛠 Techniques & Tools
Preprocessing: Label Encoding, Standard Scaling

Outlier Handling: IQR method

Class Imbalance: SMOTE (k=1), compute_class_weight

Cross-validation: Repeated Stratified K-Fold

Hyperparameter Tuning: GridSearchCV

Evaluation: Accuracy, Precision, Recall, F1-Score, Confusion Matrix

📈 Visual Analysis
Scatterplots: Feature distribution by class

Boxplots: Outlier detection

Heatmap: Feature correlation

Confusion Matrices: Model evaluation

Feature Importance: Random Forest interpretation

💼 Business Value

✅ Demonstrates ability to build end-to-end machine learning pipelines
✅ Applicable in industries like agriculture, food analytics, retail, and supply chain optimization
✅ Ensemble learning boosts model robustness, improving real-world deployability
✅ Emphasizes data quality, preprocessing, and explainability — critical for production systems

🔍 Key Insights
SVM and XGBoost performed best individually.

Ensemble methods improved generalization without major accuracy trade-offs.

Proper handling of outliers and class imbalance significantly improved model stability.

🔮 Next Steps
Integrate Explainable AI techniques (e.g., SHAP)

Deploy model with Flask or Streamlit for real-time predictions

Use MLflow or similar tools for model tracking and experiment management
