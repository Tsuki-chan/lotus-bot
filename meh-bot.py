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

  if message.content.startswith('~meh'):
    await client.send_message(message.channel, "meh!") 

  if message.content.startswith('~f'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> has paid their respects :heart_exclamation:" % (userID))    

  if message.content == "~help":
    await client.send_message(message.channel, """
__**Commands**__
```- you need to write all small, sorry
- the prefix is a "~" not a "-"
- you can trigger a command by using ~:
  cookie, f, ping, say [text], meh
- the developer @Biscuit#0061 is inexperienced
- updates comming soon! (hopfully)```""")

  if message.content.lower().startswith("~say"):
      userID = message.author.id
      await client.delete_message(message)
      args = message.content.split(" ")
      await client.send_message(message.channel, "<@%s>, %s" % ((userID), " ".join(args[1:])))
	  
# idk about this below	  
  if message.content.lower().startswith("~lilq"):
    await client.send_message(message.channel, "Do you like fish?")
    if message.content == "yes":
      await client.delete_message(message)
      await client.send_message(message.channel, "Nice, me too. Bloop!")
    elif message.content == "no":
      await client.delete_message(message)
      await client.send_message(message.channel, ":(")
    else:
      await client.delete_message(message)
      await client.send_message(message.channel, "Please only answer with yes or no")
	
client.run("Token")
