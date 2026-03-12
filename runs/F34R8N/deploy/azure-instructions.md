# Azure Deployment Guide
1. Login to Azure: `az login`
2. Create Container Registry: `az acr create --resource-group [RG] --name [NAME] --sku Basic`
3. Tag: `docker tag apple-sales-forecasting:latest [NAME].azurecr.io/apple-sales:v1`
4. Push: `docker push [NAME].azurecr.io/apple-sales:v1`
5. Deploy to App Service using `az webapp create`
