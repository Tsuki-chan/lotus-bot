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
  if message.content.lower().startswith('~cookie'):
    await client.send_message(message.channel, ":cookie:")

  if message.content.lower().startswith('~ping'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> Pong!" % (userID))

  if message.content.lower().startswith('~meh'):
    await client.send_message(message.channel, "meh!")

  if message.content.lower().startswith('~goodnight') or message.content.lower().startswith('~nighty') or message.content.lower().startswith('~gn'):
    userID = message.author.id
    await client.send_message(message.channel, ("<@%s> Sleep well, my precious meh-mber ^^ :heart:") % (userID))

  if message.content.lower().startswith('~f'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> has paid their respects :heart_exclamation:" % (userID))    

  if message.content.lower().startswith('~help') or message.content.lower().startswith('~command'):
    await client.send_message(message.channel, """
__**Commands**__
```- the prefix is a "~" not a "-"
- you can trigger a command by using ~:
  cookie, f, ping, say [text], meh, gn
- the developer @Biscuit#0061 is inexperienced
- updates comming soon! (hopfully)```""")

  if message.content.lower().startswith("~say"):
      userID = message.author.id
      await client.delete_message(message)
      args = message.content.split(" ")
      await client.send_message(message.channel, "<@%s>, %s" % ((userID), " ".join(args[1:])))
	  	 	  


client.run("Token")
