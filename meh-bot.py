import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "~")

@client.event
async def on_ready():
  print ("Ready!")
  
@client.event
async def on_message(message):
  if message.content == "~cookie":
    await client.send_message(message.channel, ":cookie:")

  if message.content.startswith('~ping'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> Pong!" % (userID))

  if message.content == "~help":
    await client.send_message(message.channel, """
__**Commands**__
```- you need to write all small, sorry
- you can trigger a command by using:
  cookie
- the developer @Biscuit#0061 is inexperienced
- updates comming soon! (hopfully)```""")

  if message.content.lower().startswith("~say"):
    if message.author.id == "209391652870029312":
      await client.delete_message(message)
      args = message.content.split(" ")
      await client.send_message(message.channel,"%s" % (" ".join(args[1:])))
    else:
      await client.send_message(message.channel, "Only the owner can use this command!")
	
	
client.run("Token")
