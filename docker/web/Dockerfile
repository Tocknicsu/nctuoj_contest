FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt -y update && apt -y upgrade
RUN apt -y install \
        build-essential \
        curl \
        git \
        wget \
        && apt clean \
        && apt autoclean \
        && apt autoremove 
RUN git clone https://github.com/allenwhale/nctuoj_contest_web.git
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash
RUN /bin/bash -c "source /root/.nvm/nvm.sh && \
        nvm install v6.3.0 && \
        nvm use v6.3.0 && \
        cd /nctuoj_contest_dist && \
        npm install && \
        npm run build"
VOLUME ["/nctuoj_contest_web/dist/"]
ENTRYPOINT ["bash"]
