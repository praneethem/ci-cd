FROM python:3.9-slim

WORKDIR /app

COPY src/ /app/

CMD ["python3", "todo.py"]


