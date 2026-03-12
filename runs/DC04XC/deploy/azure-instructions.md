# Azure Deployment Instructions
1. Login to ACR: `az acr login --name [REGISTRY_NAME]`
2. Tag: `docker tag mango-anomaly-api:latest [REGISTRY_NAME].azurecr.io/mango-anomaly:v1`
3. Push: `docker push [REGISTRY_NAME].azurecr.io/mango-anomaly:v1`
4. Deploy to ACI or App Service using the image.
