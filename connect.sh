#!/bin/bash
# figure out currently connected SSID
ssid=$(iwconfig 2>/dev/null | grep -oE 'ESSID:"[^\"]+')
ssid="${ssid#*\"}"
if [ -z "$ssid" ]; then
    echo "Not connected to any Wifi."
    exit 1
fi
echo "Connected to Wifi: $ssid"
# convert to lower case, replace spaces with underscores
ssidfn="${ssid,,}"
ssidfn="${ssidfn//\ /_}"
# call the corresponding python or shell script
here="${0%/*}"
if [ -f "$here"/"$ssidfn".py ]; then
    "$here"/"$ssidfn".py -v
elif [ -f "$here"/"$ssidfn".sh ]; then
    "$here"/"$ssidfn".sh -v
else
    echo "Unsupported SSID: $ssid"
    exit 1
fi
