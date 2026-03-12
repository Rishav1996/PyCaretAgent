# GCP Deployment Guide
1. Authenticate gcloud.
2. Build & Tag: `gcloud builds submit --tag gcr.io/[PROJECT_ID]/apple-sales-forecasting`
3. Deploy to Cloud Run: `gcloud run deploy --image gcr.io/[PROJECT_ID]/apple-sales-forecasting`
