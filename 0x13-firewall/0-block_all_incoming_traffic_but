#!/usr/bin/env bash
# Configure UFW to allow HTTP, HTTPS and SSH
echo -e "Running system updates\n"
sudo apt-get update -y

echo -e "Installing UFW\n"
sudo apt-get install ufw -y

sudo ufw default deny in
sudo ufw default allow out

sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 8080/tcp

sudo ufw enable
echo -e "Configuration completed successfully\n"