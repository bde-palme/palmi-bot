import discord

# Intents
INTENTS = discord.Intents()
INTENTS.messages = True
INTENTS.guilds = True
INTENTS.message_content = True
INTENTS.reactions = True

# Config
COMMAND_PREFIX = '!'

# cogs
COGS = [
    "categories",
    "tasks",
]