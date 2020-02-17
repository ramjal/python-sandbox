import os
import json
from collections import Counter

jsonFile = os.path.join(os.getcwd(), 'birthday.json')

with open(jsonFile, "r") as f:
    info = json.load(f)

alldays = []
for key in info:
    alldays.append(info[key][2:5])

count = Counter(alldays)

print(count)