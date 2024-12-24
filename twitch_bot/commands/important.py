from twitchio.ext import commands

class ImportantCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='raid')
    async def raid(self, ctx):
        if ctx.author.name.lower() != ctx.channel.name.lower():
            await ctx.send("Only the broadcaster can use the ;raid command!")
            return

        content = ctx.message.content.split()
        if len(content) < 2:
            await ctx.send("Usage: ;raid <channel_name>")
            return
        
        target_channel = content[1]
        await ctx.send(f"Raiding @{target_channel}! Everyone get ready!")
        await ctx.send(f"/raid {target_channel}")

    @commands.command(name='shoutout')
    async def shoutout(self, ctx):
        target = ctx.message.content.split(' ')[1]  # Gets the user mentioned after the command
        await ctx.send(f'Give a shoutout to @{target}!')
