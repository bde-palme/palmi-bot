#! /usr/bin/env python

import config
import bot_params
from discord.ext import commands
from discord import Intents, Message

# Bot class


class PalmiBot(commands.Bot):
    """ 
    PalmiBot class
    """

    def __init__(self, command_prefix: str, intents: Intents):
        super().__init__(command_prefix, intents=intents)

    async def on_ready(self):
        print(f' [+] Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message: Message):
        print(f'USER - {message.author} texted - {message.content}')
        await self.process_commands(message)

    async def setup_hook(self):
        for cog in bot_params.COGS:
            await self.load_extension(f'cogs.{cog}')
        print(f' [+] Loaded cogs: {bot_params.COGS}')


# Bot instance creation
bot = PalmiBot(command_prefix=bot_params.COMMAND_PREFIX,
               intents=bot_params.INTENTS)

bot.run(config.DISCORD_TOKEN)
