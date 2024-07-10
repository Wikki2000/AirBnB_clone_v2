#!/usr/bin/env bash
# sets up a web server for the deployment of web_static projects

# Install Nginx if it not already installed
apt-get update
apt-get install -y nginx

# Create the folder /data/web_static/releases/test/ and parent folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

# change onwerships and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By \$HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 https://youtube.com/;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}" > /etc/nginx/sites-available/default

service nginx restart
