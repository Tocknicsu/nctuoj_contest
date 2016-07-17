#!/bin/bash
set -e
if [ ! -e "/nctuoj_contest_web" ]; then
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash
    . /root/.nvm/nvm.sh
    nvm install v6.3.0
    git clone https://github.com/allenwhale/nctuoj_contest_web.git
    cd /nctuoj_contest_web
    awk '{new=$0; print old; old=new}END{print "Config.baseUrl = \"'"$BASE_URL"'\""; print old}' src/js/utils/Config.js > /tmp/Config.js
    cp /tmp/Config.js src/js/utils/Config.js
else
    cd /nctuoj_contest_web
    git pull --rebase
    . /root/.nvm/nvm.sh
fi
cd /nctuoj_contest_web
nvm use 6.3.0
npm install
npm run build
cp dist/* /mnt/oj_web
sh


