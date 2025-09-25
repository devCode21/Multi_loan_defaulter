
# 📌 Multi Loan Defaulter Project

## 🚀 Overview
This project predicts **loan defaulters** using a complete **end-to-end pipeline** that includes:  
- Data analysis and model building (Jupyter Notebooks)  
- A **production-ready backend API** (Flask)  
- An interactive **frontend interface** (React)  

The solution helps financial institutions in assessing loan risks, improving credit decisions, and reducing defaults.

---

## 📊 Data Analysis
Performed in Jupyter Notebook: [`notebooks/data_analysis.ipynb`](./notebook/Notebook.ipynb)  

### 🔹 Key Steps
- **Data Loading & Exploration**  
  - Checked for class imbalance, missing values, feature distributions.  
  - Performed EDA with **KDE plots, bar charts, and heatmaps**.  

- **Feature Engineering**  
  - Processed numerical & categorical features.  
  - Removed irrelevant/low-variance columns.  
  - Created domain-specific features (ratios, groupings, flags).  
  - Encoded categorical variables using mapping dictionaries.  
  - Handled outliers and missing values.  

- **Modeling**  
  - Train-test split with preprocessing pipelines (`ColumnTransformer`, `SimpleImputer`).  
  - **Class imbalance addressed using SMOTE**.  
  - Models tested: Logistic Regression, Random Forest, XGBoost.  
  - Hyperparameter tuning with `GridSearchCV`.  
  - Best model (`XGBoost`) saved with `joblib`.  

- **Evaluation Metrics**  
  - Accuracy, F1-score, recall, precision.  
  - Feature importance analysis for interpretability.  

---

## 🏆 Model Performance
Final **XGBoost model** achieved:  

| Metric       | Class 0 | Class 1 |
|--------------|---------|---------|
| **Accuracy** | \~0.90  | -       |
| **F1 Score** | 0.93    | 0.32    |
| **Recall**   | 0.91    | 0.37    |
| **Precision**| 0.94    | 0.26    |

> ⚠️ Note: Class imbalance impacts Class 1 performance. Further improvements may include **cost-sensitive learning** or **ensemble balancing**.

---

## 🧠 Model Development
- Trained machine learning models for **loan default prediction**.  
- Evaluated with **accuracy, precision, recall, and ROC-AUC**.  
- Best-performing model serialized (`joblib`/`pickle`) for deployment.  

---

## ⚙️ Backend API
- Built using **Flask**.  
- REST API endpoints for **real-time inference**.  
- Handles **input validation** and returns predictions in **JSON** or **CSV**.  
- Example endpoint:  

```http
POST /predict
````

---

## 💻 Frontend

* Developed with **React**.
* Clean, user-friendly UI for inputting customer details and viewing predictions.
* Communicates with backend API for real-time results.

---

## 🏃 How to Run

### 1️⃣ Clone Repository

```bash
git clone <repo-url>
cd Multi_loan_defaulter
```

### 2️⃣ Setup Python Environment

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Backend

```bash
cd backend
python app.py
```

### 4️⃣ Run Frontend

```bash
cd frontend
npm install
npm start
```

### 5️⃣ Access Application

* Open browser at: **[http://localhost:3000](http://localhost:3000)**

---

## 📦 Requirements

* **Python** 3.8+
* **Node.js** (for frontend)
* Full dependencies in:

  * `requirements.txt` (backend)
  * `frontend/package.json` (frontend)

---

## 📂 Project Structure

```
Multi_loan_defaulter/
│
├── notebooks/
│   └── data_analysis.ipynb
├── backend/
│   ├── app.py
│   └── model.pkl
├── frontend/
│   └── (React code)
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

* **Improve Class 1 Performance** → Use ensemble balancing, cost-sensitive learning, or anomaly detection.
* **Model Explainability** → Integrate SHAP/LIME for better interpretability.
* **Cloud Deployment** → Deploy on AWS/GCP/Azure with CI/CD pipelines.
* **Database Integration** → Connect to SQL/NoSQL for real-time data ingestion.
* **Monitoring** → Add drift detection, dashboards, and logging for model performance.
* **Security** → Enhance input validation, authentication, and secure APIs.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👥 Contributors

* **Kadak Singh** – Data Scientist & Full-Stack Developer

```


