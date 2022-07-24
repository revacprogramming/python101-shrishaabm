# Tuples
import re
filename = "../dataset/mbox-short.txt"
fhandle = open(filename, 'r')
hours = []
count = dict()
for line in fhandle:
    if line.startswith('From '):
        time = re.findall(r"[\d]+:[\d]+:[\d]+", line)
        print(time[0][:2])