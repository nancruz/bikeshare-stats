#!/bin/bash

BIKE_SHARE_STATIONS_ENDPOINT="https://lisboa.city-platform.com/maps/wfs?SERVICE=wfs&REQUEST=GetFeature&VERSION=2.0.0&typeNames=emel_gira_stations&srsName=EPSG:4326&outputFormat=application/json"
CURRENT_TIMESTAMP=$(date '+%s')
FILE_NAME="stations-$CURRENT_TIMESTAMP.json"
FILE_PATH="."

if [ -n "$1" ] ; then FILE_PATH="$1"; fi

if [ ! -d "$FILE_PATH" ]; then
echo "Path not found"
exit 1
fi

curl $BIKE_SHARE_STATIONS_ENDPOINT -o "$FILE_PATH/$FILE_NAME"
