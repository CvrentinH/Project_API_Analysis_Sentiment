# API d'Analyse de Sentiments

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.5-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Résumé

Ce projet présente une API d'analyse de sentiment (texte)
Il dépasse la simple modélisation théorique en implémentant une architecture logicielle prête pour la production :

1.  **Machine Learning** : Entraînement d'un modèle de Régression Logistique sur un dataset personnalisé (`pandas`, `scikit-learn`) et sérialisation (`joblib`).
2.  **Développement API** : Exposition du modèle via (`FastAPI`).
3.  **Conteneurisation** : Dockerisation de l'application pour garantir la reproductibilité (`Docker`).
4.  **Infrastructure as Code (IaC)** : Automatisation du déploiement sur un cluster Kubernetes local (`Terraform`).
5.  **Tests** : Tests d'API automatisés utilisant (`Bruno`).


## Architecture

* **Phase d'Entraînement (Training) :** Le script `train_model.py` utilise le fichier `dataset.csv`, pré-traite le texte (TF-IDF), entraînant le modèle et sauvegarde le fichier (`sentiment_model.pkl`).
* **Phase d'Inférence (Serving) :** L'API charge le fichier `.pkl` au démarrage pour utiliser les prédictions instantanément sans ré-entraînement.


## Comment lancer le projet

### Prérequis
* Python 3.11+
* Docker Desktop / Minikube
* Terraform
* Git

### Entraînement du Modèle
Générer l'artifact du modèle à partir des données brutes.

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'entraînement (crée sentiment_model.pkl)
python train_model.py