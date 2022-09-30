FROM python:3.8-slim
COPY sklearn_regressor/ sklearn_regressor/ 
WORKDIR /sklearn_regressor
RUN apt-get update && \
    apt-get install -y git && \
    python -m pip install -r requirements.txt
