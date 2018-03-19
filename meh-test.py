import discord
from discord.ext.command import Bot
from discord.ext import commands
import aysnico
import time

Client = discord.Client()
client = command.Bot(comman_prefix = "~")

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
	  
	

	
	
client.run("Token")
