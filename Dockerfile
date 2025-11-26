FROM python:3.9-slim
WORKDIR /app
COPY src/ /app/
ENTRYPOINT ["python3", "todo.py"]

