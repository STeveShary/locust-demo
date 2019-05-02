FROM mysql:5.7

ENV MYSQL_ALLOW_EMPTY_PASSWORD true

COPY ./data/ /docker-entrypoint-initdb.d/
