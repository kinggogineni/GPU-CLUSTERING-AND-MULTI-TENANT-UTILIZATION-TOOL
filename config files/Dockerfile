# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY cpu_allocator.py /app
RUN pip install psutil

CMD ["python", "cpu_allocator.py"]

