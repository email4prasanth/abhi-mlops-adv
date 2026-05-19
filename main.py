from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import numpy as np

# print the column data type
url = "https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/diabetes.csv"
df = pd.read_csv(url)
column_type = print(df.dtypes)

# Create an Instance/Method of Fast API
app = FastAPI()
model = joblib.load("diabetes_model.pkl")

# Create class Feature and type
class diabetesinput(BaseModel):
        Pregnancies             :      int
        Glucose                 :      int
        BloodPressure           :      int
        SkinThickness           :      int
        Insulin                 :      int
        BMI                     :    float
        DiabetesPedigreeFunction:    float
        Age                     :      int
# Using decorator '@' to functions or methods
@app.get('/')
def index():
    return "Welcome to diatebets Prediction"

@app.post('/predict')
def model_predict(data: diabetesinput ):
      input_data=np.array(
            [[
                data.Pregnancies,             
                data.Glucose    ,             
                data.BloodPressure ,          
                data.SkinThickness ,          
                data.Insulin     ,            
                data.BMI         ,            
                data.DiabetesPedigreeFunction,
                data.Age                        
            ]]
      )
      prediction = model.predict(input_data)[0]
      return {"diabetic": bool(prediction)}