FROM python:3.12-slim

WORKDIR /work
COPY app/ app/

CMD ["python", "app/main.py"]
