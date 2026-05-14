---
title: Customer Churn Prediction API
emoji: 📉
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 7860
---

# Customer Churn Prediction (Docker / Hugging Face Spaces)

A small Flask API for predicting customer churn probability.

## Local run
```bash
docker build -t churn-app ./docker
docker run -p 7860:7860 churn-app
```

## Endpoints
- `GET /health`
- `POST /predict` with JSON: `{ "customer_id": 123 }`

