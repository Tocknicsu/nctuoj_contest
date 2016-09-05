#!/bin/bash
set -e
echo "sb_token = '$SB_TOKEN'" >> config.py
echo "base_url = '$BASE_URL'" >> config.py
pip3 install --upgrade requests
python3 tick.py
