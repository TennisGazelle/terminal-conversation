#!/usr/bin/python3
import csv
import time
import subprocess

with open('test.csv', 'r') as f:
    lines = csv.reader(f)

    default_font = 'standard'

    for row in lines:
        font = default_font
        if len(row) > 2 and row[2] is not '':
            font = row[2]
        if row[0]:
            subprocess.call('figlet -w 120 -ckf {} {}'.format(font, row[0]).split())
        if row[1] is not '':
            time.sleep(float(row[1]))
        subprocess.call(['clear'])        