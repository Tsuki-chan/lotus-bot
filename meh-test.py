import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "~")

@client.event
async def on_ready()
  print ("Ready!")
  
@client.event
async def on_message(message):
  if message.content == "!cookie":
    await client.delete_message(message)
    await client.send_message(message.channel, " Here is your big :cookie:")
    await client.send_message(message.channel, ":cookie:")
  
  if message.content.lower().startswith("~meh"):
    if message.author.id == "209391652870029312":
	  args = message.content.split (" ")
	  await client_send_message(message.channel,"%s" % (" ".join(args[1])))
	else await client.send_message(message.channel, "Only Lotus can use this command")
  
  if message.content.lower().startswith("~lilq"):
    await client.send_message(message.channel, "Do you like fish?")
      if message.content == "yes":
         await client.send_message(message.channel, "Nice, me too. Bloop!")
      elif message.content == "no":
	 await client.send_message(message.channel, ":(")
      else:
	 await client.send_message(message.channel, "Please only answer with yes or no")
	  
	

	
	
client.run("Token")
