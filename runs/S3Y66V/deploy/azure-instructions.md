# Azure Deployment Guide

1. Login to ACR:
   `az acr login --name <acr_name>`
2. Tag image:
   `docker tag student-productivity-api <acr_name>.azurecr.io/student-productivity-api:latest`
3. Push image:
   `docker push <acr_name>.azurecr.io/student-productivity-api:latest`
4. Deploy on Azure Container Instances (ACI):
   `az container create --resource-group <rg> --name <name> --image <acr_name>.azurecr.io/student-productivity-api:latest --cpu 1 --memory 1.5 --registry-login-server <acr_name>.azurecr.io --ports 5000`
