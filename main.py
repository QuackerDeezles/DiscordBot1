import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ';')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Subscribe to QuackerDeezles'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ya pingg is {round(client.latency * 1000)} milliseconds!')

@client.command()
async def eball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook good.',
                 'Outlook not so good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes - definitely.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def chem(ctx, *, symbol):
    elements = {
        "H":"Hydrogen, 1st, Mass of 1.008",
        "He":"Helium, 2nd, Mass of 4.0026, Noble Gas",
        "Li":"Lithium, 3rd, Mass of 6.94, Alkali Metal",
        "Be":"Beryllium, 4th, Mass of 9.0122, Alkaline Earth Metal",
        "B":"Boron, 5th, Mass of 10.81, Metalloid",
        "C":"Carbon, 6th, Mass of 12.011, Nonmetal",
        "N":"Nitrogen, 7th, Mass of 14.007, Nonmetal",
        "O":"Oxygen, 8th, Mass of 15.999, Nonmetal",
        "F":"Flourine, 9th, Mass of 18.998, Halogen",
        "Ne":"Neon, 10th, Mass of 20.180, Noble Gas",
        "Na":"Sodium, 11th, Mass of 22.990, Alkali Metal",
        "Mg":"Magnesium, 12th, Mass of 23.405, Alkaline Earth Metal",
        "Al":"Aluminum, 13th, Mass of 26.982, Other Metal",
        "Si":"Silicon, 14th, Mass of 28.085, Metalloid",
        "P":"Phosphorus, 15th, Mass of 30.974, Nonmetal",
        "S":"Sulfur, 16th, Mass of 32.06, Nonmetal",
        "Cl":"Chlorine, 17th, Mass of 35.45, Halogen",
        "Ar":"Argon, 18th, Mass of 39.948, Noble Gas",
        "K":"Potassium, 19th, Mass of 39.098, Alkali Metal"
    }
    await ctx.send(f'Symbol: {symbol}\nInformation: {elements[symbol]}')

@client.command()
async def ducc(ctx):
    await ctx.send(f'Hey there fella, I am Quacc Ducc, a bot that does what rarely other bots do. I am currently adding more things to my bot, such as adding the periodic table, and more. I suppose you want a duck emoji, so here it is! :duck:')

@client.command()
async def youtube(ctx):
    await ctx.send(f'https://www.youtube.com/channel/UC6PKOburRMFSjwTCQcL4wbQ?view_as=subscriber')

@client.command()
async def website(ctx):
    await ctx.send(f'The programmers website is here: https://talentkrazy.wixsite.com/website | chWill make a bot website soon!')

@client.command()
async def twitch(ctx):
    await ctx.send(f'https://www.twitch.tv/quackerdeezles')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def helps(ctx):
    await ctx.send(f' Commands: ;ping | ;eball | ;chem | ;ducc | ;youtube | ;website | ;twitch | ;clear | ;helps')

client.run('KEY')
