#!/usr/bin/env bash
# Bash script that setups the web servers for the deployment of web_static

ADD_WEBSTATIC="\\\tlocation /hbnb_static/ {\n\t\talias/data/web_static/current/;\n\t}\n"

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test to see if Nginx is working" | sudo tee /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current
# linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, delete and recreate it.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership /data/ folder to ubuntu user & group
sudo chown -hR ubuntu:ubuntu /data/
# Update nginx config to serve /data/web_static/curent
# Restart nginx
sudo sed -i "35i $ADD_WEBSTATIC" /etc/nginx/sites-available/default
sudo service nginx start
