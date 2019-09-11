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

# Bot prefix and Discord Bot token
BOT_PREFIX = ("!")
TOKEN = "NTg4NDM0NjAzNjM1OTAwNDI2.XUunhg.xyN0xKhOnRlnF0jba6p-knsL50o"

# Creates the Bot with name 'client'
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')

# Lists for information such as LoL Champs/Roles/Keystones/Items
txt = 'champions.txt'
itemsTxt = 'items.txt'
champs = []
roles = []
items = []
ks = ['Press the Attack', 'Lethal Tempo', 'Fleet Footwork', 'Conqueror', 'Electrocute', 'Predator', 'Dark Harvest',
      'Hail of Blades', 'Summon Aery', 'Arcane Comet', 'Phase Rush', 'Grasp of the Undying', 'Aftershock Guardian',
      'Glacial Augment', 'Kleptomancy', 'Unsealed Spellbook']

# Reading the files to populate lists champs and items
with open(txt) as f:
    for line in f:
        s = line.strip().split(' ')
        champs.append(s[0])
        roles.append(s[1])
champSelect = dict(zip(champs, roles))

with open(itemsTxt) as f:
    for line in f:
        items.append(line)


# Replaces the basic !help feature, responds with formatted bot commands and usage
@client.event
async def on_message(message):
    """
    :param message: Sent in by the user. Executed by !help
    :return: Formatted command list
    """
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
        msg.add_field(name="Kill me", value="Selects a random LoL Champ, Role, Keystone, and two items. \n Usage: !km",
                      inline=False)
        msg.add_field(name="Minecraft", value="Prints out MC IP address. \n Usage: !mc",
                      inline=False)
        msg.add_field(name="GG EZ", value="Just use it \n Usage: !ggez @[user]", inline=False)
        msg.set_thumbnail(url="https://themerkle.com/wp-content/uploads/2017/05/kingdice-pr.jpg")
        msg.set_footer(text="Developed by Clam")
        await client.send_message(message.channel, embed=msg)
    await client.process_commands(message)


@client.command(name='8ball', aliases=['eight_ball', 'eightball', '8-ball'], pass_context=True)
async def eight_ball(context):
    """
    :param context: The question the user is wanting to ask
    :return: Answer to the question
    """
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
    """
    :param number: The number the user is wanting to square
    :return: Squared Number
    """
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    """
    :return: Price of bitcoin
    """
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


# randomchamp command takes input !rc and replies with a random champion
@client.command(aliases=['rc', 'rchamp'], pass_context=True)
async def randomchamp(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author.
    :return: The user's champion selection
    """
    await client.say("{0.mention}, Your Champ is: ".format(ctx.message.author) + random.choice(champs))


# randomrole command takes input !rr and replies with a random role
@client.command(aliases=['rr', 'rrole'], pass_context=True)
async def randomrole(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author.
    :return: The user's role selection
    """
    await client.say("{0.mention}, Your Role is: ".format(ctx.message.author) + random.choice(roles))


# bothroleandchamp command takes input !rac and replies with a role and champion
@client.command(aliases=['rac', 'rolechamp'], pass_context=True)
async def bothroleandchamp(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author.
    :return: The user's role and champion selection
    """
    await client.say("{0.mention}, \n Your Champ is: ".format(ctx.message.author) + random.choice(
        champs) + "\n Your Role is: " + random.choice(roles))


@client.command(aliases=['km'], pass_context=True)
async def killme(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: Returns the users Champ, Role, Keystone, and two Items
    """
    # TODO: Potentially add 6 random items, also add an if statement where if the role is jungle at least one item
    #  will be a jungle item.
    await client.say("{0.mention}, \n Your Champ is: ".format(ctx.message.author) + random.choice(
        champs) + "\n Your Role is: " + random.choice(roles) + "\n Your keystone is: " + random.choice(
        ks) + "\n Your two items are: \n" + random.choice(items) + random.choice(items))


@client.command()
async def ggez(name):
    msg = '''░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█▀▀▀░█▀▀▀░░█▀▀░▀▀█░░░░
░░░█░▀█░█░▀█░░█▀▀░▄▀░░░░░
░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░'''
    await client.say(msg + "\n" + name)

@client.command(aliases=['mc'])
async def minecraft(ctx):
    msg = discord.Embed(title='__**Minecraft Server**__', description="", color=0x0000ff)
    msg.add_field(name="IP", value="71.68.104.177:6969",
                  inline=False)
    await client.send_message(ctx.message.channel, embed=msg)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
