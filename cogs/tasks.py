# Tasks manager for the bot

from discord.ext import commands

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='task')
    async def task(self, ctx):
        print(f' [+] Received task command from {ctx.author}')
        await ctx.reply(f'Task 1!')

async def setup(bot):
    await bot.add_cog(Tasks(bot))