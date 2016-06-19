if [ ! -d "/nctuoj_contest" ]; then
    set -e
    if [ "$DOCKERHOST" = "" ]; then
        DOCKERHOST="172.17.0.1";
    fi
    if [ "$DB_HOST" = "" ]; then
        DBHOST="$DOCKERHOST";
    fi
    if [ "$DB_USER" = "" ]; then
        DBUSER="postgres";
    fi
    if [ "$DB_PORT" = "" ]; then
        DBPORT="5432";
    fi
    if [ "$PORT" = "" ]; then
        PORT="3019";
    fi
    if [ "$DB_NAME" = "" ]; then
        DBNAME="$DB_USER";
    fi
    cd /
    git clone https://github.com/Tocknicsu/nctuoj_contest.git
    cd /nctuoj_contest/backend
    cp config.py.sample config.py
    echo "DB_SETTING['dsn'] = 'dbname=${DB_NAME} user=${DB_USER} password=${DB_PASSWORD} host=${DB_HOST} port=${DB_PORT}'" >> config.py
    cd /nctuoj_contest
    pip3 install --upgrade -r requirements.txt
else
    cd /nctuoj_contest
    git pull --rebase
    pip3 install --upgrade -r requirements.txt
fi
cd /nctuoj_contest/backend
python3 server.py
