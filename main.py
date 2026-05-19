from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

MODEL_PATH = os.getenv("MODEL_PATH", "models/diabetes_model.pkl")
model = None

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load(MODEL_PATH)

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/")
def index():
    return {"message": "Diabetes Prediction API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: DiabetesInput):
    try:
        input_data = np.array([[
            data.Pregnancies,
            data.Glucose,
            data.BloodPressure,
            data.SkinThickness,
            data.Insulin,
            data.BMI,
            data.DiabetesPedigreeFunction,
            data.Age
        ]])

        prediction = model.predict(input_data)[0]
        return {"diabetic": bool(prediction)}

    except Exception as e:
        return {"error": str(e)}