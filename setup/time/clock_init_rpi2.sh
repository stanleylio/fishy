#!/bin/bash
# schedule this to run on boot to set system clock using the DS1307 RTC

sleep 2

echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device

# for debugging
#log="/root/ds1307.txt"
#log="/root/setup/time/clock_init.log"

date

echo "rtc (rpi):"
hwclock --show -f /dev/rtc

echo "rtc0 (ds1307/ds3231):"
hwclock --show -f /dev/rtc0

# from DS1307 to system time
hwclock --hctosys -f /dev/rtc0

# from system time to BBB's rtc
hwclock --systohc -f /dev/rtc
