from twitchio.ext import commands
from twitchAPI.twitch import Twitch
import random
import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()
class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.oauth_token = os.getenv("TWITCH_OAUTH_TOKEN")
        self.client_id = os.getenv("TWITCH_CLIENT_ID")
        self.decapi_token = os.getenv("DECAPI_TOKEN")

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}, welcome to the stream and enjoy your stay.')

    @commands.command(name='8ball')
    async def _8ball(self, ctx):
        responses = ["Yes", "No", "Maybe", "Ask again later", "Definitely", "Absolutely not","kinda","fk no","yes mf and stop asking me ques now"]
        await ctx.send(random.choice(responses))

    @commands.command(name="random")
    async def random_command(self, ctx, start: int, end: int):
        if start > end:
            await ctx.send("Please make sure the first number is smaller than or equal to the second number.")
            return

        random_number = random.randint(start, end)
        await ctx.send(f"A random number between {start} and {end}: {random_number}")

    @commands.command(name="toss")
    async def cointoss(self,ctx):
        side  = "Heads" if random.randint(0,1) == 0 else "Tails"
        await ctx.send(f"the coin has decided {side}")

    @commands.command(name="roll")
    async def roll(self,ctx):
        side  = random.randint(1,6) 
        await ctx.send(f"the dice has decided {side}")
    
    @commands.command(name="followage")
    async def followage(self, ctx):
        mentioned_user = None
        message_content = ctx.message.content

        match = re.search(r"@(\w+)", message_content)
        if match:
            mentioned_user = match.group(1)  

        if not mentioned_user:
            mentioned_user = ctx.author.name

        channel_name = ctx.channel.name

        try:
            response = requests.get(
                f"https://decapi.me/twitch/followage/{channel_name}/{mentioned_user}?token={self.decapi_token}"
            )
            response.raise_for_status()
            followage = response.text

            if followage == "User is not following the channel":
                await ctx.send(f"{mentioned_user}, you are not following {channel_name}.")
            else:
                await ctx.send(f"{mentioned_user}'s followage: {followage}")
        except requests.exceptions.RequestException as e:
            await ctx.send(f"An error occurred while fetching follow age: {e}")
    
    @commands.command(name="social")
    async def social(self, ctx):
        links = (
            "Check out my socials here:\n"
            " Website: https://spacebirblizzy.carrd.co/\n"
            " Discord: https://discord.gg/sBXnexHBtV"
        )
        await ctx.send(links)