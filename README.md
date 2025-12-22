# Student Performance Predictor

Predicts whether a student will **pass or fail** based on exam scores and background features using Logistic Regression and Random Forest.

## Overview
- Built a machine learning pipeline on the Kaggle *Students Performance in Exams* dataset.
- Encodes categorical features, trains models, and evaluates using accuracy and cross-validation.
- Includes confusion matrix and coefficient plots to interpret model decisions.

## Dataset
- Source: Kaggle – StudentsPerformance in exams dataset.
- 1000 rows, features like gender, race/ethnicity, parental education, lunch, test preparation, and three exam scores.

## Models
- Logistic Regression: mean CV accuracy ≈ 0.999, winner vs Random Forest.
- Random Forest: mean CV accuracy ≈ 0.982 on the same encoded features.
- Confusion matrix and coefficient/bar plots used for interpretability.

## How to Run
git clone <https://github.com/nazneenahmed11/student-performance-predictor>
cd student-performance-predictor
python -m venv .venv
..venv\Scripts\activate # Windows
pip install -r requirements.txt
jupyter notebook main.ipynb

## Results
- Very high accuracy on pass/fail prediction.
- Important factors include exam scores and preparation-related features (from coefficient analysis).

## Tech Stack
- Python, Jupyter Notebook, VS Code
- pandas, NumPy
- scikit-learn (Logistic Regression, RandomForestClassifier)
- matplotlib, seaborn
- Git and GitHub for version control

## Features
- Exploratory data analysis (EDA) on a student performance dataset
- Feature engineering and one-hot encoding for categorical variables
- Two models: Logistic Regression and Random Forest
- 5-fold cross-validation and model comparison (CV ~0.999 vs ~0.982)
- Confusion matrix and coefficient/bar plots for model interpretability





