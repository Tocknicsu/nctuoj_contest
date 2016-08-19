# Install docker 
`curl -sSL https://get.docker.com/ | sudo sh`

# Install nginx ( for load balance )
`sudo apt-get install nginx`

# Add user to use docker
`sudo usermod -aG docker username`
+   Relogin then you can use docker free.

# Have your own copy

`git clone https://github.com/Tocknicsu/nctuoj_contest.git`

# Enter the folder

`cd nctuoj_contest/docker`

# Initial the configuation

`cp config.json.sample config.json`

# Edit `config.json`

+   `prefix` indicates the prefix of the names of the images
    +   Will create `prefix_web`, `prefix_db`, `prefix_judge_i`, and `prefix_api_i`.
+   `DB` for the database
    +   `POSTGRES_USER`: user name
    +   `POSTGRES_DB`: db name
    +   `POSTGRES_PASSWORD`: db password
+   `api` for the images of the application interface
    +   `number`: number of server instances
    +   `DATA_ROOT`: place for the shared data pool
+   `web`
    +   `BASE_URL`: URL of the api server (Don't use `http://localhost`! Use your network interface if you are running the judge system locally)
    +   `DATA_ROOT`: folder for storing web data
+   `judge`
    +   `number`: number of server instances
    +   `BASE_URL`: URL of the api server (Don't use `http://localhost`! Use your network interface if you are running the judge system locally)
+   `judgetoken`: use `"token"` for now.


# Build the judge system

## Build docker images
`./build.py -images`

## Build database
`./build.py -db`

## Build api
`./build.py -api`

## Build judge
`./build.py -judge`

## Check the configuration
`./build.py -config`

+   The first IP is db, and following IPs are instances of the api server. 
+   You might have to wait for 2 - 3 minutes until docker installed lots of thing.
+   If the IP of some api server is 172.17.0.3, then use `curl 172.17.0.3:3019/api/users/` to check if the api server is activated.
    +   You should see `{"msg": [{"type": 0, "name": "admin", "id": 1, "account": "admin"}]}` if the server is setup properly.

# Build web
`./build.py -web`
+   This step will take lots of time
    +   Use `docker attach contest_web` to monitor the installation progress if you didn't change the prefix in `config.json`.
    +   Hold <kbd>Ctrl</kbd> then press <kbd>P</kbd>, then press <kbd>Q</kbd> to detach the container.

# Setup `nginx`
`cp nginx.setting /etc/nginx/sites-enabled/default`
`sudo service nginx restart`

# Done!
If everyhing works properly, then you may go to `BASE_URL` (depends on what you set in `config.json`) and login account `admin` with password `admin` after all iamges start.