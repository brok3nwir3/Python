# Discord news bot.
#
# IMPORTANT!
# This bot uses free APIs to retreve various news information. Note the following:
# 1) You'll need to create free accounts to obtain API keys and use some of the included APIs.
# 2) Most of the free APIs limit you to x5 requests per 5 minutes.
# 3) The stock market API only works Monday-Friday.
# 4) The stock market function determines the date via your system date.
import discord
import os
import requests
import json
from datetime import date
from dotenv import load_dotenv
from discord.ext import commands

# Global time variables.
global today
today = date.today()
global today_string
today_string = str(today)

# Load the Discord API token and other tokens from an environment file.
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_NEWS_TOKEN")
CRYPTO_TOKEN = os.getenv("COIN_API")
EXCHANGE_TOKEN = os.getenv("ALPHA_API")
STOCK_TOKEN = os.getenv("POLYGON_API")

# Bot prefixes.
prefix_list = ['!', '$', '#']

# Bot permissions.
bot = commands.Bot(command_prefix=prefix_list, intents=discord.Intents().all())

# Server specific emoji IDs. Obtained using "\:emote:" .
stonks_emoji = "<:stonks:914288192847491083>"
illuminati_emoji = "<:illuminati:915850513138982962>"

# Set bot status.
@bot.event
async def on_ready():
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the news"))

#--------------------------------------------------------------------#
# A function to parse JSON data and pull market data, using several APIs.
def get_market():
        # Time
        response = requests.get("http://worldtimeapi.org/api/timezone/America/Los_Angeles")
        json_data = json.loads(response.text)
        json_time = json_data['datetime']
        time_parse = json_time[11:16]
        json_utc = json_data['utc_datetime']
        result_time = "The current time (PST) is :watch: **" + time_parse + "**\n*UTC: " + json_utc + "*\n\n"
        # Crypto
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_btc = "BTC **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_eth = "\nETH **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/LTC/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_ltc = "\nLTC **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/XMR/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_xmr = "\nXMR **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/USDC/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_usdc = "\nUSDC **${:,.2f}**".format(json_parsed)
        result_crypto = "" + illuminati_emoji + " Crypto\n" + result_btc + result_eth + result_ltc + result_xmr + result_usdc + "\n\n"
        # Stocks
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/MSFT/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_msft = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/AMZN/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_amzn = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/OKTA/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_okta = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/GOOGL/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_googl = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/TSLA/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_tsla = "" + json_stock + " **$" + str(json_price) + "**"
        result_stocks = "" + stonks_emoji  + " The latest closing stock prices...\n" + result_msft + "\n" + result_amzn + "\n" + result_okta + "\n" + result_googl + "\n" + result_tsla + "\n\n"
        # Exchange
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_eur = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :euro: Euros\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=GBP&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_gbp = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :pound: British Pounds\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CAD&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_cad = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :flag_ca: Canadian Dollars\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CNY&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_cny = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :yen: Chinese Yuan\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=RUB&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_rub = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :flag_ru: Russian Rubles\n"
        result_exchange = "1.00 :dollar: USD currently exchanges for...\n" + result_eur + result_gbp + result_cad + result_cny + result_rub
        # Collect and return all data.
        all_results = result_time + result_crypto + result_stocks + result_exchange
        return(all_results)

@bot.command(help="Returns all categories of market information.")
async def market(ctx):
        await ctx.channel.send(get_market())

#--------------------------------------------------------------------#
# A function to parse JSON data and pull some exchange rates, using an API.
def get_exchange():
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EUR&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_eur = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :euro: Euros\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=GBP&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_gbp = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :pound: British Pounds\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CAD&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_cad = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :flag_ca: Canadian Dollars\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CNY&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_cny = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :yen: Chinese Yuan\n"
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=RUB&apikey=" + EXCHANGE_TOKEN)
        json_data = json.loads(response.text)
        json_exchange = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        result_rub = "" + json_exchange.partition('.')[0] + "." + json_exchange.partition('.')[2][0:2] + " :flag_ru: Russian Rubles\n"
        result_exchange = "1.00 :dollar: USD currently exchanges for...\n" + result_eur + result_gbp + result_cad + result_cny + result_rub
        return(result_exchange)

@bot.command(help="Returns some exchange rates.")
async def exchange(ctx):
        await ctx.channel.send(get_exchange())

