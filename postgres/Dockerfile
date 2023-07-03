FROM postgis/postgis:14-3.3
RUN apt-get update && apt-get -y install postgresql-14-cron
COPY runtime /
ENV POSTGRES_PASSWORD=electric
USER postgres