import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Loading CSV


df = pd.read_csv("dataset.csv")
df = df.dropna()
df['text'] = df['text'].str.strip()
df['sentiment'] = df['sentiment'].str.strip()

# Features

x = df["text"]
y = df["sentiment"]

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state = 42)
print(f"Training {len(X_train)}")
print(f"Test{X_test}")

# Pipeline

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(lowercase=True, stop_words = "english")),
    ('classifier', LogisticRegression())
])

# Training

print("Training")
pipeline.fit(X_train, Y_train)

# Evaluating model

print("Evaluating")
Y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy {accuracy:.2f} ({accuracy*100:.0f}% correct predictions)")

#Export

model_filename = "sentiment_model.pkl"
joblib.dump(pipeline, model_filename)
print(f"Model saved under the name {model_filename}")
