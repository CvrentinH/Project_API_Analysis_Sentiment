from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("sentiment_model.pkl")
print("Modèle chargé")

app = FastAPI()

class sentimentRequest(BaseModel):
    text : str

@app.get("/")
def read_root():
    return {"Message": "Sentiment Analysis API"}

@app.post("/predict/")
def predict_sentiment(request: sentimentRequest):
    if model is None:
        return {"error": "No model available"}
    prediction = model.predict([request.text])
    sentiment_label = prediction[0]
    probabilities = model.predict_proba([request.text])
    confidence_score = np.max(probabilities)

    return {
            "text": request.text,"sentiment": sentiment_label,"confidence": round(confidence_score, 2), "model_type": "Logistic Regression v1"
            }  
