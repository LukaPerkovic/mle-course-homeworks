FROM python:3.10-slim
EXPOSE 5000
COPY . .
RUN apt-get update && \
    python -m pip install -r requirements.txt