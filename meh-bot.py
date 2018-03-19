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
  if message.content == "cookie":
    await client.send_message(message.channel, ":cookie:")
  if message.content.startswith('!ping'):
      userID = message.author.id
      await client.send_message(message.channel, "<@%s> Pong!" % (userID))
	
	
client.run("Token")
