# INSTALL DOCKER
    - ./docker.sh

# BUILD DOCKER IMAGE
    - docker build -t db -f contest_psql.Dockerfile ..
    - docker build -t api -f contest_api.Dockerfile .

# RUN DOCKER
    - docker run -itd --name db -e POSTGRES_PASSWORD=nctuoj_contest -e POSTGRES_USER=nctuoj_contest -e POSTGRES_DB=nctuoj_contest -P db
    - docker run -it --name api --link db:db -e DB_HOST=db -e DB_PORT=5432 -e DB_USER=nctuoj_contest -e DB_NAME=nctuoj_contest -e DB_PASSWORD=nctuoj_contest -e PORT=3019 api

# GET CONTAINER IP
    - docker inspect -f "{{.NetworkSettings.Networks.bridge.IPAddress}}" <container name>
