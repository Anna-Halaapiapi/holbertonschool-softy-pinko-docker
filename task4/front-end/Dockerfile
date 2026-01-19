# base on the latest nginx (static web server)
FROM nginx:latest

# copy softy-pinko-front-end files to /var/www/html/softy-pinko-front-end on the Docker image
COPY softy-pinko-front-end /var/www/html/softy-pinko-front-end

# copy Nginx config file to /etc/nginx/conf.d/default.conf on the Docker image
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf



