```
# install docker 
curl -sSL https://get.docker.com/ | sudo sh

# install nginx ( for load balance )
sudo apt-get install nginx

# add user to use docker
sudo usermod -aG docker username

# relogin and you can use docker free

git clone https://github.com/Tocknicsu/nctuoj_contest.git

cd nctuoj_contest/docker

# setting config.py
cp config.json.sample config.json

### DB, api, judge will always run at backend
### web will run just once and generate some file

### prefix: for docker name prefix
###         default is contest, so the docker container name will be contest_db, contest_api_0, etc.
### DB: setting username, password and database name
### api: 
###     number: how many api server 
###     DATA_ROOT: which folder to store data
### web:
###     BASE_URL: where is api server
###     DATA_ROOT: 
### 
### judge:
###     number: how many judge
###     BASE_URL: where is api server
### judgetoken: to avoid fake judge (not implement, it should be set to "token")

# build docker images
./build.py -images

# build db
./build.py -db

# build api
./build.py -api

./build.py -config

### first ip is db, and following four ip are apis
### if one of those apis is 172.17.0.3
### wait the docker 2 - 3 minutes to install lots of thing
wget 172.17.0.3:3019/api/users
### you should see {"msg": [{"type": 0, "name": "admin", "id": 1, "account": "admin"}]}

# build web
./build.py -web
# go into the container
# this step will take lots of time
docker attach contest_web

# <kbd>Ctrl+P</kbd>, <kbd>Ctrl+Q</kbd> detach the container

cp nginx.setting /etc/nginx/sites-enabled/default
sudo service nginx restart

```
