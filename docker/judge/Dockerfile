FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install curl gcc g++ python python3 git 
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN apt-get -y upgrade
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y --force-yes --no-install-recommends install oracle-java8-installer
RUN apt-get clean
RUN apt-get autoclean
RUN apt-get autoremove
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD judge.sh /judge.sh
ENTRYPOINT ["bash"]
