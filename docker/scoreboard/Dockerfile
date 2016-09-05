FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt -y update && apt -y upgrade
RUN apt -y install python3
RUN apt -y install python3-pip
RUN apt clean
RUN apt autoclean
RUN apt autoremove
RUN pip3 install --upgrade pip
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD config.py.sample /config.py
ADD tick.py /tick.py
ADD sb.sh /sb.sh
ENV SB_TOKEN=sbtoken
ENV BASE_URL=https://contest.oj.nctu.me/
ENTRYPOINT ["bash", "/sb.sh"]
