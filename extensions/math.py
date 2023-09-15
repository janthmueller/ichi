import lightbulb
import random

plugin = lightbulb.Plugin("math")


@plugin.command
@lightbulb.option(
    "n", "number of sides on the dice (defaults to 6)", type=int, default=6
)
@lightbulb.command("roll", "roll a dice with n sides")
@lightbulb.implements(lightbulb.SlashCommand)
async def roll(ctx):
    await ctx.respond(random.randint(1, ctx.options.n))


def load(bot):
    bot.add_plugin(plugin)
