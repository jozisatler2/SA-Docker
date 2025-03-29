#!/bin/bash

# network
sudo docker network create net

# server
sudo docker build . -t server_image -f Dockerfile-server
sudo docker run -d --name server --device=/dev/video0 -p 5000:5000 --network net server_image

# client
sudo docker build . -t client_image -f Dockerfile-client
sudo docker run -d --name client -p 5001:5001 --network net client_image

# izpis ip-ja
echo "Odjemalec:"
sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' client
echo "Dostopen na portu 5001"
