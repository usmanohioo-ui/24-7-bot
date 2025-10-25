import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm alive and running on Render 🚀")

bot.run("MTQyNDM5OTMzMTAzNjg4OTI1OQ.GfLNcC.ntbd-tK1EPZu4DdBtLfjV2OCeWkTKfAKzxiYKY")