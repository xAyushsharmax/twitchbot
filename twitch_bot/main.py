import os
from dotenv import load_dotenv
from twitchio.ext import commands
from commands.general import GeneralCommands
from commands.important import ImportantCommands
from commands.admin import AdminCommands

load_dotenv()
class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.getenv("TWITCH_OAUTH_TOKEN"),
            client_id=os.getenv("TWITCH_CLIENT_ID"),
            nick=os.getenv("TWITCH_BOT_USERNAME"),
            prefix=";",
            initial_channels=self.get_channels()
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"Connected to channels | {self.connected_channels}")

    async def event_message(self, message):
        if message.echo:
            return
        print(f"Message from {message.author.name}: {message.content}")
        await self.handle_commands(message)  
    def get_channels(self):
        # Split the channel names by commas and strip whitespace
        return [channel.strip() for channel in os.getenv("TWITCH_CHANNEL_NAME").split(",")]


bot = TwitchBot()
bot.add_cog(GeneralCommands(bot))
bot.add_cog(ImportantCommands(bot))
bot.add_cog(AdminCommands(bot))

bot.run()
