import discord
import os
from discord.ext import commands
from bot_functions.roll_function import roll_dice
from numpy import random
from dotenv import load_dotenv

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
    users = msg.split(" ")
    initiative_dict = {}
    reply = ""
    for user in users:
        user_dice_value = random.randint(1,21)
        initiative_dict[user] = user_dice_value

    initiative_dict = sorted(initiative_dict.items(), 
                             key=lambda x: x[1], 
                             reverse=True)

    for user_and_result in initiative_dict:
        reply += f"👉 {user_and_result[0]} 🎯 {user_and_result[1]}\n"    
    await ctx.reply(reply)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))