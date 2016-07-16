FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt -y update && apt -y upgrade
RUN apt -y install curl gcc g++ python python3 git software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt -y update && apt -y upgrade
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt -y --force-yes --no-install-recommends install oracle-java8-installer
RUN apt clean
RUN apt autoclean
RUN apt autoremove
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD judge.sh /judge.sh
ENTRYPOINT ["bash", "judge.sh"]
