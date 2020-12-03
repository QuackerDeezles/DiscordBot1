import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ';')

@client.command()
async def creeper(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=cPJUBQd-PNM um u asked for it here it is')

@client.command()
async def mineparody(ctx):
    random_minecraft_parodies = ['https://www.youtube.com/watch?v=cPJUBQd-PNM',
                                 'https://www.youtube.com/watch?v=5nfv_iEeC8Y',
                                 'https://www.youtube.com/watch?v=pcWWg0T1RSQ',
                                 'https://www.youtube.com/watch?v=Gl6ekgobG2k',
                                 'https://www.youtube.com/watch?v=OIWK3BD5zT8']
    await ctx.send(f'Here is your random Minecraft parody! {random.choice(random_minecraft_parodies)}')

@client.command()
async def magginoodles(ctx):
    await ctx.send(f'https://tenor.com/view/1983-maggi-noodles-halal-malaysia-cooking-gif-15639489')


@client.command()
async def deletus(ctx, amount=0):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

@client.command()
async def nexuspuk(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=kdTxybWNwL4')

@client.command()
async def omegalul(ctx):
    await ctx.send(f'https://tenor.com/view/omegalul-omega-lul-gif-9902854')

@client.command()
async def skyperoast(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=sSPIMgtcQnU')

@client.command()
async def thefatrat(ctx):
    thefatrat_songs = ['https://www.youtube.com/watch?v=p-LOXXGGeAc',
                       'https://www.youtube.com/watch?v=Gc3tqnhmf5U',
                       'https://www.youtube.com/watch?v=kL8CyVqzmkc',
                       'https://www.youtube.com/watch?v=YqrxIimmiqs',
                       'https://www.youtube.com/watch?v=B7xai5u_tnk',
                       'https://www.youtube.com/watch?v=KR-eV7fHNbM',
                       'https://www.youtube.com/watch?v=3fxq7kqyWO8',
                       'https://www.youtube.com/watch?v=jqkPqfOFmbY',
                       'https://www.youtube.com/watch?v=n8X9_MgEdCg',
                       'https://www.youtube.com/watch?v=3aLyiI2odhU']
    await ctx.send(f'Here is one of my favorite TheFatRat songs! {random.choice(thefatrat_songs)}')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.command()
async def vibincat(ctx):
    catdobevibin = [
        'https://www.youtube.com/watch?v=NUYvbT6vTPs',
        'https://www.youtube.com/watch?v=eZTS4cL4Euo',
        'https://www.youtube.com/watch?v=bFzrB-lo9k8',
        'https://www.youtube.com/watch?v=lcCZbPyfWPM'
    ]
    await ctx.send(f'Here is a vibing cat video! {random.choice(catdobevibin)}')

@client.command()
async def woooo(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=z-JRdRXiNv4 WOOOOOOO')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ya pingg is {round(client.latency * 1000)} milliseconds! Why did I make this command?')

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
async def memepeepo(ctx):
    gifs = ['https://tenor.com/view/peepo-arrive-peepo-pepe-the-frog-happy-gif-16095288',
            'https://tenor.com/view/pepe-pepe-the-frog-clapping-applause-gif-17906949',
            'https://tenor.com/view/peepo-smash-pepe-pepe-the-frog-punch-gif-16142453',
            'https://tenor.com/view/pepe-hype-hands-up-gif-17872512',
            'https://tenor.com/view/peepo-dance-pepe-cool-gif-15777418',
            'https://tenor.com/view/petthepeepo-gif-18147335',
            'https://tenor.com/view/burrito-pass-peepohappy-gif-18706235',
            'https://tenor.com/view/peepo-wtf-gif-18154652',
            'https://tenor.com/view/peepo-wiadro-good-morning-gif-18944877']
    await ctx.send(f'Here is your peepo gif! {random.choice(gifs)}')

@client.command()
async def memerobux(ctx):
    await ctx.send(f'https://tenor.com/view/roblox-robux-robuxgratis-wentis-gamer-yootube-gif-18776887 Here is your Robux you filthy rich kid')

@client.command()
async def memeyoutube(ctx):
    memes = ['https://www.youtube.com/watch?v=BPO4Gp2tHWw',
             'https://www.youtube.com/watch?v=XqZsoesa55w',
             'https://www.youtube.com/watch?v=j9V78UbdzWI',
             'https://www.youtube.com/watch?v=mKue4WuagL8',
             'https://www.youtube.com/watch?v=g9TNY75jhcs&t=3s',
             'https://www.youtube.com/watch?v=tPEQUfszEkk&has_verified=1',
             'https://www.youtube.com/watch?v=GnrwM7vFn_U',
             'https://www.youtube.com/watch?v=BJ0xBCwkg3E&t=40s',
             'https://www.youtube.com/watch?v=E9s1ltPGQOo'
             ]
    await ctx.send(f'Here is your randomized YouTube meme video! {random.choice(memes)}')


@client.command()
async def fortnitemontage(ctx):
    montages = ['https://www.youtube.com/watch?v=D7SDYCTq444&t=308s',
                'https://www.youtube.com/watch?v=2OSEQx6j74U',
                'https://www.youtube.com/watch?v=L8tCx1YpqWo',
                'https://www.youtube.com/watch?v=BE9OlU4IWlc',
                'https://www.youtube.com/watch?v=dB8OVwna09I',
                'https://www.youtube.com/watch?v=QLKDXrdm5l8',
                'https://www.youtube.com/watch?v=cj0LUew0t4Y',
                'https://www.youtube.com/watch?v=xZFy4GsCT5M&t=32s',
                'https://www.youtube.com/watch?v=0qaVwIi_gvk',
                'https://www.youtube.com/watch?v=GKt-CfZwA70&t=9s'
                ]
    await ctx.send(f'Here is a random Fortnite montage! {random.choice(montages)}')

@client.command()
async def elem(ctx, *, symbol):
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

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'DM BCC QuackerDeezlesYT#6392 to invite bot, featured in {len(client.guilds)} servers!'))
    print("ready!")

@client.command()
async def ducc(ctx):
    await ctx.send(f'Hey there fella, I am Quacc Ducc, a bot that does what rarely other bots do. I am currently adding more things to my bot, such as adding the periodic table, and more. I suppose you want a duck emoji, so here it is! :duck:')

@client.command()
async def inviteme(ctx):
    await ctx.send(f'Thank you very much! It would be very appreciative if you would invite me to your server, it really means a lot :slight_smile: Here is the link: https://discord.com/oauth2/authorize?client_id=767190721534361631&permissions=8&scope=bot Thanks!')

@client.command()
async def randomemoji(ctx):
    emojis = [':japanese_ogre:',
              ':space_invader:',
              ':shit:',
              ':tooth:',
              ':woman_detective:',
              ':mermaid:',
              ':dog:',
              ':monkey:',
              ':bagel:',
              ':archery:',
              ':musical_keyboard',
              ':video_game:',
              ':ferris_wheel:',
              ':sponge:',
              ':cool:',
              ':bagel:'
              ':archery:',
              ':musical_keyboard',
              ':video_game:',
              ':ferris_wheel:',
              ':sponge:',
              ':cool:',
    ]
    await ctx.send(f'Here is your random emoji! {random.choice(emojis)}')

@client.command()
async def socyoutube(ctx):
    await ctx.send(f'https://www.youtube.com/channel/UC6PKOburRMFSjwTCQcL4wbQ?view_as=subscriber')

@client.command()
async def socwebsite(ctx):
    await ctx.send(f'The programmers website is here: https://talentkrazy.wixsite.com/website | Will make a bot website soon!')

@client.command()
async def soctwitch(ctx):
    await ctx.send(f'https://www.twitch.tv/quackerdeezles')

@client.command()
async def musicsans(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=wDgQdr8ZkTw Megalovania, the #1 undertale song (dev opinion)')

@client.command()
async def musicrushe(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=Qskm9MTz2V4 E')

@client.command()
async def stillpesta(ctx):
    await ctx.send(f'https://tenor.com/view/npesta-stillpesta-gif-18113412 FOR THE KENOS')

client.run('NzY3MTkwNzIxNTM0MzYxNjMx.X4uUCQ.745U52MZThnSQtRilYt1eJBbiC0')
