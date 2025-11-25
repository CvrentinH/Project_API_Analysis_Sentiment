TFLAG=-chdir=terraform/

build:
	pip install -r requirements.txt \
	&& python train_model.py \
	&& docker build -t sentiment-api:latest . \
	&& minikube start \
	&& minikube image load sentiment-api:latest

init:
	terraform $(TFLAG) init

apply:
	terraform $(TFLAG) apply -auto-approve

run:
	minikube service sentiment-api-service --url

first-run: build init apply run