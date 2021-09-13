#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static, parameters:
# Port 80, Permanent redirection /redirect_me. ,Use custom 404 error page, Custom header X-Served-By and Prepare server to deploy

# Install NGINX
sudo apt-get update
sudo apt-get install -y nginx
# --> Create forlders
sudo mkdir -p /data/web_static/{releases/test,shared}
# --> Create default page
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
# --> Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# --> Change ownership
sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data
# Configurate server
sudo ufw allow 'Nginx HTTP'
f_config="/etc/nginx/sites-available/default"
# Add header
sudo sed -i "/listen 80 default_server/a add_header X-Served-By \"$HOSTNAME\";" $f_config
# --> Add alias
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' $f_config
# Create default page
sudo rm /var/www/html/*
sudo echo "Holberton School for the win!" | sudo tee /var/www/html/index.html
# Add redirection
new_site="https://www.youtube.com/watch?v=QH2-TGUlwu4"
sudo sed -i "/listen 80 default_server/a rewrite ^/redirect_me $new_site permanent;" $f_config
# Add 404 redirection
sudo echo "Ceci n'est pas une page" | sudo tee /usr/share/nginx/html/error404.html
error404="error404.html"
l_error404="/error404.html {root /usr/share/nginx/html;\n internal;}"
sudo sed -i "/listen 80 default_server/a error_page 404 /$error404; location = $l_error404" $f_config
# Restart server
sudo service nginx restart
