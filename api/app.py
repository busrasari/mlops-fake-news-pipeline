from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("../model/fake_news_model.pkl")

app = FastAPI(title="Fake News Detection API")

class NewsItem(BaseModel):
    title: str
    text: str

@app.post("/predict")
def predict(news: NewsItem):
    content = news.title + " " + news.text
    prediction = model.predict([content])[0]
    result = "FAKE" if prediction == 1 else "REAL"
    return {"prediction": result}
