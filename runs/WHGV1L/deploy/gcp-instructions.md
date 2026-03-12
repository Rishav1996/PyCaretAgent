# GCP Deployment
1. Configure gcloud: `gcloud auth configure-docker`
2. Tag: `docker tag placement-model:latest gcr.io/<PROJECT_ID>/placement-model:latest`
3. Push: `docker push gcr.io/<PROJECT_ID>/placement-model:latest`
4. Deploy on Cloud Run.
