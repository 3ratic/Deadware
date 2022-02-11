import os, time
from colorama import Fore, init

init()

try:
    print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']', Fore.WHITE + 'Starting Builder')
    time.sleep(2)
    os.system('pyinstaller deadcord.py --onefile --uac-admin')
except:
    print(Fore.WHITE + '[' + Fore.RED + '+' + Fore.WHITE + ']', Fore.WHITE + 'You do not have pyinstaller')
    os.system('pip3 install pyinstaller')
    os.system('pyinstaller deadcord.py --onefile --uac-admin')