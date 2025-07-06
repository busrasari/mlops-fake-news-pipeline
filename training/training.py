import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

df_true = pd.read_csv("../data/True.csv")
df_fake = pd.read_csv("../data/Fake.csv")

df_true["label"] = 0
df_fake["label"] = 1

df = pd.concat([df_true, df_fake]).reset_index(drop=True)
df["text"] = df["title"] + " " + df["text"]

X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

pipe = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_df=0.7)),
    ("clf", LogisticRegression(max_iter=1000))
])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(pipe, "../model/fake_news_model.pkl")
