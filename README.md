
# House Price Prediction System

A Machine Learning based California Housing Price Prediction System that estimates median house values using regression algorithms and a Flask web application.

## Project Overview

This project uses the California Housing Dataset to analyze housing-related features and predict median house values.

The project includes data preprocessing, exploratory data analysis, feature engineering, model training, model evaluation, and deployment through a Flask-based web interface.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- HTML
- CSS
- Jupyter Notebook

## Machine Learning Workflow

1. Dataset loading and exploration
2. Exploratory Data Analysis (EDA)
3. Handling missing values
4. Encoding categorical features
5. Feature engineering
6. Train-test splitting
7. Training and comparing regression models
8. Model evaluation
9. Selecting the best-performing model
10. Saving the trained model using Joblib
11. Integrating the model with Flask

## Feature Engineering

The following features were created:

- `rooms_per_household`
- `bedrooms_per_room`
- `population_per_household`

## Models Implemented

- Linear Regression
- Polynomial Regression
- Decision Tree Regression
- Random Forest Regression

A Dummy Regressor was also used as a baseline for comparison.

## Best Model Performance

Selected Model: Random Forest Regressor

| Evaluation Metric | Result |
|---|---:|
| R² Score | 80.63% |
| MAE | $32,311.34 |
| RMSE | $50,378.95 |

## Web Application

The Flask application allows users to enter housing area information, including:

- Longitude and Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

The application processes the inputs, performs the required feature engineering and encoding, and displays the predicted median house value.

## Project Structure

```text
house-price-prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── best_house_price_model.pkl
│   └── feature_columns.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── notebooks/
    └── ML-Project.ipynb
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd house-price-prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add the trained model

Place the trained model file and feature columns file inside the `models/` directory.

The large trained model file is not included in this GitHub repository.

### 6. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## Dataset

California Housing Dataset.

The model predicts median house values for California housing areas (census block groups), rather than the exact selling price of an individual property.

## Author

Aditi Sachdeva
