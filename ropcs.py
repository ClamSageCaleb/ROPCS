__author__ = "ClamSageCaleb"
__copyright__ = "Copyright 2019, MIT License"
__credits__ = "ClamSageCaleb"
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "ClamSageCaleb"
__status__ = "Production"

import random
import json
import discord
from discord.ext import commands

# Bot prefix and Discord Bot token
BOT_PREFIX = ("!")

# Insert your own Token here
TOKEN = " "
game = discord.Game("with the API")

# Creates the Bot with name 'client'
client = commands.Bot(command_prefix=BOT_PREFIX)
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
        # Splits the txt file by the space character and then puts champs in the champs list and the
        # roles into the roles list.
        s = line.strip().split(' ')
        champs.append(s[0])
        roles.append(s[1])
# Zips roles and champs into a dictionary. Champion name is the key and the role is the value
champSelect = dict(zip(champs, roles))

# Reads items from the items.txt and adds it to items list.
with open(itemsTxt) as f:
    for line in f:
        items.append(line)

# Replaces the basic !help feature, responds with formatted bot commands and usage
@client.event
async def on_message(ctx):
    """
    :param ctx: Sent in by the user. Executed by !help
    :return: Formatted command list
    """
    if ctx.author == client.user:
        return

    if ctx.content.startswith('!help'):
        msg = discord.Embed(title='__**Scrub Bot Commands**__', description="", color=0x0000ff)
        msg.add_field(name="Random Champ", value="Selects a random LoL Champion. \n Usage: !rc", inline=False)
        msg.add_field(name="Stats", value="Get the OP.GG stats of a champion. \n Usage: !st [champ name]", inline=False)
        msg.add_field(name="Summoner", value="Get the OP.GG stats of a player. \n Usage: !pl [player]", inline=False)
        msg.add_field(name="Options", value="List ALL Champions. \n Usage: !opt", inline=False)
        msg.add_field(name="Top", value="List ALL TOP Champions. \n Usage: !top", inline=False)
        msg.add_field(name="Mid", value="List ALL MID Champions. \n Usage: !mid", inline=False)
        msg.add_field(name="ADC", value="List ALL ADC Champions. \n Usage: !adc", inline=False)
        msg.add_field(name="Support", value="List ALL SUPPORT Champions. \n Usage: !supp", inline=False)
        msg.add_field(name="Jungle", value="List ALL JUNLGE Champions. \n Usage: !jg", inline=False)
        msg.add_field(name="Random Role", value="Selects a random LoL Role. \n Usage: !rr", inline=False)
        msg.add_field(name="Combo Role/Champ", value="Selects a random LoL Role and Champion. \n Usage: !rac",
                      inline=False)
        msg.add_field(name="Kill me", value="Selects a random LoL Champ, Role, Keystone, and two items. \n Usage: !km",
                      inline=False)
        msg.add_field(name="GG EZ", value="Just use it \n Usage: !ggez [user]", inline=False)
        msg.add_field(name="Vote", value="Use it to cast votes. \n Usage: !v [topic]")
        msg.add_field(name="Note", value="Development Information. \n Usage: !info")
        msg.set_thumbnail(url="http://scrubhubkc.com/wp-content/uploads/2014/05/logo_large.png")
        msg.set_footer(text="Developed by Clam")
        await ctx.channel.send(embed=msg)
    await client.process_commands(ctx)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=game)
    print("Logged in as " + client.user.name)

