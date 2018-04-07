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

  if message.content.lower().startswith('~help') or message.content.lower().startswith('~command'):
    embed = discord.Embed(title="Information", description="""- the prefix is a "~" not a "-"
- you can trigger commands only with the prefix
- updates comming soon! (hopefully)
- the developer @Biscuit#0061 is inexperienced ^^'
""", color=0xFF1D8E)
    embed.add_field(name="Commands", value="""
cookie = You will receive a cookie :3
f = Pay your respects
ping = Play ping pong!
say = add an text afterwards to make the bot say something you want (owner only)
meh = meh
gn; nighty; goodnight = sleep well
coin; cf = Flip a coin to make a choice
lotusquote; lq = Exclusive owner quotes
choice; q = Add a 'yes or no' question
""", inline=False)
    embed.add_field(name="Support", value="""If you have struggles with the bot or any questions, 
contact @Biscuit#0061 on her server:
https://discord.gg/kQThPRT""", inline=False)
    await client.send_message(message.channel, embed=embed) 

	
  if message.content.lower().startswith("no u"):
    await client.add_reaction(message, "ðŸ‘€")
	
  if message.content.lower().startswith("lewd"):
    await client.add_reaction(message, "ðŸ‘€")
	
  if message.content.lower().startswith('~cookie'):
    embed = discord.Embed(title=":cookie:", color=0xA72D23)
    await client.send_message(message.channel, embed=embed)

  if message.content.lower().startswith('~ping'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> Pong!" % (userID))

  if message.content.lower().startswith('~meh'):
    embed = discord.Embed(title="meh!", color=0xFF1D8E)
    await client.send_message(message.channel, embed=embed)

  if message.content.lower().startswith('~goodnight') or message.content.lower().startswith('~nighty') or message.content.lower().startswith('~gn'):
    userID = message.author.id
    await client.add_reaction(message, "ðŸ’¤")
    await client.add_reaction(message, "ðŸ’•")
    await client.send_message(message.channel, ("<@%s> Sleep well, my precious meh-mber ^^ :heart:") % (userID))

  if message.content.lower().startswith('~f'):
    userID = message.author.id
    await client.delete_message(message)
    await client.send_message(message.channel, "<@%s> has paid their respects :heart_exclamation:" % (userID))    

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
    choice = random.randint(1,16)  
    if choice == 1:
      embed = discord.Embed(title="You are awesome c:", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 2:
      embed = discord.Embed(title="meh!", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 3:
      embed = discord.Embed(title="yaay", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 4:
      embed = discord.Embed(title="Be yourself. I like you how you are ^^", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 5:
      embed = discord.Embed(title="Mine!", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 6:
      embed = discord.Embed(title="Your character is beautiful <3", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 7:
      embed = discord.Embed(title="Aww, such a qtie", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 8:
      embed = discord.Embed(title="hot", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 9:
      embed = discord.Embed(title="I should add more..", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 10:
      embed = discord.Embed(description="I want to control you to move you on the table smirk to make you lay down for me baby so that you can kiss MY ASS AND I CAN FLIP THE FUCKN TABLE flips table", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed) 
    if choice == 11:
      embed = discord.Embed(title="https://bdsmtest.org/", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 12:
      embed = discord.Embed(title="grrrrGRRRRR", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 13:
      embed = discord.Embed(title="wat https://i.redd.it/09yvzago4pjy.jpg", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 14:
      embed = discord.Embed(title="Everything is relative.", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 15:
      embed = discord.Embed(title="I am confused.", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
    if choice == 16:
      embed = discord.Embed(title="We are all indiviuals.", color=0xFF1D8E)
      await client.send_message(message.channel, embed=embed)
	  
	  
	  
  if message.content.lower().startswith('~q')or message.content.lower().startswith('~choice'):
    choice = random.randint(1,10)  
    if choice == 1:
      embed = discord.Embed(title="Yes.", color=0x00CD00)
      await client.send_message(message.channel, embed=embed)
    if choice == 2:
      embed = discord.Embed(title="No.", color=0xFF0000)
      await client.send_message(message.channel, embed=embed)
    if choice == 3:
      embed = discord.Embed(title="Maybe.", color=0xFFFF00)
      await client.send_message(message.channel, embed=embed)
    if choice == 4:
      embed = discord.Embed(title="Probably not.", color=0xFFFF00)
      await client.send_message(message.channel, embed=embed)
    if choice == 5:
      embed = discord.Embed(title="Definitely.", color=0xFFFF00)
      await client.send_message(message.channel, embed=embed)
    if choice == 6:
      embed = discord.Embed(title="No. Just no.", color=0xFF0000)
      await client.send_message(message.channel, embed=embed)
    if choice == 7:
      embed = discord.Embed(title="Try again.", color=0xFFFF00)
      await client.send_message(message.channel, embed=embed)
    if choice == 8:
      embed = discord.Embed(title="Why do you ask me?", color=0xFFFF00)
      await client.send_message(message.channel, embed=embed)
    if choice == 9:
      embed = discord.Embed(title="NO. GOD. NO. NOOOOOOOO!", color=0xFF0000)
      await client.send_message(message.channel, embed=embed)
    if choice == 10:
      embed = discord.Embed(title="Yehehehe s.", color=0x00CD00)
      await client.send_message(message.channel, embed=embed)
	  
	
	
  if message.content.lower().startswith("~wall"):
    if message.author.id == "209391652870029312":
      await client.send_message(message.channel,"""```{1} {1} {1} {1} {1} {1} {1} {1} {1} {1}
   {1} {1} {1} {1} {1} {1} {1} {1} {1} {1}
{1} {1} {1} {1} {1} {1} {1} {1} {1} {1}```""".format(message.author.mention, message.content[5:20]))
    else:
      await client.send_message(message.channel,"{0}, No, this is not my owner. Take back your word >{1}<.".format(message.author.mention, message.content[7:]))
	
  if message.content.lower().startswith("~topsikrit"):
    if message.author.id == "209391652870029312":
      await client.add_reaction(message, "ðŸ‘ðŸ»")
      await client.send_message(message.channel,"_hugs_ shh {1}, here's a cookie :cookie: c:".format(message.author.mention, message.content[11:]))
	
  if message.content.lower().startswith("~hello"):
    embed = discord.Embed(title="Tile", description="Desc", color=0xFF1D8E)
    embed.add_field(name="Fiel1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    await client.send_message(message.channel, embed=embed)  
	  
  if message.content.lower().startswith("~wolf"):
    if message.author.id == "209391652870029312" or message.author.id == "192405723462893568":
        args = message.content.split(" ")
        await client.send_message(message.channel,"%s wuff wuff :wolf:" % (" ".join(args[1:])))
    else:
      await client.send_message(message.channel, "Sorry, you are not wolf!")	
	  

	  
client.run("")
