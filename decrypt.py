from AesEverywhere import aes256
from colorama import Fore
import os 
def mass_decrypt(folder_path , password):
    try:
        files = os.listdir(folder_path)
        os.chdir(folder_path)
        for file in files:
            decrypt(file , password)
        print(Fore.GREEN + f'You SuccessFully Decrypted ==> {folder_path}')
    except FileExistsError:
        print(Fore.RED + 'Folder Not Found ?!')

def decrypt(filename , password):
    with open(filename , 'r') as file:
        encrypted_data = file.read()
        file.close()
    decrypted_data = aes256.decrypt(encrypted_data , password)
    if decrypted_data == b'':
        print(Fore.RED + f'{filename} Incorrect Password !')
    else:
        with open(filename , 'w') as file:
            file.write(decrypted_data.decode())
            print(Fore.GREEN + f'You Successfully Decrypted => {filename}')
            file.close()
        