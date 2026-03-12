# GCP Deployment Guide
1. Auth: `gcloud auth configure-docker`
2. Tag: `docker tag amazon-clustering-app:latest gcr.io/<project_id>/amazon-clustering:latest`
3. Push: `docker push gcr.io/<project_id>/amazon-clustering:latest`
4. Deploy to Cloud Run: `gcloud run deploy --image gcr.io/<project_id>/amazon-clustering:latest`
