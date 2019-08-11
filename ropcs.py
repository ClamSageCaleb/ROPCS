__author__ = "Caleb Smith"
__copyright__ = "Copyright 2019, MIT License"
__credits__ = "Caleb Smith"
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "Caleb Smith"
__email__ = "caleb.benjamin9799@gmail.com"
__status__ = "Production"

import random
import asyncio
import aiohttp
import json
import discord
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!")
TOKEN = "NTg4NDM0NjAzNjM1OTAwNDI2.XUunhg.xyN0xKhOnRlnF0jba6p-knsL50o"

client = Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

txt = 'champions.txt'
champs = []
roles = []
with open(txt) as f:
    for line in f:
        s = line.strip().split(' ')
        champs.append(s[0])
        roles.append(s[1])
champSelect = dict(zip(champs, roles))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        msg = discord.Embed(title='__**Scrub Bot Commands**__', description="", color=0x0000ff)
        msg.add_field(name="Eight Ball", value="Answers a yes/no question. \n Usage: !8ball [question]",
                      inline=False)
        msg.add_field(name="Square", value="Squares a number. \n Usage: !square [number]", inline=False)
        msg.add_field(name="Bitcoin", value="Current value of Bitcoin. \n Usage: !bitcoin", inline=False)
        msg.add_field(name="Random Champ", value="Selects a random LoL Champion. \n Usage: !rc", inline=False)
        msg.add_field(name="Random Role", value="Selects a random LoL Role. \n Usage: !rr", inline=False)
        msg.add_field(name="Combo Role/Champ", value="Selects a random LoL Role and Champion. \n Usage: !rac",
                      inline=False)
        msg.add_field(name="GG EZ", value="Just use it \n Usage: !ggez @[user]", inline=False)
        msg.set_thumbnail(url="https://themerkle.com/wp-content/uploads/2017/05/kingdice-pr.jpg")
        msg.set_footer(text="Developed by Clam")
        await client.send_message(message.channel, embed=msg)
    await client.process_commands(message)


@client.command(name='8ball', aliases=['eight_ball', 'eightball', '8-ball'], pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


@client.command(aliases=['rc', 'rchamp'], pass_context=True)
async def randomchamp(ctx):
    await client.say("{0.mention}, Your Champ is: ".format(ctx.message.author) + random.choice(champs))


@client.command(aliases=['rr', 'rrole'], pass_context=True)
async def randomrole(ctx):
    await client.say("{0.mention}, Your Role is: ".format(ctx.message.author) + random.choice(roles))


@client.command(aliases=['rac', 'rolechamp'], pass_context=True)
async def bothroleandchamp(ctx):
    await client.say("{0.mention}, \n Your Champ is: ".format(ctx.message.author) + random.choice(
        champs) + "\n Your Role is: " + random.choice(roles))


@client.command()
async def ggez(name):
    msg = '''░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█▀▀▀░█▀▀▀░░█▀▀░▀▀█░░░░
░░░█░▀█░█░▀█░░█▀▀░▄▀░░░░░
░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░'''
    await client.say(msg + "\n" + name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
