# Python 3.9 use karte hain
FROM python:3.9-slim

# Working directory set karo
WORKDIR /app

# System dependencies install karo
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Requirements copy aur install karo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Poora project copy karo
COPY . .

# Port expose karo
EXPOSE 5000

# Verify script run karo aur phir app start karo
CMD python verify.py && python app.py
