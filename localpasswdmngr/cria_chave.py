#!/bin/python3.13 

from sys import argv
from os import system
from os import environ 

from cryptography.fernet import Fernet
PARAMS = {
        "-d" : "--destination file"
        }
def main(args, *argv):
    if args:
        print(".\t.\t.\t.\t", args[1],"\t", args[2])
        key = Fernet.generate_key()
        print("\n=======generated key========\n\t\r")
        print(key, "\t", key.decode())
        print("\n")
        print(f"saving key in /home/kali/{args[2]}")
        print()
        system(f"echo {key.decode()} > /home/kali/{args[2]}")





        

def help_me()-> str:
    text = "  use to create a key to encrypt some data. \n"
    text += "\ttry\n\tpython cria_chave.py --destination phrase_key.txt\n"
    text += "\n"
    text += "\n"
    text += "\t-d\t--destination file\n"
    
    return text

if __name__ == "__main__":
    try:
        app = main(argv)
    except IndexError as err:
        print(help_me())

