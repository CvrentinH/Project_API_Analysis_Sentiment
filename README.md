# 🚀 MLOps Sentiment Analysis API

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.5-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## 📋 Overview

This project demonstrates a complete **End-to-End MLOps pipeline**.
It goes beyond simple modeling by implementing a production-ready architecture:

1.  **Machine Learning**: Training a Logistic Regression model on a custom dataset (`pandas`, `scikit-learn`) and serializing it (`joblib`).
2.  **API Development**: Serving the model via a high-performance REST API (`FastAPI`).
3.  **Containerization**: Packaging the application for reproducibility (`Docker`).
4.  **Infrastructure as Code**: Automating the deployment on a local Kubernetes cluster (`Terraform`).
5.  **Testing**: Automated API testing (`Bruno`).

---

## 🏗️ Architecture

The project follows a decoupling strategy between Training and Inference:

* **Training Phase:** `train_model.py` consumes `dataset.csv`, preprocesses text (TF-IDF), trains the model, and saves the artifact (`sentiment_model.pkl`).
* **Inference Phase:** The API loads the `.pkl` artifact at startup to serve predictions efficiently.

---

## ⚙️ How to Run Locally

### Prerequisites
* Python 3.11+
* Docker Desktop / Minikube
* Terraform
* Git

### 1. Model Training
First, generate the model artifact from the raw data.

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model (creates sentiment_model.pkl)
python train_model.py