import lightbulb
import random

plugin = lightbulb.Plugin("basics")


@plugin.command
@lightbulb.command("ping", "see if the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("pong")


def load(bot):
    bot.add_plugin(plugin)
