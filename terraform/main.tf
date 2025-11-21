terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment" "sentiment_api" {
  metadata {
    name = "sentiment-api-deployment"
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "sentiment-api"
      }
    }

    template {
      metadata {
        labels = {
          app = "sentiment-api"
        }
      }

      spec {
        container {
          image = "sentiment-api:latest"
          name  = "sentiment-api-container"
          image_pull_policy = "IfNotPresent"

          port {
            container_port = 8000
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "sentiment-api-service" {
    metadata {
        name = "sentiment-api-service"
    }

    spec {
        selector = {
            app = "sentiment-api"
        }

        port {
            port        = 80
            target_port = 8000
        }

        type = "NodePort"
    }
}