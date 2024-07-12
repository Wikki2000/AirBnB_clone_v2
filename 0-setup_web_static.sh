#!/usr/bin/env bash
# sets up a web server for the deployment of web_static projects

# Install Nginx if it not already installed
if [ ! -e /usr/sbin/nginx ]; then
        apt-get update
        apt-get -y install nginx
        echo "Nginx installed successfully."
else
        echo "Nginx is already installed."
fi

# Create the rquired directory and sub-directory
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

test_html_file="<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <p>This is a test html file.</p>
</body>
<html>"
echo "$test_html_file" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

#  change the ownership for the specified directory and all of its subdirectories and files.
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
