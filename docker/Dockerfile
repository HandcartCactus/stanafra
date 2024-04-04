FROM tiangolo/uvicorn-gunicorn:python3.11

ARG DB_CONNECTION
ARG MODE

ENV SQLALCHEMY_DATABASE_URI=${DB_CONNECTION}
ENV MODE=${MODE}

COPY ./backend/stanafra/requirements/base.txt .
RUN pip install -r base.txt

COPY ./backend/stanafra/scripts /app
COPY ./backend/stanafra/stanafra /app
WORKDIR /app
