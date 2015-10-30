#!/bin/bash


crontab -l > crontab.txt
cat /etc/network/interfaces > interfaces.txt
cat /etc/hostname > hostname.txt
cat /etc/hosts > hosts.txt
cat /etc/resolv.conf > resolv.conf.txt
cat /etc/rc.local > rc.local.txt
cat /etc/supervisor/supervisord.conf > supervisord.conf


