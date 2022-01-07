from os import write
import discord
from discord.ext import commands, tasks
intents = discord.Intents().all()
from commands.json_edit import add, change, remove

import json
from pathlib import Path

with Path("data/config.json").open() as f:
    config = json.load(f)

token = config["token"]
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith('step!'):
        return

    pref_removed = message.content[5:len(message.content)]
    if pref_removed.startswith(" "):
        pref_removed = pref_removed[1:len(pref_removed)]

    command_args = pref_removed.split(" ")

    #Ping command check if active - !ADMIN RESTRICTED!
    if command_args[0] == "ping" and message.author.guild_permissions.administrator:
        await message.channel.send('pong')

    if command_args[0] == "change" and message.author.guild_permissions.administrator:
        try:
            if isinstance(command_args[1], str):
                command_args[1] = command_args[1][1:len(command_args[1])-1]
            print(command_args[1])
            change("time_interval", message.guild.id, command_args[1])
        except:
            print("error")


#{
#"guilds":[
#    {
#    "guildID":"", 
#    "timed_messages":[""], 
#    "reaction_triggers":[""],
#    "reactive_messages":[""],
#    "server_prefix":"",
#    "time_interval":""
#    }
#]
#}
@client.event
async def on_guild_join(guild):
    print("JOINED GUILD")
    add_dict = {
    "guildID":guild.id, 
    "timed_messages":config["default_timed"], 
    "reaction_triggers":config["default_triggers"],
    "reactive_messages":config["default_reactive"],
    "time_interval":config["default_timer"],
    "server_prefix":config["default_prefix"]
    }
    print("generated")
    with open("data/guilds-info.json", "r+") as inf:
        guilds = json.load(inf)
        guilds["guilds"].append(add_dict)
        print(json.dumps(guilds, indent=4))
        inf.seek(0)
        json_obj = json.dumps(guilds, indent = 4)
        inf.write(json_obj)
    
@client.event
async def on_guild_remove(guild):
    with open("data/guilds-info.json", "r+") as inf:
        guilds = json.load(inf)
        index = 0
        for item in guilds["guilds"]:
            if item["guildID"] == guild.id:
                remove_guild = guilds["guilds"].pop(index)
                break
            index+=1
        print(json.dumps(guilds, indent=4))
        inf.seek(0)
        inf.truncate()
        json_obj = json.dumps(guilds, indent = 4)
        inf.write(json_obj)



client.run(token, bot=True, reconnect=True)

#   ACTIVE COMMANDS:
#   ping
#   on guild join/leave update data
#   
#   
#   TO BE WRITTEN:
#   Timed messages
#   Reactive messages
#   Prefix change
#   Add reactive message
#   Add timed message
#   set time difference
#       option to set time random within interval
#   Show all timed messages
#   Show all reactive messages
#   
#   ACTIVE TODO:
#   ADD CUSTOM SERVER PREFIX AND ADJUSTMENT
#   CREATE FILE W SCRIPT FOR IMPORT TO EDIT ANY GIVEN JSON ENTRY (PARAMS: ACTION(ADD,REMOVE,CHANGE), ASPECT TO BE ACTED ON, VALUE(if delete = null))
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
#   
