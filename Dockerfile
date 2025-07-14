FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

COPY Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip && pip install pipenv && pipenv install --deploy --system

COPY . /app/

RUN apt-get update && apt-get install -y netcat-openbsd
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]