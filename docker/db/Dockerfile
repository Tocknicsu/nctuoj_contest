FROM postgres:9.5
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ADD https://raw.githubusercontent.com/Tocknicsu/nctuoj_contest/master/psql.sql /docker-entrypoint-initdb.d/psql.sql
