# GCP Deployment Instructions
1. Authenticate: `gcloud auth configure-docker`
2. Tag: `docker tag mango-anomaly-api:latest gcr.io/[PROJECT_ID]/mango-anomaly`
3. Push: `docker push gcr.io/[PROJECT_ID]/mango-anomaly`
4. Deploy: `gcloud run deploy mango-anomaly --image gcr.io/[PROJECT_ID]/mango-anomaly --platform managed`
