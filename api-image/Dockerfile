FROM python:3.11-slim

WORKDIR /app

COPY main.py validate_peptide.py .

RUN pip install fastapi uvicorn prometheus-fastapi-instrumentator

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

