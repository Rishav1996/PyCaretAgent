# AWS Deployment Guide
1. Create ECR repository.
2. Login to ECR: `aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com`
3. Tag image: `docker tag apple-sales-forecasting:latest <repository_uri>:latest`
4. Push: `docker push <repository_uri>:latest`
5. Create ECS task definition and service for deployment.
