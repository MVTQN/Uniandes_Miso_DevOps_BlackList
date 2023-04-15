FROM python:3.10-slim

WORKDIR /app

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y libpq-dev gcc && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev

RUN pip install pipenv psycopg2

COPY Pipfile Pipfile.lock ./

RUN pipenv install

COPY . .

RUN ["chmod", "+x", "./deploy.sh"]

EXPOSE 3000

ENTRYPOINT ["./deploy.sh"]