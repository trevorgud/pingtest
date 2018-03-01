#!/usr/bin/env python3
import os
import datetime

hostnames = ["8.8.8.8", "google.com", "208.67.222.222"]
currentTime = datetime.datetime.now()
failed = False

for host in hostnames:
    response = os.system("ping -c 1 " + host)
    if(response != 0):
        failed = True
        with open("/etc/ping/pings.txt", "a") as pings:
            pings.write(host + " failed " + str(currentTime) + "\n")

if(failed):
    with open("/etc/ping/pings.txt", "a") as pings:
        pings.write("==========================\n")