# Category manager for the bot

from discord.ext import commands


class Categories(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='category')
    async def category(self, ctx: commands.Context):
        print(f' [+] Received category command from {ctx.author}')
        await ctx.reply(f'Category 1!')


async def setup(bot):
    await bot.add_cog(Categories(bot))
