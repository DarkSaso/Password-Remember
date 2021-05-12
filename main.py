#GitHub https://github.com/DarkSaso
#imports
import os
import time
import pyperclip
#Credits
author = " DarkSaso "
version = " Version:1.0.0"
#code
psw = {
    'servicename': 'password',
    'servicename1': 'password',
    'servicename2': 'password',
}#edit this
print("Password remember by "+author + version)
masterpsw = "1234" #master password
mspw= input("enter the master password:")
if(mspw == masterpsw):
    print("Login...")
    for sito in psw:
        print(" ."+sito)
    sito_s = input("Enter the name of the service:")
#Debug system
    try:
        ps_scelta = psw[sito_s]
        pyperclip.copy(ps_scelta)
        print("\nPassword found!, You are now ready to paste it: D")
        time.sleep(5)
    except:
        print("Password not found!")
        input("Press ENTER to exit")
else:
    print("access denied!, the program will close in 5 sec")
    time.sleep(5)
#made by DarkSaso with <3
