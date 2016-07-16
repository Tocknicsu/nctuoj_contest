#!/bin/bash
ls /nctuoj_contest_web
if [ ! -e "/nctuoj_contest_web" ]; then
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash
    . /root/.nvm/nvm.sh
    nvm install v6.3.0
    git clone https://github.com/allenwhale/nctuoj_contest_web.git
else
    cd /nctuoj_contest_web
    git pull --rebase
    . /root/.nvm/nvm.sh
fi
cd /nctuoj_contest_web
nvm use 6.3.0
npm install
rm dist/*
npm run build
cp dist/* /mnt/oj_web
sh


