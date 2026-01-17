# Northflank Deployment Guide

This service is designed to run on Northflank using the repository build workflow.

## Prerequisites
- A Northflank account
- GitHub repo: `https://github.com/dera-delis/sentiment-api`

## Deploy From GitHub
1. **Create a Project** in Northflank.
2. Click **Create Service** → **Build from Git**.
3. Connect your GitHub account and select `dera-delis/sentiment-api`.
4. **Build settings**
   - **Build type**: Dockerfile
   - **Dockerfile path**: `Dockerfile`
   - **Build context**: repository root
5. **Networking**
   - **Container port**: `8000`
   - **Health check path**: `/health`
6. Click **Deploy**.

## Verify
- `GET https://<service-url>/health`
- `POST https://<service-url>/analyze`

Example request:
```bash
curl -X POST https://<service-url>/analyze \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"I love this product\"}"
```

## Notes
- The container respects the `PORT` environment variable set by Northflank.
- First startup may take a minute while the model downloads.

