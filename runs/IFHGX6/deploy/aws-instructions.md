# AWS Deployment Guide
1. Login: `aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com`
2. Create Repo: `aws ecr create-repository --repository-name amazon-clustering`
3. Tag: `docker tag amazon-clustering-app:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/amazon-clustering:latest`
4. Push: `docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/amazon-clustering:latest`
5. Deploy to ECS/Fargate.
