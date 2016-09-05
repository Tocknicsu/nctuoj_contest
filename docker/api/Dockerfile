FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt -y update && apt -y upgrade
RUN apt -y install git 
RUN apt -y install \
        build-essential \
        python3 \
        python3-pip \
        postgresql-client \
        libpq-dev \
        && apt clean \
        && apt autoclean \
        && apt autoremove 
RUN pip3 install --upgrade pip
COPY contest.sh ./contest.sh
ENV PORT=3019
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_USER=nctuoj_contest
ENV DB_NAME=nctuoj_contest
ENV DB_PASSWORD=nctuoj_contest
ENV JUDGE_TOKEN=judgetoken
ENV SB_TOKEN=sbtoken
VOLUME ["/mnt/oj/"]
EXPOSE $PORT
ENTRYPOINT ["bash", "contest.sh"]
