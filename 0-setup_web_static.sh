#!/usr/bin/env bash
# Bash script that setups the web servers for the deployment of web_static

if ! [ -x "$(command -v nginx)" ]; then
   sudo apt-get -y update
   sudo apt-get install -y nginx
fi

if [ ! -d "/data" ]; then
  mkdir /data
fi

if [ ! "/data/web_static" ]; then
  mkdir /data/web_static
fi

if [ ! "/data/web_static/releases" ]; then
  mkdir /data/web_static/releases
fi

if [ ! "/data/web_static/shared" ]; then
  mkdir /data/web_static/shared
fi

if [ ! "/data/web_static/releases/test" ]; then
  mkdir /data/web_static/releases/test/
fi

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current
#linked to the /data/web_static/releases/test/ folder.
# If the symbolic link already exists, delete and recreate it.
if [ -L "/data/web_static/current" ]; then
  rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/
/data/web_static/current

# Give ownership /data/ folder to ubuntu user & group
chown -R ubuntu:ubuntu /data

# Update nginx config to serve /data/web_static/curent
# Restart nginx
echo "
server {
  listen 80;
  server_name localhost;

  location /hbnb_static {
    alias /data/web_static/current/;
  }
}" > /etc/nginx/sites-available/default
sudo service nginx restart

exit 0
