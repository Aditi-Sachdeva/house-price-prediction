
import os
import joblib
import pandas as pd

from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model and feature columns

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR, "models", "best_house_price_model.pkl"
)

FEATURE_PATH = os.path.join(
    BASE_DIR, "models", "feature_columns.pkl"
)

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)

# Ocean proximity categories

OCEAN_CATEGORIES = [
    "<1H OCEAN",
    "INLAND",
    "ISLAND",
    "NEAR BAY",
    "NEAR OCEAN"
]

# Home route

@app.route("/")
def home():
    return render_template(
        "index.html",
        ocean_categories=OCEAN_CATEGORIES
    )


# House price prediction route

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Read numerical inputs
        longitude = float(request.form["longitude"])
        latitude = float(request.form["latitude"])
        housing_median_age = float(
            request.form["housing_median_age"]
        )
        total_rooms = float(request.form["total_rooms"])
        total_bedrooms = float(request.form["total_bedrooms"])
        population = float(request.form["population"])
        households = float(request.form["households"])
        median_income = float(request.form["median_income"])

        ocean_proximity = request.form["ocean_proximity"]

        # Validate numerical values
        numeric_values = [
            longitude, latitude, housing_median_age,
            total_rooms, total_bedrooms, population,
            households, median_income
        ]

        if not all(pd.notna(value) and abs(value) != float("inf")
                   for value in numeric_values):
            raise ValueError("Please enter valid numerical values.")

        if total_rooms <= 0 or households <= 0:
            raise ValueError(
                "Total rooms and households must be greater than zero."
            )

        if total_bedrooms < 0 or population < 0:
            raise ValueError(
                "Bedrooms and population cannot be negative."
            )

        if ocean_proximity not in OCEAN_CATEGORIES:
            raise ValueError("Please select a valid ocean proximity.")

        # Feature engineering

        rooms_per_household = total_rooms / households

        bedrooms_per_room = (
            total_bedrooms / total_rooms
        )

        population_per_household = (
            population / households
        )

        # Prepare input features

        input_data = {
            "longitude": longitude,
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "rooms_per_household": rooms_per_household,
            "bedrooms_per_room": bedrooms_per_room,
            "population_per_household": population_per_household
        }

        # One-hot encode ocean proximity
        for category in OCEAN_CATEGORIES:
            column_name = f"ocean_proximity_{category}"

            input_data[column_name] = (
                1 if ocean_proximity == category else 0
            )

        # Convert to DataFrame in the exact training order
        input_df = pd.DataFrame([input_data])

        input_df = input_df.reindex(
            columns=feature_columns,
            fill_value=0
        )

        # Predict house price

        predicted_price = model.predict(input_df)[0]

        return render_template(
            "index.html",
            ocean_categories=OCEAN_CATEGORIES,
            prediction=f"${predicted_price:,.2f}"
        )

    except (ValueError, KeyError) as error:

        return render_template(
            "index.html",
            ocean_categories=OCEAN_CATEGORIES,
            error=str(error)
        )

    except Exception:

        return render_template(
            "index.html",
            ocean_categories=OCEAN_CATEGORIES,
            error="Something went wrong while predicting. Please try again."
        )


# Run Flask application

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
