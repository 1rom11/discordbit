#Made using relp.it and discord.py
#-1rom11

import discord
import time
import os
import requests
import json
from keep_alive import keep_alive
from discord.ext import commands
#Import libares

bot = commands.Bot(command_prefix="-",case_insensitive=True, help_command=None)
bot.remove_command('help')
#Setup

bot.author_id = 487258918465306634
#Set bot owner

@bot.event 
async def on_ready():
    print('Logged on as', bot.user)

    async def on_message(self, message):
        # Don't refspond to ourselves
        if message.author == self.user:
            return
# Bot is ready if this happens



@bot.command(name ='help', description="Help command", pass_content=True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		color = discord.Color.orange()
	)

	embed.set_author(name="Help")
	embed.add_field(name= '-code', value='Returns the link to the github used for this bot', inline=False)
	embed.add_field(name= '-invite', value='Returns the value of the link to invite the bot', inline=False)
	embed.add_field(name= '-credits', value='Returns the bot credits', inline=False)
	embed.add_field(name= '-hello', value='Greets the user', inline=False)
	embed.add_field(name='-kick @user', value='Kick mentioned user (ex. -kick @1rom11)', inline=False)

	await ctx.send(author, embed=embed)
#help command (with embed)

@bot.command(name='hello', description="Greet the user!")
async def hello(ctx):
	user = ctx.message.author
	embed = discord.Embed(
		title="Hello", description="",color= discord.Color.orange()
		)

	embed.add_field(name="Hello", value=f"Hello {ctx.author.name}!", inline=True)

	await ctx.send(user, embed=embed)
#hello commands

@bot.command(name='invite', description="Get the invite link for user")
async def invite(ctx):
	user = ctx.message.author
	embed = discord.Embed(
		title="Invte Link", description="Invite link for bot", color=discord.Color.orange()
	)

	embed.add_field(name="Invite", value=f"Invite link is https://bit.ly/1negative11! Just too tell you the bot may change its link if 1rom11 change the name")

	await ctx.send(user, embed=embed)
#invite command

@bot.command(name='credits', description="Bot's credits")
async def credit(ctx):

	await ctx.send(f"```Creator: 1rom11```")
#credit command

@bot.command(name='code', description="Bot code")
async def code(ctx):
    await ctx.send(f"Code for bot is in https://bit.ly/code-negative")
#code command

@bot.command(name="Kick", description="Kick member")
async def kick(ctx, member : discord.Member):

    try:
        await member.kick(reason=None)
        await ctx.send("Kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions

    except:
        await ctx.send(f"Bot cannot kick this person. Ether the person has higher rank or{ bot.username} don't have kick perms")

@bot.command(name="Ban", description="Ban member")
async def ban(ctx, member : discord.Member):

    try:
        await member.ban(reason=None)
        await ctx.send("Baned "+member.mention) #simple ban command to demonstrate how to get and use member mentions

    except:
        await ctx.send(f"Bot cannot ban this person. Ether the person has higher rank or {bot.username} don't have ban perms")

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
#Change token to your bot token (Token must be in a secret (I used relp.it))
bot.run(token)
#Flask ping bot to stay awake

if token:
	print("token = ",token)
else:
	print("You are not the owner of this bot")

#owner ship boolen

# Orignal bot author = 1rom11