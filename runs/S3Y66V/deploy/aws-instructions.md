# AWS Deployment Guide

1. Login to ECR:
   `aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com`
2. Create repository:
   `aws ecr create-repository --repository-name student-productivity-api`
3. Tag image:
   `docker tag student-productivity-api:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/student-productivity-api:latest`
4. Push image:
   `docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/student-productivity-api:latest`
5. Deploy on ECS/Fargate using the pushed image.
