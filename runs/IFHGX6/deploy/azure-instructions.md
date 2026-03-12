# Azure Deployment Guide
1. Login: `az acr login --name <registry_name>`
2. Tag: `docker tag amazon-clustering-app:latest <registry_name>.azurecr.io/amazon-clustering:latest`
3. Push: `docker push <registry_name>.azurecr.io/amazon-clustering:latest`
4. Deploy to ACI or Web App for Containers.
