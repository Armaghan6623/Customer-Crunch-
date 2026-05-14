# Customer Churn Deployment

Starter project scaffold for deploying a customer-churn ML model.

## Structure
- `src/`: Flask app and inference utilities
- `docker/`: Dockerfile
- `terraform/`: Terraform IaC (placeholder)
- `scripts/`: local validation scripts (placeholder)

## Quick start (local)
1. Build and run the container:
   ```bash
   docker build -t churn-app ./docker
   docker run -p 8080:8080 churn-app
   ```
2. Call health endpoint:
   ```bash
   curl http://localhost:8080/health
   ```

