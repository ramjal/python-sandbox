import os
import json

jsonFile = os.path.join(os.getcwd(), 'birthday.json')

with open(jsonFile, "r") as f:
    info = json.load(f)


info["Shahin Jalali"] = "24Apr1964"


with open(jsonFile, "w") as f:
    json.dump(info, f)