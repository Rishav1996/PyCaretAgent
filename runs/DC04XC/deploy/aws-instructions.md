# AWS Deployment Instructions
1. Login to ECR: `aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <id>.dkr.ecr.<region>.amazonaws.com`
2. Create repository: `aws ecr create-repository --repository-name mango-anomaly`
3. Tag: `docker tag mango-anomaly-api:latest <id>.dkr.ecr.<region>.amazonaws.com/mango-anomaly:latest`
4. Push: `docker push <id>.dkr.ecr.<region>.amazonaws.com/mango-anomaly:latest`
5. Deploy on ECS/Fargate using the ECR image URI.
