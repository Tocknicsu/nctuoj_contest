FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt -y update && apt -y upgrade
RUN apt -y install git
RUN apt -y install curl
RUN apt -y install \
        wget \
        && apt clean \
        && apt autoclean \
        && apt autoremove 
VOLUME ["/mnt/oj_web/"]
COPY web.sh ./web.sh
ENTRYPOINT ["bash", "web.sh"]
