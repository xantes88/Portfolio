🧠 Fruit Classification with Ensemble Learning

A robust ML system that classifies exotic fruits using advanced preprocessing, feature scaling, class balancing (SMOTE), and ensemble models like Random Forest, SVM, and XGBoost.

📦 Business Use-Case

Used by a mid-size exporter with ~2M annual fruit shipments to automate quality sorting at the warehouse level.
Before implementation, visual inspection errors led to 5–8% misclassification, impacting both compliance and customer satisfaction.

💰 Business Value

✅ Reduces return costs by up to €20K/year by catching misclassified shipments early.

✅ Improves sorting precision to 88.7%, reducing false classification between visually similar fruits.

✅ Saves ~200 hours/year in manual quality control through automated predictions.

✅ Enables better forecasting by generating consistent classification logs per batch.

📊 Performance Metrics

Model	Accuracy (Test)	Notes
KNN	86.5%	Fast, slightly overfitting
Random Forest	86.0%	Balanced performance
SVM	88.7%	Best generalization
XGBoost	88.7%	High training accuracy (100%)
Voting Ensemble	88.7%	Stable across all classes
Stacking Model	87.5%	Meta-learning with LR

🔧 Key Features

SMOTE oversampling to balance class distribution

Outlier detection using IQR method

Feature importance extraction from Random Forest

Grid Search with RepeatedStratifiedKFold CV

Stacking and voting ensemble methods

🚀 Next Steps

Deploy as an internal API for batch or real-time fruit scanning at entry points

Extend model to include texture or image features

Integrate with IoT sensors in conveyor systems

Dashboard with live classification and alerting for anomalies

