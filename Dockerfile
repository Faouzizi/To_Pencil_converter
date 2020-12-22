FROM python:3.7-slim

COPY requirements.txt /app/
WORKDIR /app

RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org --requirement requirements.txt \
    && apt-get update \
    && apt-get install -y openssh-client
EXPOSE 5001
COPY . .
CMD ["python", "main.py"]