from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class SentimentRequest(BaseModel):
    text : str

@app.post("/predict/")
def predict_sentiment(item: SentimentRequest):
    analysis = TextBlob(item.text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        sentiment_label = "positive"
    elif sentiment < 0:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"
    return {"text": item.text, "sentiment": sentiment_label, "polarity": sentiment}