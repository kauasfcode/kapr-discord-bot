import discord
import os
from discord.ext import commands
from bot_functions.roll_function import roll_dice
from bot_functions.initiative_function import roll_initiative
from numpy import random
from dotenv import load_dotenv
import uuid

load_dotenv("/home/kaua/personal projects/rpg-discord-bot/bot-env/.env")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command()
async def roll(ctx:commands.Context, dado):
    print(dado)
    dice_result = roll_dice(dado)
    await ctx.reply(dice_result)
    
@bot.command()
async def initiative(ctx:commands.Context, *, msg: str):
    initiative = roll_initiative(msg)
    await ctx.reply(initiative)

@bot.command()
async def talk(ctx:commands.Context):
    mentions = ctx.message.mentions
    guild = ctx.guild
    vc_name = str(uuid.uuid4())
    voice_channel = await guild.create_voice_channel(name=vc_name)
    
    for mention in mentions:
        await mention.move_to(voice_channel)
    await ctx.author.move_to(voice_channel)


bot.run(os.getenv('DISCORD_BOT_TOKEN'))