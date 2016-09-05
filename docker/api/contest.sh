if [ ! -d "/nctuoj_contest" ]; then
    set -e
    cd /
    git clone https://github.com/Tocknicsu/nctuoj_contest.git
    cd /nctuoj_contest/backend
    cp config.py.sample config.py
    echo "DB_SETTING['dsn'] = 'dbname=${DB_NAME} user=${DB_USER} password=${DB_PASSWORD} host=${DB_HOST} port=${DB_PORT}'" >> config.py
    echo "JUDGE_TOKEN = '${JUDGE_TOKEN}'" >> config.py
    echo "SB_TOKEN = '${SB_TOKEN}'" >> config.py
    cd /nctuoj_contest
    pip3 install --upgrade -r requirements.txt
else
    cd /nctuoj_contest
    git pull --rebase
    pip3 install --upgrade -r requirements.txt
fi
cd /nctuoj_contest/backend
python3 server.py
