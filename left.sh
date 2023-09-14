#!/bin/sh

echo LEFT > /etc/hostname
echo auto enp0s8 >> /etc/network/interfaces
echo iface enp0s8 inet static >> /etc/network/interfaces
echo address 192.168.100.2 >> /etc/network/interfaces
echo netmask 255.255.255.0 >> /etc/network/interfaces
sed -i 's/FA21-ICA4/LEFT/g' /etc/hosts
