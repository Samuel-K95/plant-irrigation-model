from fastapi import FastAPI, HTTPException
from app.model_handler import load_model
from app.schema import InputData, PredictionResult
import numpy as np

app = FastAPI(title="ML Prediction API")

@app.on_event("startup")
def startup_event():
    try:
        load_model()
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {str(e)}")

@app.post("/predict", response_model=PredictionResult)
def predict(data: InputData):
    try:
        model = load_model()
        input_dict = data.features
        features = np.array([list(input_dict.values())])
        prediction = model.predict(features)[0]
        return PredictionResult(prediction=float(prediction))
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
