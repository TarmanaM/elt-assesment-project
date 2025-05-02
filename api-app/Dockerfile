FROM python:3.11-slim

WORKDIR /app

COPY api-app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api-app .

CMD ["python", "run.py"]
