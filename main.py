import discord
import time
import os
import requests
import json
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix="*",case_insensitive=True)

bot.author_id = 487258918465306634

@bot.event 
async def on_ready():
    print("Bot has posted. Link to invite = https://bit.ly/iroquois-bot")
    print(bot.user)

@bot.command(name='hello', description="Greet the user!")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")

@bot.command(name='invite', description="Get the invite link for user")
async def invite(ctx):
    await ctx.send(f"```Invite link is https://bit.ly/iroquois-bot! Just too tell you the bot may change its link if 1rom11 change the name```")

@bot.command(name='credits', description="Bot's credits")
async def invite(ctx):
    await ctx.send(f"""```Bot creator: 1rom11
	Created for School Discord
	Coded in relp.it vist https://discord.1rom11yt.repl.co
	```
	**Thank you for using this bot**""")

@bot.command(name='credits', description="Bot's
credits")
async def invite(ctx):
    await ctx.send(f"""Code for bot is in """)

extensions = [
	'cogs.cog_example'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

keep_alive()
token = os.environ['token']
os.environ.get("TOKEN") 
bot.run(token)

if token:
	print("token = ",token)
else:
	print("You are not the owner of this bot")