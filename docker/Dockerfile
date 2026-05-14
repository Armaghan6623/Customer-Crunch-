FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app
COPY src /app/src

# Flask via Gunicorn
EXPOSE 7860
ENV PORT=7860

CMD ["gunicorn", "src.app:app", "--bind", "0.0.0.0:7860", "--workers", "2", "--threads", "4"]


