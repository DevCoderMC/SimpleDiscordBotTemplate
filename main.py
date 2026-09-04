import os

import discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.slash_command(name="ping", description="Replies with Pong")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond("Pong!")


bot.run(os.getenv("TOKEN"))