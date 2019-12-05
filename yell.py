#!/usr/bin/python3
import csv
import time
import subprocess

with open('test.csv', 'r') as f:
    lines = csv.reader(f)

    for row in lines:
        if row[0]:
            subprocess.call('figlet -c -k {}'.format(row[0]).split())
        if row[1] and row[1] is not '':
            time.sleep(float(row[1]))
        subprocess.call(['clear'])

        