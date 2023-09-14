#!/bin/sh

sudo sed -i 's/FA21-ICA4/RIGHT/g' /etc/hosts
sudo sed -i 's/FA21-ICA4/RIGHT/g' /etc/hostname
sudo sed -i -e '$aauto enp0s8' /etc/network/interfaces
sudo sed -i -e '$aiface enp0s8 inet static' /etc/network/interfaces
sudo sed -i -e '$aaddress 192.168.100.3' /etc/network/interfaces
sudo sed -i -e '$anetmask 255.255.255.0' /etc/network/interfaces

sudo reboot
