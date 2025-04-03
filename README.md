# Car Insurance Claim Prediction

## 📌 Project Description
The project is dedicated to predicting insurance claims for car policies. It uses a dataset from Kaggle containing information about policies, car characteristics, and car owners. The target variable indicates whether the policyholder files a claim within the next 6 months

## 📌 Kaggle Competition
The dataset used in this project is from the Kaggle competition: [Car Insurance Claim Prediction - Classification](https://www.kaggle.com/datasets/ifteshanajnin/carinsuranceclaimprediction-classification)


## 📊 Data Description

The dataset contains the following features:
- **policy tenure** — the duration of the policy,
- **age of the car** — the age of the car,
- **age of the car owner** — the age of the car owner,
- **population density** — the population density of the city,
- **make and model** — the make and model of the car,
- **power, engine type** — the power and type of the engine,
- **and other parameters**.

The target variable (**target**) indicates whether the car owner files an insurance claim in the next 6 months (1 - yes, 0 - no).

## 🔍 Data Preprocessing
1. Data analysis and checking for missing values.
2. Encoding categorical features using **OHE (One-Hot Encoding)** and **MTE (Mean Target Encoding)**.
3. Detection and handling of outliers.
4. Creating a separate `BaseEstimator` class for transforming categorical features.
5. Analyzing feature distributions.
6. Generating new features.
7. Checking correlations and removing highly correlated features.
8. Checking for quasi-constant features.
9. Balancing the dataset using **SMOTE** (Synthetic Minority Over-sampling Technique).

## 🏆 Model Training
The following models were trained and tested:
- **RandomForest**
- **XGBoost**
- **LightGBM**

Hyperparameter tuning was performed using **Grid Search**. The models' performance was evaluated using the following metrics:
- **Precision**
- **Recall**
- **F1-score**
- **Accuracy**

### 📈 Results
Best model: **LightGBM**
- **F1-score:** 0.96
- **Accuracy:** 0.96
- **ROC AUC:** 0.9766 (on the test set)

A **ROC curve** was created, and the area under the curve (AUC) was calculated.

## 🚀 Model Deployment
A **FastAPI-based API service** was developed, which allows getting predictions using the insurance policy number through HTTP requests.

## 📌 Running the Project
### Installing dependencies
```bash
pip install -r requirements.txt
```
### Running the service
```bash
uvicorn app:app --reload
```

## 📌 Контакты
If you have any questions or suggestions, you can reach out to me via GitHub Issues or Telegram: [@elina_glmv](https://t.me/elina_glmv)

