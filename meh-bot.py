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
  if message.content.lower().startswith == "~cookie":
    await client.send_message(message.channel, ":cookie:")

  if message.content.lower().startswith('~ping'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> Pong!" % (userID))

  if message.content.lower().startswith('~meh'):
    await client.send_message(message.channel, "meh!") 

  if message.content.lower().startswith('~f'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> has paid their respects :heart_exclamation:" % (userID))    

  if message.content.lower() == "~help" or message.content.lower() =="~commands" or message.content.lower() =="~command":
    await client.send_message(message.channel, """
__**Commands**__
```- the prefix is a "~" not a "-"
- you can trigger a command by using ~:
  cookie, f, ping, say [text], meh
- the developer @Biscuit#0061 is inexperienced
- updates comming soon! (hopfully)```""")

  if message.content.lower().startswith("~say"):
      userID = message.author.id
      await client.delete_message(message)
      args = message.content.split(" ")
      await client.send_message(message.channel, "<@%s>, %s" % ((userID), " ".join(args[1:])))
	  	 	  
			  
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
