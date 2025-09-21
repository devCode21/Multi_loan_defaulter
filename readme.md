# Multi Loan Defaulter Project

## Overview
This project predicts loan defaulters using data analysis, a production-ready backend API, and a frontend interface.

---

## Table of Contents
- [Data Analysis](#data-analysis)
- [Model Development](#model-development)
- [Backend API](#backend-api)
- [Frontend](#frontend)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [Project Structure](#project-structure)

---

## Data Analysis
- Performed in Jupyter Notebook.
- Steps include data cleaning, EDA, feature engineering, and model selection.
- Visualizations and insights are documented in `notebooks/data_analysis.ipynb`.


- **Data Loading & Exploration:**  
    The dataset is loaded and explored for class imbalance, missing values, and feature distributions. Visualizations (KDE plots, bar charts, heatmaps) are used for EDA.

- **Feature Engineering:**  
    - Numerical and categorical features are identified and processed.
    - Irrelevant or low-variance columns are dropped.
    - New features are created (e.g., ratios, groupings, flags).
    - Categorical variables are encoded using mapping dictionaries.
    - Outliers and missing values are handled appropriately.

- **Modeling:**  
    - Data is split into training and test sets.
    - Preprocessing pipelines are built using `ColumnTransformer` and `SimpleImputer`.
    - Class imbalance is addressed using SMOTE.
    - Multiple models are evaluated: Logistic Regression, Random Forest, XGBoost.
    - Hyperparameter tuning is performed with `GridSearchCV`.
    - The best model (XGBoost) is saved using `joblib`.

- **Evaluation:**  
    - Models are evaluated using cross-validation and classification metrics (F1, recall, precision).
    - Feature importance and model interpretability are considered.

## Model Performance

The final XGBoost model achieved the following metrics on the test set:

- **Accuracy:** ~0.90
- **F1 Score:** ~0.93->class 0 && 0.32->class 1
- **Recall:** ~0.91 ->class 1 && .37 ->class 1
- **Precision:** ~0.94 ->class 0 && .26->clss1

>
## Model Development
- Trained machine learning models to predict loan default.
- Evaluated models using metrics like accuracy, precision, recall, and ROC-AUC.
- Best model serialized (e.g., with `joblib` or `pickle`) for deployment.

## Backend API
- Built with Flask
- Exposes endpoints for model inference.
- Handles input validation and returns predictions in JSON format and Csv .
- Example endpoint: `/predict`

## Frontend
- Developed using React
- User-friendly interface to input data and view predictions.
- Communicates with backend API for real-time results.

---

## How to Run

### 1. Clone the repository
```bash
git clone <repo-url>
cd Multi_loan_defaulter
```

### 2. Setup Environment
```bash
pip install -r requirements.txt
```

### 3. Run Backend
```bash
cd backend
python app.py
```

### 4. Run Frontend
```bash
cd frontend
npm install
npm start
```

### 5. Access Application
- Open your browser at `http://localhost:3000`

---

## Requirements
- Python 3.8+
- Node.js (for frontend)
- See `requirements.txt` and `frontend/package.json` for details

---

## Project Structure
```
Multi_loan_defaulter/
│
├── notebooks/
│   └── data_analysis.ipynb
├── backend/
│   ├── app.py
│   └── model.pkl
├── frontend/
│   └── (frontend code)
├── requirements.txt
└── README.md
```

---

## License
MIT License

---

## Contributors
- Kadak singh 
