#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static. It must.

## Install Nginx if it not already installed.
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
## Create the folder.
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
## Create a fake HTML file.
sudo chown -R ubuntu:ubuntu /data/
echo "Holberton School" > /data/web_static/releases/test/index.html
## Create linked.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
