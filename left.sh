#!/bin/sh

sudo sed -i 's/FA21-ICA4/LEFT/g' /etc/hosts
sudo sed -i 's/FA21-ICA4/LEFT/g' /etc/hostname
sudo sed -i -e '$aauto enp0s8' /etc/network/interfaces
sudo sed -i -e '$aiface enp0s8 inet static' /etc/network/interfaces
sudo sed -i -e '$aaddress 192.168.00.2' /etc/network/interfaces
sudo sed -i -e '$anetmask 255.255.255.0' /etc/network/interfaces

sudo reboot
