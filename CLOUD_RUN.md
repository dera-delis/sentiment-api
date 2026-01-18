# Cloud Run Deployment

Deployed service:
- Base URL: `https://sentiment-api-742824180889.us-central1.run.app`
- Docs: `https://sentiment-api-742824180889.us-central1.run.app/docs`

## Build (Cloud Build)
Configure a trigger that builds the Dockerfile and publishes to Artifact Registry:

Image destination:
```
us-central1-docker.pkg.dev/sentiment-api-484716/sentiment-api/sentiment-api:$COMMIT_SHA
```

## Deploy (Cloud Run)
1. **Cloud Run → Create Service**
2. Container image: use the latest digest from Artifact Registry
3. Memory: **1–2 GB**
4. Port: **8000**
5. Allow unauthenticated: **Yes**

## Verify
- `GET /health`
- `POST /analyze`

