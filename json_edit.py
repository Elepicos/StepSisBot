import json
from pathlib import Path

def add(characteristic, guildIdentity, value):
    with open("./data/guilds-info.json", "r+") as inf:
        data = json.load(inf)
        for item in data["guilds"]:
            if item["guildID"] == guildIdentity:
                item[characteristic].append(value)
            print(json.dumps(data, indent=4))
        inf.seek(0)
        json_obj = json.dumps(data, indent = 4)
        inf.write(json_obj)   

def remove(characteristic, guildIdentity, index):
    with open("./data/guilds-info.json", "r+") as inf:
        data = json.load(inf)
        for item in data["guilds"]:
            if item["guildID"] == guildIdentity:
                item[characteristic].pop(index)
            print(json.dumps(data, indent=4))

def change(characteristic, guildIdentity, value):
    with open("./data/guilds-info.json", "r+") as inf:
        data = json.load(inf)
        for item in data["guilds"]:
            if item["guildID"] == guildIdentity:
                item[characteristic] = value
            print(json.dumps(data, indent=4))