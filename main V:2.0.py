#Made by DarkSaso with <3 GitHub https://github.com/DarkSaso
#imports
import os
import time
import pyperclip
from os import system, name
#def
clear = lambda: os.system('cls')
#Credits
author = " DarkSaso "
version = " Version:2.0.0"
#edit this
psw = {
    'changeme': 'cangeme',
    'changeme1': 'cangeme1',
    'changeme2': 'cangeme2',
}
masterpsw = "1234" #master password CHANGE ME
#Code

print("██████████████████████████████████████████████████████████████████████████████████████████████████████████")
print("█▄─▄▄─██▀▄─██─▄▄▄▄█─▄▄▄▄█▄─█▀▀▀█─▄█─▄▄─█▄─▄▄▀█▄─▄▄▀███▄─▄▄▀█▄─▄▄─█▄─▀█▀─▄█▄─▄▄─█▄─▀█▀─▄█▄─▄─▀█▄─▄▄─█▄─▄▄▀█")
print("██─▄▄▄██─▀─██▄▄▄▄─█▄▄▄▄─██─█─█─█─██─██─██─▄─▄██─██─████─▄─▄██─▄█▀██─█▄█─███─▄█▀██─█▄█─███─▄─▀██─▄█▀██─▄─▄█")
print("▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀")
print("\nPassword remember by "+author + version)
mspw= input("\nenter the master password:")
if(mspw == masterpsw):
    clear()
    print("██████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("█▄─▄▄─██▀▄─██─▄▄▄▄█─▄▄▄▄█▄─█▀▀▀█─▄█─▄▄─█▄─▄▄▀█▄─▄▄▀███▄─▄▄▀█▄─▄▄─█▄─▀█▀─▄█▄─▄▄─█▄─▀█▀─▄█▄─▄─▀█▄─▄▄─█▄─▄▄▀█")
    print("██─▄▄▄██─▀─██▄▄▄▄─█▄▄▄▄─██─█─█─█─██─██─██─▄─▄██─██─████─▄─▄██─▄█▀██─█▄█─███─▄█▀██─█▄█─███─▄─▀██─▄█▀██─▄─▄█")
    print("▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀")
    print("\nPassword remember by "+author + version)
    for element in psw:
        print(" ."+element)
    sito_s = input("\nEnter the name of the service:")
    try:
        clear()
        ps_scelta = psw[sito_s]
        pyperclip.copy(ps_scelta)
        print("\nPassword found!, You are now ready to paste it :D")
        time.sleep(5)
    except:
        clear()
        print("Password not found!")
        input("Press ENTER to exit")
else:
    clear()
    print("access denied!, the program will close in 5 sec1234")
    time.sleep(5)
