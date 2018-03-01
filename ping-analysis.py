#!/usr/bin/env python3
import datetime

failures = {}

with open("/etc/ping/pings.txt", "r") as pings:
	for ping in pings:
		tokens = ping.rstrip().split(" ")
		if(len(tokens) == 4):
			timeStr = tokens[2] + " " + tokens[3]
			timeFormat = "%Y-%m-%d %H:%M:%S.%f"
			timestamp = datetime.datetime.strptime(timeStr, timeFormat)
			if(timestamp not in failures):
				failures[timestamp] = []
			failures[timestamp].append(tokens[0])

print(failures)