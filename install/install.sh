#!/usr/bin/env bash
echo "Blume Installer"
echo "-------------------------"
echo "Installing BlumeHome"

echo "Installing Python"
sudo apt-get install python3
sudo apt-get install python3-pip

echo "Installing Pip Libs"
sudo python3 -m pip install requests
sudo python3 -m pip install flask

echo "Installing Bluetooth"
sudo apt-get install bluetooth libbluetooth-dev
sudo python3 -m pip install pybluez

echo "Editing Hostname"
sudo cp /etc/hostname /etc/hostname_backup
echo "echo BlumeDevice > /etc/hostname " | sudo bash
sudo hciconfig hci0 name 'BlumeDevice'

echo "Creating User"
sudo adduser --disabled-password --gecos "" blume
sudo echo "blumeIOTRulez" | sudo passwd --stdin linuxuser

echo "Downloading Code"
sudo git clone https://github.com/SamHDev/BlumeHomeCore.git /home/blume/code/

echo "Creating Service"