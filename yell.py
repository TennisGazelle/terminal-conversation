#!/usr/bin/python3
import csv
import time
import subprocess

with open('test.csv', 'r') as f:
    lines = csv.reader(f)

    for row in lines:
        if row[0]:
            subprocess.call('figlet -c -k {}'.format(row[0]).split())
        time.sleep(float(row[1]))