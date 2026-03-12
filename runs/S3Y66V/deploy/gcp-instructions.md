# GCP Deployment Guide

1. Configure gcloud:
   `gcloud auth configure-docker`
2. Tag image:
   `docker tag student-productivity-api gcr.io/<project_id>/student-productivity-api:latest`
3. Push image:
   `docker push gcr.io/<project_id>/student-productivity-api:latest`
4. Deploy on Cloud Run:
   `gcloud run deploy --image gcr.io/<project_id>/student-productivity-api:latest --platform managed`
