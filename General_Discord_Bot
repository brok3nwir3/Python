# A general purpose Discord bot.
import discord
import os
import random
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands

# Grab Discord API token from environment file.
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Bot prefixes.
prefix_list = ['!', '$', '#']

# Bot permissions.
bot = commands.Bot(command_prefix=prefix_list, intents=discord.Intents().all())

# Server specific emoji IDs. Obtained using "/:emote:" .
crit_emoji = "<:CRIT:925236565989527606>"
rekt_emoji = "<:REKT:937902738900136057>"

# Set bot status.
@bot.event
async def on_ready():
        await bot.change_presence(activity=discord.Game(name="DM me !help"))

#--------------------------------------------------------------------#
# A function to parse JSON data and pull random waifu images, using an API.
def get_waifu(waifu_select):
        response = requests.get("https://api.waifu.pics/sfw/" + waifu_select)
        json_data = json.loads(response.text)
        json_parsed = json_data['url']
        return(json_parsed)

@bot.command(help="Returns a random highfive waifu.")
async def highfive(ctx):
        await ctx.channel.send(get_waifu("highfive"))

@bot.command(help="Returns a random yeet waifu.")
async def yeet(ctx):
        await ctx.channel.send(get_waifu("yeet"))

@bot.command(help="Returns a random poke waifu.")
async def poke(ctx):
        await ctx.channel.send(get_waifu("poke"))

#--------------------------------------------------------------------#
# A function to parse JSON data and create a shortened URL, using an API.
def get_short_url(big_url):
        response = requests.get("https://short-link-api.vercel.app/?query=" + big_url)
        json_data = json.loads(response.text)
        if "is.gd" in json_data:
                json_parsed = json_data['is.gd']
                result = "Here ya go, kid.\n" + json_parsed
                return(result)
        else:
                json_parsed = json_data['chilp.it']
                result = "Tough one, but here ya go.\n" + json_parsed 
                return(result)

@bot.command(help="Returns a shortened link.")
async def shorten(ctx, *args):
        await ctx.channel.send(get_short_url(*args))

#--------------------------------------------------------------------#
# A function to parse JSON data and pull random quores, using an API.
def get_quote():
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        json_parsed = json_data[0]['q'] + " -" + json_data[0]['a']
        return(json_parsed)

@bot.command(help="Returns a random quote.")
async def quote(ctx):
        await ctx.channel.send(get_quote())

#--------------------------------------------------------------------#
# A message function to greet new server members.
@bot.event
async def on_member_join(member):
        await member.send('Welcome to the jungle, punk!')

#--------------------------------------------------------------------#
# A function to have the bot respond to a thank you message.
thanks_list = ["No problemo, amigo.",
"Bout time I get some thanks.",
"It's the least I can do, I suppose."]
@bot.command()
async def thanks(ctx):
        bot_response = random.choice(thanks_list)
        await ctx.channel.send(bot_response)

#--------------------------------------------------------------------#
# A function to have the bot send a shooting gif.
@bot.command(help="Shoots.")
async def shoot(ctx):
        await ctx.channel.send(file=discord.File('bender_gun.gif'))

#--------------------------------------------------------------------#
# A function to have the bot send a neat gif.
@bot.command(help="Takes a photo.")
async def neat(ctx):
        await ctx.channel.send(file=discord.File('bender_neat.gif'))

#--------------------------------------------------------------------#
# A function to have the bot send a lightup gif.
@bot.command(help="Lights up.")
async def lightup(ctx):
        await ctx.channel.send(file=discord.File('bender_lightup.gif'))

#--------------------------------------------------------------------#
# A function to have the bot send a chug gif.
@bot.command(help="Chugs.")
async def chug(ctx):
        await ctx.channel.send(file=discord.File('bender_chug.gif'))

#--------------------------------------------------------------------#
# A function to have the bot send an applause gif.
@bot.command(help="Applauds.")
async def applause(ctx):
        await ctx.channel.send(file=discord.File('bender_applause.gif'))

#--------------------------------------------------------------------#
# An echo function, which repeats the users string.
@bot.command(help="Echoes what was said.")
async def echo(ctx, *args):
        response = ""
        for arg in args:
                response = response + " " + arg
        await ctx.channel.send(response)

#--------------------------------------------------------------------#
# A D20 rolling function.
@bot.command(help="Rolls a 20-sided dice.")
async def d20(ctx):
        roll = random.randrange(1,21)
        if roll == 20:
                await ctx.channel.send("20 " + crit_emoji + " CRIT!")
        if roll == 1:
                await ctx.channel.send("1  " + rekt_emoji + "  CRIT FAIL!")
        elif roll != 1 and roll != 20:
                await ctx.channel.send(roll)

#--------------------------------------------------------------------#
# Error message function.
@bot.event
async def arg_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
                await ctx.send("Bruh, add something after '!'")

#--------------------------------------------------------------------#
# A message interaction function.
@bot.event
async def on_message(message):
        if message.content == "hi" and message.author != bot.user:
                await message.channel.send("Howdy! Use !help to view my commands.")
        await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