#--------------------------------------------------------------------#
# A function to parse JSON data and pull some current stock prices, using an API.
def get_stocks():
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/MSFT/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_msft = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/AMZN/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_amzn = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/OKTA/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_okta = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/GOOGL/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_googl = "" + json_stock + " **$" + str(json_price) + "**"
        response = requests.get("https://api.polygon.io/v2/aggs/ticker/TSLA/prev?adjusted=true&apiKey=" + STOCK_TOKEN)
        json_data = json.loads(response.text)
        json_stock = json_data['ticker']
        json_price = json_data['results'][0]['c']
        result_tsla = "" + json_stock + " **$" + str(json_price) + "**"
        result_stocks = "" + stonks_emoji  + "\nThe latest closing stock prices...\n" + result_msft + "\n" + result_amzn + "\n" + result_okta + "\n" + result_googl + "\n" + result_tsla
        return(result_stocks)

@bot.command(help="Returns some stock prices.")
async def stocks(ctx):
        await ctx.channel.send(get_stocks())

#--------------------------------------------------------------------#
# A function to parse JSON data and pull the current time, using an API.
def get_time():
        response = requests.get("http://worldtimeapi.org/api/timezone/America/Los_Angeles")
        json_data = json.loads(response.text)
        json_time = json_data['datetime']
        time_parse = json_time[11:16] #Slice out time data.
        json_utc = json_data['utc_datetime']
        result = "The current time (PST) is: " + time_parse + "\nUTC: " + json_utc
        return(result)

@bot.command(help="Returns the current time.")
async def time(ctx):
        await ctx.channel.send(get_time())

#--------------------------------------------------------------------#
# A function to parse JSON data and pull the current time, using an API.
def get_date():
        response = requests.get("http://worldtimeapi.org/api/timezone/America/Los_Angeles")
        json_data = json.loads(response.text)
        json_time = json_data['datetime']
        date_parse = json_time[0:10] #Slice out date data.
        result = "The current date in western United States is: " + date_parse
        return(result)

@bot.command(help="Returns the current date.")
async def date(ctx):
        await ctx.channel.send(get_date())

#--------------------------------------------------------------------#
# A function to parse JSON data and pull the current price of crypto, using an API.
def get_crypto():
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/BTC/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_btc = "BTC **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/ETH/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_eth = "\nETH **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/LTC/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_ltc = "\nLTC **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/XMR/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_xmr = "\nXMR **${:,.2f}**".format(json_parsed)
        response = requests.get("https://rest.coinapi.io/v1/exchangerate/USDC/USD/?apikey=" + CRYPTO_TOKEN)
        json_data = json.loads(response.text)
        json_parsed = json_data['rate']
        result_usdc = "\nUSDC **${:,.2f}**".format(json_parsed)
        result_crypto = ":money_mouth:\nCrypto\n" + result_btc + result_eth + result_ltc + result_xmr + result_usdc
        return(result_crypto)

@bot.command(help="Returns the price of BTC.")
async def crypto(ctx):
        await ctx.channel.send(get_crypto())

#--------------------------------------------------------------------#
# A function to parse JSON data and pull random quotes, using an API.
def get_tech_news():
        response = requests.get("https://inshorts.deta.dev/news?category=technology")
        json_data = json.loads(response.text)
        json_parsed = json_data['data'][0]['url']
        return(json_parsed)

@bot.command(help="Returns a random tech news article.")
async def tech(ctx):
        await ctx.channel.send(get_tech_news())

#--------------------------------------------------------------------#
# A function to parse JSON data and pull a random space news article, using an API.
def get_space_news():
        response = requests.get("https://api.spaceflightnewsapi.net/v3/articles")
        json_data = json.loads(response.text)
        json_parsed = json_data[3]['url']
        return(json_parsed)

@bot.command(help="Returns a random space news article.")
async def space(ctx):
        await ctx.channel.send(get_space_news())

#--------------------------------------------------------------------#
# Error message function.
@bot.event
async def arg_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
                await ctx.send("Hello there, please add something after '!'")

# A message interaction function.
@bot.event
async def on_message(message):
        if message.content == "hi" and message.author != bot.user:
                await message.channel.send("Greetings! Use !help to view my commands.")
        await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
