# Azure Deployment
1. Login to ACR: `az acr login --name <registry_name>`
2. Tag: `docker tag placement-model:latest <registry_name>.azurecr.io/placement-model:latest`
3. Push: `docker push <registry_name>.azurecr.io/placement-model:latest`
4. Deploy using Azure Container Instances (ACI).
