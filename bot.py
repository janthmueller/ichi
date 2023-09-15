import hikari
import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
default_enabled_guilds = eval(
    os.getenv("DEFAULT_ENABLED_GUILDS")
)  # TODO: replace eval with something safer

bot = lightbulb.BotApp(
    token=discord_token, default_enabled_guilds=default_enabled_guilds
)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print(f"Bot has started!")


bot.load_extensions_from("./extensions")
bot.run()
