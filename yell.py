#!/usr/local/bin/python3
import csv
import time
import subprocess

# script = 'sister-was-a-witch.csv'
# script = 'someone-broke-into-house.csv'
script = 'this-is-for-rachel.csv'

speed_multiplier = 1

with open(script, 'r') as f:
    lines = csv.reader(f)

    default_font = 'standard'

    for row in lines:
        font = default_font
        if len(row) > 2 and row[2] is not '':
            font = row[2]
        if row[0]:
            subprocess.call('figlet -w 120 -ckf {} {}'.format(font, row[0]).split())
        if len(row) < 2:
            print('no time listed, making estimate')
            wait_time = .05 * len(row[0])
            time.sleep(wait_time)
        elif row[1] is not '':
            time.sleep(float(row[1]) * speed_multiplier)
        subprocess.call(['clear'])