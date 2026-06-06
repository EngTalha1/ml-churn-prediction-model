# Customer Churn Prediction Using Machine Learning

## Project Overview

Customer churn is a major challenge for subscription-based businesses. Predicting customer churn allows companies to identify customers who are likely to leave and take proactive actions to retain them.

This project uses machine learning techniques to predict customer churn based on customer demographics, service subscriptions, contract details, and billing information.

---

## Dataset

The dataset contains customer-related information including:

* Demographic information
* Service subscription details
* Contract information
* Billing and payment details

Target Variable:

* Churn = 1 → Customer Left
* Churn = 0 → Customer Stayed

---

## Data Preprocessing

The following preprocessing steps were performed:

* Missing value handling
* One-Hot Encoding of categorical variables
* Train-Test Split
* Data Cleaning and Type Conversion

---

## Machine Learning Models Used

The following models were trained and compared:

1. K-Nearest Neighbors (KNN)
2. Decision Tree Classifier
3. Random Forest Classifier

Hyperparameter tuning was performed using GridSearchCV with Stratified Cross Validation.

---

## Results

Best Performing Model:

* Random Forest Classifier

Best Parameters:

* max_depth = 5
* n_estimators = 50

Test Accuracy:

* 79.33%

---

## Visualizations

The project includes:

* Model Accuracy Comparison
* Feature Importance Analysis
* Confusion Matrix

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn

---

## Key Learning Outcomes

* Data preprocessing
* Feature encoding
* Hyperparameter tuning using GridSearchCV
* Model comparison
* Cross-validation
* Feature importance analysis
* Classification model evaluation

---

## Future Improvements

* Additional feature engineering
* Advanced ensemble models
* Probability-based churn analysis
* Deployment as a web application
