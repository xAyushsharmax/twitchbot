from twitchio.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    async def ban(self, ctx):
        if not ctx.author.is_mod:
            await ctx.send(f'Sorry {ctx.author.name}, you do not have permission to use this command.')
            return
        
        user = ctx.message.mentions[0]  # Get the first mentioned user
        await ctx.send(f'Banning {user.name}...')

    @commands.command(name='mute')
    async def mute(self, ctx):
        if not ctx.author.is_mod:
            await ctx.send(f'Sorry {ctx.author.name}, you do not have permission to use this command.')
            return
        
        user = ctx.message.mentions[0]  # Get the first mentioned user
        await ctx.send(f'{user.name} has been muted!')
