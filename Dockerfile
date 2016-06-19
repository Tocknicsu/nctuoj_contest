FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV PORT=3019
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_USER=nctuoj_contest
ENV DB_NAME=nctuoj_contest
ENV DB_PASSWORD=nctuoj_contest
VOLUME ["/mnt/nctuoj_contest"]
EXPOSE $PORT
RUN apt -y update && apt -y upgrade
RUN apt -y install build-essential curl git wget python3 python3-pip postgresql-server-dev-all \
&& apt clean \
&& apt autoclean \
&& apt autoremove \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip3 install --upgrade pip
COPY contest.sh ./contest.sh
ENTRYPOINT ["bash", "./contest.sh"]
