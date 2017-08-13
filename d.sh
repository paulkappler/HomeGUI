#!/bin/bash

chmod 666 /sys/class/backlight/rpi_backlight/bl_power
chmod 666 /sys/class/backlight/rpi_backlight/brightness
echo 20 > /sys/class/backlight/rpi_backlight/brightness
echo 1 > /sys/class/backlight/rpi_backlight/brightness

while [ 1 ]
do
     sleep 1h
done
