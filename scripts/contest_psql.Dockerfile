FROM postgres:9.5
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ADD ./psql.sql /docker-entrypoint-initdb.d/psql.sql
