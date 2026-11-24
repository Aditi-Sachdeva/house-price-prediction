# House Price Prediction System

A Machine Learning based California Housing Price Prediction System that estimates median house values using regression algorithms and a Flask web application.

## Live Demo

**Try the application here:**  
[House Price Prediction System](https://house-price-prediction-4kjz.onrender.com/)

## Project Overview

This project uses the California Housing Dataset to analyze housing-related features and predict median house values.

It covers data preprocessing, exploratory data analysis, feature engineering, model training, model evaluation, and integration of the trained model into a Flask web application.

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
- Render

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
12. Deploying the application on Render

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

**Selected Model:** Random Forest Regressor

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
├── download_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
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

**Note:** The trained model file is hosted separately because of its large size and is downloaded automatically using `download_model.py`.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aditi-Sachdeva/house-price-prediction.git
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

### 5. Download the trained model

Run the following command:

```bash
python download_model.py
```

This downloads the trained Random Forest model from Google Drive and saves it inside the `models/` directory.

The model is hosted separately to avoid GitHub's file size limitations.

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Deployment

The application is deployed using Render.

**Live Application:**  
https://house-price-prediction-4kjz.onrender.com/

The deployment process uses Gunicorn to serve the Flask application and downloads the trained model during the build process.

## Dataset

**California Housing Dataset**

The model predicts median house values for California housing areas (census block groups), rather than the exact selling price of an individual property.

## Author

**Aditi Sachdeva**
