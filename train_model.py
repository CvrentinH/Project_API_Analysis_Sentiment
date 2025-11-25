import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#Chargement CSV

print("Chargement des données")
try : 
    df = pd.read_csv("dataset.csv")
    df = df.dropna()
    df['text'] = df['text'].str.strip()
    df['sentiment'] = df['sentiment'].str.strip()
    print(f"Data chargé {len(df)} lignes")
except FileNotFoundError :
    print("Erreur fichier introuvable")
    exit()

#Définition features

x = df["text"]
y = df["sentiment"]

#Séparation

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state = 42)
print(f"Training {len(X_train)}")
print(f"Test{X_test}")

#Création pipeline

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(lowercase=True, stop_words = "english")),
    ('classifier', LogisticRegression())
])

#Entrainement

print("Entrainement")
pipeline.fit(X_train, Y_train)

#Evaluation du modèle

print("Evaluation")
Y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy : {accuracy:.2f} (Signifiant {accuracy*100:.0f}% prédiciton correctes sur des données non vues)")

#Export

model_filename = "sentiment_model.pkl"
joblib.dump(pipeline, model_filename)
print(f"Modele sauvegardé sous le nom {model_filename}")