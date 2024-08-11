from AesEverywhere import aes256
from src import *
from colorama import Fore
from encrypt import *
from decrypt import *
print(Fore.CYAN + icon)

option = input(Fore.RED + '[1]-Encrypt\n[2]-Decrypt\n[99]-Exit\n==>')
if option == '1':
    option = input(Fore.RED + '[1]-Single File\n[2]-Mass Files\n==>')
    if option == '1':
        filename = input('Filename :')
        password = input('Password :')
        if filename and password:
            encrypt(filename , password)
    elif option == '2':
        folder_path = input('Folder_Path :')
        password = input('Password :')
        if folder_path and password:
            mass_encrypt(folder_path , password)
elif option == '2':
    option = input(Fore.RED + '[1]-Single File\n[2]-Mass Files\n==>')
    if option == '1':
        filename = input('Filename :')
        password = input('Password :')
        if filename and password:
            decrypt(filename , password)
    elif option == '2':
        folder_path = input('Folder_Path :')
        password = input('Password :')
        if folder_path and password:
            mass_decrypt(folder_path , password)