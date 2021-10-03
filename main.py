import discord
import time
import os
import requests
import json
from keep_alive import keep_alive
from discord.ext import commands
#Import libares

bot = commands.Bot(command_prefix="-",case_insensitive=True)
#prefix and case senstive commands off

bot.author_id = 487258918465306634
#Set bot owner

@bot.event 
async def on_ready():
    print("Bot has posted. Link to invite = https://bit.ly/1negative11")
    print(bot.user)
#bot is ready if this happens

@bot.command(name='hello', description="Greet the user!")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")
#hello commands

@bot.command(name='invite', description="Get the invite link for user")
async def invite(ctx):
    await ctx.send(f"```Invite link is https://bit.ly/1negative11! Just too tell you the bot may change its link if 1rom11 change the name```")
#invite command

@bot.command(name='credits', description="Bot's credits")
async def credit(ctx):
    await ctx.send(f"""```Bot creator: 1rom11
	Created for School Discord
	Coded in relp.it vist https://discord.1rom11yt.repl.co
	```
	**Thank you for using this bot**""")
#credit command

@bot.command(name='code', description="Bot code")
async def code(ctx):
    await ctx.send(f"Code for bot is in https://bit.ly/code-negative")
#code command

extensions = [
	'cogs.cog_example'
]
#extension connect code

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)
#load extensions

keep_alive()
token = os.environ['token']
os.environ.get("TOKEN") 
bot.run(token)
#Flask ping bot to stay awake

if token:
	print("token = ",token)
else:
	print("You are not the owner of this bot")

#owner ship boolen

# Orignal bot autor = 1rom11