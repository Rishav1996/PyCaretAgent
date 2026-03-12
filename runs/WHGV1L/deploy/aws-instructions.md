# AWS Deployment
1. Login to ECR: `aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <id>.dkr.ecr.<region>.amazonaws.com`
2. Create repo: `aws ecr create-repository --repository-name placement-model`
3. Tag: `docker tag placement-model:latest <id>.dkr.ecr.<region>.amazonaws.com/placement-model:latest`
4. Push: `docker push <id>.dkr.ecr.<region>.amazonaws.com/placement-model:latest`
5. Deploy using ECS/Fargate.
