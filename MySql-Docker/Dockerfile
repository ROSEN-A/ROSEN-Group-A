FROM mysql/mysql-server

ENV MYSQL_DATABASE=rosendb \
    MYSQL_ROOT_PASSWORD=password \
    MYSQL_ROOT_HOST=%

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306
