#! /usr/bin/env python

import config
import discord
from discord.ext import commands

# Intents
intents = discord.Intents()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.reactions = True

# Bot instance creation
bot = commands.Bot(command_prefix='!', intents=intents)

# functions

@bot.event
async def on_ready():
    print(f'----\n [+] Logged in as {bot.user} (ID: {bot.user.id})\n----')

# @bot.event
# async def on_message(message):
#     print(f'USER - {message.author} texted - {message.content}')
#     await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    print(f' [+] Received ping command from {ctx.author}')
    await ctx.reply(f'Pong!')

# run bot
bot.run(config.DISCORD_TOKEN)

