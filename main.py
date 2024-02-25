#! /usr/bin/env python

import config
import discord

# Bot instance creation
bot = discord.Client(intents=None)

# functions

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# run bot
bot.run(config.DISCORD_TOKEN)

