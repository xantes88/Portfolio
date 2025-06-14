# 🧠 Fruit Classification with Ensemble Learning

A robust ML system that classifies exotic fruits using advanced preprocessing, feature scaling, class balancing (SMOTE), and ensemble models like Random Forest, SVM, and XGBoost.

---

## 📦 Business Use Case

Designed for simulation in a **mid-size export company** handling ~2M fruit shipments/year.  
The model automates quality sorting at warehouse level using batch data (e.g., weight, diameter, sweetness).

Before automation, **manual visual inspection led to 5–8% misclassification**, impacting both compliance and client satisfaction.  
This system uses ML to simulate a consistent and automated classification process.

---

## 💰 Business Value 

✅ **~€20K/year saved** by catching misclassifications before shipment (based on 1% error reduction across 2M units)  
✅ Sorting **precision improved to 88.7%**, especially on visually similar classes  
✅ Saves ~200 hours/year in **manual classification** (estimated 30 seconds per sample for 50,000 checked units)  
✅ Enables better batch forecasting through consistent digital logs

---

## 📊 Performance Metrics

| Model            | Accuracy (Test) | Notes                         |
|------------------|-----------------|-------------------------------|
| KNN              | 86.5%           | Fast, slightly overfitting    |
| Random Forest    | 86.0%           | Balanced performance          |
| SVM              | 88.7%           | Best generalization           |
| XGBoost          | 88.7%           | 100% train accuracy (overfit) |
| Voting Ensemble  | 88.7%           | Stable across all classes     |
| Stacking Model   | 87.5%           | Meta-learning with LR         |

---

## 🔧 Key Features

- **Outlier detection** via IQR  
- **SMOTE balancing** with `k_neighbors=1`  
- **StandardScaler** for feature scaling  
- **LabelEncoder** for fruit class encoding  
- **Grid Search** with `RepeatedStratifiedKFold`  
- **Ensemble Learning**: Voting and Stacking with KNN, RF, SVM, XGBoost  
- **Feature importance** chart (Random Forest)  
- **Confusion Matrix** and classification reports for all models  

---

## 📈 Data Snapshot

- 500 samples, 6 features:  
  `Peso (g)`, `Diametro medio`, `Lunghezza media`, `Durezza buccia`, `Dolcezza`, `Frutto`  
- Cleaned from outliers using IQR  
- No missing values  

---

## 🚀 Next Steps

- Deploy as **internal API** for batch or real-time warehouse scanning  
- Extend features with **texture or image inputs** from cameras  
- Integrate with **IoT conveyor systems** for smart labeling  
- Create a **Power BI / Python dashboard** for real-time classification tracking and anomaly detection  

