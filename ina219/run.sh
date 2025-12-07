#!/bin/sh
echo "Starting INA219 reader...."

while true; do
    python3 /app/ina219.py
    sleep 2
done