# Lists all of the application info
@client.command()
async def info(ctx):
    msg = discord.Embed(title='__**Scrub Bot**__', description="", color=0x0000ff)
    msg.add_field(name="Contributors", value=__author__, inline=False)
    msg.add_field(name="Copyright", value=__copyright__, inline=False)
    msg.add_field(name="License", value=__license__, inline=False)
    msg.add_field(name="Version", value=__version__, inline=False)
    msg.add_field(name="Maintainer", value=__maintainer__, inline=False)
    msg.add_field(name="Email", value= __email__, inline=False)
    msg.add_field(name="Status", value= __status__, inline=False)
    msg.set_thumbnail(url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/f0/f0936f1b28b2b9ad67c52ef775a52284cf93a950_full.jpg")
    await ctx.send(embed=msg)


# randomchamp command takes input !rc and replies with a random champion
@client.command(aliases=['rc', 'rchamp'], pass_context=True)
async def randomchamp(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author.
    :return: The user's champion selection
    """
    await ctx.send("{0.mention}, Your Champ is: ".format(ctx.message.author) + random.choice(champs))


# randomrole command takes input !rr and replies with a random role
@client.command(aliases=['rr', 'rrole'], pass_context=True)
async def randomrole(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author.
    :return: The user's role selection
    """
    await ctx.send("{0.mention}, Your Role is: ".format(ctx.message.author) + random.choice(roles))


# bothroleandchamp command takes input !rac and replies with a role and champion
@client.command(aliases=['rac', 'rolechamp'], pass_context=True)
async def bothroleandchamp(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author.
    :return: The user's role and champion selection
    """
    await ctx.send("{0.mention}, \n Your Champ is: ".format(ctx.message.author) + random.choice(
        champs) + "\n Your Role is: " + random.choice(roles))


@client.command(aliases=['km'], pass_context=True)
async def killme(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: Returns the users Champ, Role, Keystone, and two Items
    """
    # TODO: Potentially add 6 random items, also add an if statement where if the role is jungle at least one item
    #  will be a jungle item.
    ranChamp = random.choice(champs)
    champName = ranChamp.title()
    msg = discord.Embed(title='__**' + champName +  '**__', description="", color=0x0000ff)
    msg.add_field(name="Role:", value= random.choice(roles), inline=False)
    msg.add_field(name="Keystone:", value= random.choice(ks), inline=False)
    msg.add_field(name="Two required items (For Entire Game):", value= random.choice(items) + "\n" + random.choice(items), inline=False)
    msg.set_thumbnail(url="https://opgg-static.akamaized.net/images/lol/champion/" + champName + "?image=q_auto,w_140&v=1581511032")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# options Lists all of the potential champions and roles
@client.command(aliases=['opt'], pass_context=True)
async def options(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: ALL Champs and Roles
    """
    midList = []
    topList = []
    botList = []
    suppList = []
    jgList = []
    await ctx.send("Here, have a look at the options! \n" + ctx.message.author.mention + "\n")
    for key in champSelect:
        if champSelect[key] == 'Mid':
            midList.append(key)
    midStr = ', '.join(midList)
   
    
    for key in champSelect:
        if champSelect[key] == 'Top':
            topList.append(key)
    topStr = ', '.join(topList)
    
   
    for key in champSelect:
        if champSelect[key] == 'ADC':
            botList.append(key)
    botStr = ', '.join(botList)
    
   
    for key in champSelect:
        if champSelect[key] == 'Support':
            suppList.append(key)
    suppStr = ', '.join(suppList)
   
    for key in champSelect:
        if champSelect[key] == 'Jungle':
            jgList.append(key)
    jgStr = ', '.join(jgList)

    msg = discord.Embed(title='__**Champions & Roles**__', description="", color=0x0000ff)
    msg.add_field(name="Top", value= topStr, inline=False)
    msg.add_field(name="Jungle", value=jgStr, inline=False)
    msg.add_field(name="Mid", value= midStr, inline=False)
    msg.add_field(name="ADC", value= botStr, inline=False)
    msg.add_field(name="Support", value=suppStr, inline=False)
    msg.set_thumbnail(url="https://dl2.macupdate.com/images/icons256/47210.png?d=1362775965")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Lists all Mid Champs 
@client.command()
async def mid(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: Returns all Mid Champs
    """
    midList = []
    for key in champSelect:
        if champSelect[key] == 'Mid':
            midList.append(key)
    midStr = ', '.join(midList)
    msg = discord.Embed(title='__**Mid Lane**__', description="", color=0x0000ff)
    msg.add_field(name="Champions", value= midStr, inline=False)
    msg.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/9/98/Middle_icon.png/revision/latest?cb=20181117143644")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Lists all Top Champs
@client.command()
async def top(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: Returns all Top champs
    """
    topList = []
    for key in champSelect:
        if champSelect[key] == 'Top':
            topList.append(key)
    topStr = ', '.join(topList)
    msg = discord.Embed(title='__**Top Lane**__', description="", color=0x0000ff)
    msg.add_field(name="Champions", value= topStr, inline=False)
    msg.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/e/ef/Top_icon.png/revision/latest?cb=20181117143602")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Lists all Support Champs
@client.command()
async def supp(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: Returns all support champs
    """
    suppList = []
    for key in champSelect:
        if champSelect[key] == 'Support':
            suppList.append(key)
    suppStr = ', '.join(suppList)
    msg = discord.Embed(title='__**Support**__', description="", color=0x0000ff)
    msg.add_field(name="Champions", value= suppStr, inline=False)
    msg.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/e/e0/Support_icon.png/revision/latest?cb=20181117143601")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Lists all ADC champs
@client.command()
async def adc(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: Returns all ADC champs
    """
    botList = []
    for key in champSelect:
        if champSelect[key] == 'ADC':
            botList.append(key)
    botStr = ', '.join(botList)
    msg = discord.Embed(title='__**ADC**__', description="", color=0x0000ff)
    msg.add_field(name="Champions", value= botStr, inline=False)
    msg.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/9/97/Bottom_icon.png/revision/latest?cb=20181117143632")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Lists all jungle champs
@client.command()
async def jg(ctx):
    """
    :param ctx: Takes the user's message in order to extract the author
    :return: Returns all Jungle champs
    """
    jgList = []
    for key in champSelect:
        if champSelect[key] == 'Jungle':
            jgList.append(key)
    jgStr = ', '.join(jgList)
    msg = discord.Embed(title='__**Support**__', description="", color=0x0000ff)
    msg.add_field(name="Champions", value= jgStr, inline=False)
    msg.set_thumbnail(url="https://vignette.wikia.nocookie.net/leagueoflegends/images/0/05/Smite.png/revision/latest?cb=20180514003641")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Takes the user arugement of champName and creates a url for OP.GG based on champion
@client.command(aliases=['st'], pass_context=True)
async def stat(ctx, champName):
    """
    :param ctx: Takes the user's message in order to extract the author
    :param champName: Used to create URL for OP.GG
    :return: Returns the link to OP.GG for given champion
    """
    link = "https://op.gg/champion/" + champName
    champName = champName.title()
    msg = discord.Embed(title='__**' + champName +  ' Build**__', description="", color=0x0000ff, url=link)
    msg.add_field(name=champName + " Build", value= "This will increase win chance by 100%", inline=False)
    msg.set_thumbnail(url="https://opgg-static.akamaized.net/images/lol/champion/" + champName + "?image=q_auto,w_140&v=1581511032")
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Takes the user argument of name and creates a url for OP.GG based on player
@client.command(aliases=['pl'], pass_context=True)
async def summoner(ctx, name):
    """
    :param ctx: Takes the user's message in order to extract the author
    :param name: Used to create URL for OP.GG
    :return: Returns the link to OP.GG for given player
    """
    link = "https://op.gg/summoner/userName=" + name
    msg = discord.Embed(title='__**' + name +  ' Stats**__', description="", color=0x0000ff, url=link)
    msg.add_field(name=name + " Stats", value= "Flame their Win/Rate", inline=False)
    msg.set_footer(text="Developed by Clam")
    await ctx.channel.send(embed=msg)

# Creates a poll with a user-generated question
@client.command(aliases=['v'], pass_context=True)
async def vote(ctx, *args):
    """
    :param ctx: Takes the user's message in order to extract the author
    :param *args: Takes the users arguements after the !v command in chat
    :return: A poll with pre applied reactions
    """
    question = '{}'.format(' '.join(args))
    await ctx.message.delete()
    author = ctx.message.author
    msg = discord.Embed(title='** {} asked: ' + question + '**'.format(author), description="", color=0x0000ff)
    msg.add_field(name='Place your votes!', value="✅ YES \n\n ❌ NO", inline=True)
    r = await ctx.channel.send(embed=msg)
    await discord.Message.add_reaction(r, "✅")
    await discord.Message.add_reaction(r, "❌")

@client.command()
async def ggez(ctx, name):
    msg = '''░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█▀▀▀░█▀▀▀░░█▀▀░▀▀█░░░░
░░░█░▀█░█░▀█░░█▀▀░▄▀░░░░░
░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░'''
    await ctx.send(msg + "\n" + name)


client.run(TOKEN)
