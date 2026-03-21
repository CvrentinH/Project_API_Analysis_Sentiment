import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset.csv")
df = df.dropna()
df['text'] = df['text'].str.strip()
df['sentiment'] = df['sentiment'].str.strip()

x = df["text"]
y = df["sentiment"]

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state = 42)
print(f"Training {len(X_train)}")   
print(f"Test {len(X_test)}")

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(lowercase=True, stop_words = "english")),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, Y_train)

Y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy {accuracy:.2f} ({accuracy*100:.0f}% correct predictions)")

model_filename = "sentiment_model.pkl"
joblib.dump(pipeline, model_filename)
print(f"{model_filename} saved")
