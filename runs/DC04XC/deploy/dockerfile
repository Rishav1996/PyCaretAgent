FROM python:3.11-slim
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "deploy:app", "--host", "0.0.0.0", "--port", "5000"]
