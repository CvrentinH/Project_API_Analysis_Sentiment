# MLOps Sentiment Analysis API

![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Overview
This project presents a complete sentiment analysis API. 
It implements a **production-ready** MLOps architecture:

1.  **Machine Learning** : Training a Logistic Regression model on a custom dataset (`pandas`, `scikit-learn`) and serialization (`joblib`).
2.  **API Développement** : Exposing the model via (`FastAPI`).
3.  **Dockerization** : Dockerizing the application to ensure reproducibility (`Docker`).
4.  **Infrastructure as Code (IaC)** : Automating deployment on a local Kubernetes cluster (`Terraform`).
5.  **Tests** : Automated API testing (`Bruno`).

---

## Architecture

The project follows a strict separation between training and usage:

* **Training phase :** The script `train_model.py` use the file `dataset.csv`, re-processes the text (TF-IDF vectorization), trains the model, and saves the logic into a binary file (`sentiment_model.pkl`).
* **Inference Phase (Serving) :** The API loads this `.pkl` file at startup to serve instant predictions without needing to retrain the model.

---

## Model Visualization & Interpretation (And Limitations)

To understand how the model makes decisions, we extracted the coefficients from the Logistic Regression. The chart below shows the words that most influence the decision toward "Positive" (Green) or "Negative" (Red).

![Explicabilité du modèle](feature_importance.png)

### Why do neutral words seem "polarized"?
You may notice that some seemingly neutral words appear strongly colored.

This is explained by **Dataset Bias**: Since the training dataset is small, the model works by direct association.

* If a neutral word often appears in a sentence containing `amazing`, the model will deduce that the associated word is positive in itself.
* Conversely, if a neutral word frequently appears next to `awful`, it will be considered negative.

---

## How to Run the Project

### Prerequisites

* Python 3.11+
* Docker Desktop / Minikube
* Terraform
* Git
* Make

### Option 1: Quick Start (Via Makefile)
The entire pipeline (Installation, Training, Docker Build, Minikube, Terraform) is automated.

```bash
make first-run
```

### Option 2: Manual Setup

### 1. Model Training
Generate the artifact (`.pkl`) from raw datas.

```bash
# Install dependencies
pip install -r requirements.txt

# Run training
python train_model.py
```

### 2. Docker Build
Package the API.

```bash
docker build -t sentiment-api:latest .

# (If using Minikube) Load the image into the cluster
minikube image load sentiment-api:latest
```

### 3. Deployment (IaC)
Deploy the infrastructure on Kubernetes via Terraform.

```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### 4. Accessing the API
Once the infrastructure is deployed, here are 3 ways to test the API:

#### Option A: Visual Interface
Retrieve the service URL:
```bash
minikube service sentiment-api-service --url
```

Open this URL in your browser and add /docs to the end. 
You can test the endpoints directly via the Swagger UI interface.

#### Option B: Automated Tests (Bruno)
The project contains a ready-to-use API test collection.

Open the **Bruno** application.
- Click on Open Collection.
- Select the sentiment api folder located at the root of this project.
- Run the Predict Sentiment request (Don't forget to update the URL with your Minikube URL).

### Option C : Terminal (CURL)
You can test directly from your terminal:

```bash
curl -X 'POST' \
  'http://MINIKUBE_URL:PORT/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "The deployment pipeline is robust and efficient."
}'
```

## Cleanup
To remove the created resources:

```bash
cd terraform && terraform destroy
minikube stop
```
