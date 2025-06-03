FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY server2fa.py .
COPY fonctions.py .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "server2fa:app"]