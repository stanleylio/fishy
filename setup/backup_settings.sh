#!/bin/bash

DIR="./backup"

if ! [ -e "$DIR" ]
then
	mkdir $DIR
fi

rsync -avh /etc/apache2 $DIR
rsync -avh /etc/supervisor $DIR
rsync -avh /etc/logrotate.d $DIR
rsync -avh /etc/rsnapshot $DIR

crontab -l > $DIR/crontab.txt
cp /etc/fstab $DIR/fstab
cp /boot/uEnv.txt $DIR/uEnv.txt
cp -a /etc/network/interfaces $DIR/interfaces.txt
cp -a /etc/hostname $DIR/hostname.txt
cp -a /etc/hosts $DIR/hosts.txt
#cp -a /etc/resolv.conf $DIR/resolv.conf.txt
cat /etc/resolv.conf > $DIR/resolv.conf.txt
cp -a /etc/rc.local $DIR/rc.local.txt
cp -a /etc/ntp.conf $DIR/ntp.conf

if [ -a /etc/wpa_supplicant ]
then
	rsync -avh /etc/wpa_supplicant $DIR
fi

#cp -a /etc/supervisor/supervisord.conf $DIR/supervisord.conf
#cp -a /etc/supervisor/conf.d/sampling.conf $DIR/sampling.conf
