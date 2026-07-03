import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# Load model and feature names
model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")


class HouseFeatures(BaseModel):
    MedInc: float = Field(gt=0, description="Median income of neighbourhood")
    HouseAge: float = Field(gt=0, description="Average age of houses")
    AveRooms: float = Field(gt=0, description="Average number of rooms")
    AveBedrms: float = Field(gt=0, description="Average number of bedrooms")
    Population: float = Field(gt=0, description="Population in the area")
    AveOccup: float = Field(gt=0, description="Average occupants per household")
    Latitude: float = Field(ge=32, le=42, description="Latitude")
    Longitude: float = Field(ge=-125, le=-114, description="Longitude")


@app.get("/")
def home():
    return {
        "Message": "California House Price Prediction API",
        "Status": "Running",
        "Endpoint": "Send POST request to /predict"
    }


@app.get("/health")
def health():
    return {
        "Status": "Running",
        "Model": "RandomForestRegressor",
        "Features": features,
        "Average_Error": "$39,000"
    }


@app.post("/predict")
def predict(house: HouseFeatures):
    try:
        # Convert input into DataFrame
        input_data = pd.DataFrame([{
            "MedInc": house.MedInc,
            "HouseAge": house.HouseAge,
            "AveRooms": house.AveRooms,
            "AveBedrms": house.AveBedrms,
            "Population": house.Population,
            "AveOccup": house.AveOccup,
            "Latitude": house.Latitude,
            "Longitude": house.Longitude
        }])

        # Make prediction
        predicted = model.predict(input_data)[0]

        # Convert from $100,000 units to dollars
        price_usd = predicted * 100000

        return {
            "Predicted_Price": f"${price_usd:,.0f}",
            "Predicted_Price_Short": f"${predicted:.2f} hundred thousands",
            "Confidence_Range": f"${price_usd - 39000:,.0f} to ${price_usd + 39000:,.0f}"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )