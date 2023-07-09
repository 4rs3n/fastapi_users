FROM postgres:15.3-bullseye

RUN apt update -y
RUN apt upgrade -y
RUN apt install nfs-common -y

# ENV POSTGRES_USER=admin
# ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=user_db

COPY postgres_schema.sql /docker-entrypoint-initdb.d
COPY user_db_postgres.conf /etc/postgresql/postgresql.conf

EXPOSE 5432