import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

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
  cookie, f, ping, say [text], meh, gn, coin; cf, lotusquote; lq
  
- the developer @Biscuit#0061 is inexperienced

- updates comming soon! (hopfully)```""")

  if message.content.lower().startswith("~say"):
      userID = message.author.id
      await client.delete_message(message)
      args = message.content.split(" ")
      await client.send_message(message.channel, "<@%s>, %s" % ((userID), " ".join(args[1:])))
	  
  if message.content.lower().startswith('~coin') or message.content.lower().startswith('~cf'): #Coinflip 50/50% 
    choice = random.randint(1,2)
    if choice == 1:
      await client.add_reaction(message, 'ðŸŒ‘')
    if choice == 2:
      await client.add_reaction(message, 'ðŸŒ•')
	  
  if message.content.lower().startswith('~lotusquote')or message.content.lower().startswith('~lq'):
    choice = random.randint(1,14)  
    if choice == 1:
      await client.send_message(message.channel, '```"You are awesome c:"```')
    if choice == 2:
      await client.send_message(message.channel, '```"meh!"```')
    if choice == 3:
      await client.send_message(message.channel, '```"yaay"```')
    if choice == 4:
      await client.send_message(message.channel, '```"Be yourself. I like you how you are ^^"```')
    if choice == 5:
      await client.send_message(message.channel, '```"Mine!"```')
    if choice == 6:
      await client.send_message(message.channel, '```"Your character is beatiful <3"```')
    if choice == 7:
      await client.send_message(message.channel, '```"Aww, such a qtie"```')
    if choice == 8:
      await client.send_message(message.channel, '```"hot"```')
    if choice == 9:
      await client.send_message(message.channel, '```"I should add more..."```')
    if choice == 10:
      await client.send_message(message.channel, '```"I want to control you to move you on the table smirk to make you lay down for me baby so that you can kiss MY ASS AND I CAN FLIP THE FUCKN TABLE *flips table*" ``` ')
    if choice == 11:
      await client.send_message(message.channel, '"https://bdsmtest.org/"')
    if choice == 12:
      await client.send_message(message.channel, '```"grrrrGRRRR"```')
    if choice == 13:
      await client.send_message(message.channel, '" wat https://i.redd.it/09yvzago4pjy.jpg"')
    if choice == 14:
      await client.send_message(message.channel, '```"Everything is relative"```')
	  	 	  


client.run("Token")
