FROM python:3.8.3-alpine

RUN mkdir -p /app

COPY ./app /app

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

RUN apk add curl
RUN apk add bash
# Install Poetry

# Copy poetry.lock* in case it doesn't exist in the repo

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80"]

