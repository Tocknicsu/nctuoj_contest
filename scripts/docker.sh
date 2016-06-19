#!/bin/sh
wget -qO- https://get.docker.com/ | sudo sh
sudo usermod -aG docker $(whoami)
