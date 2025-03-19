#!/bin/python3.13
#-*-code:utf-8-*-
#-*-By:__DDr669__-*-
#-*-date:__/__/__-*-

import mariadb
from cryptography.fernet import Fernet
import sys

def get_id_from(cur, con)-> int:
    # get last id from server 
    cur.execute("select id from users;")
    users_id = []
    for a in cur:
        users_id.append(a)
    print(users_id[0][-1])
    return users_id[0][-1]

def decry_(key, byte_hash):
    f = Fernet(key)
    t = f.decrypt(byte_hash)
    return t

def encry_(key, text: str):
    f = Fernet(key)
    t = f.encrypt(bytes(text.encode("utf-8")))
    return t

def get_key(src = "//home//kali//chaves.txt"):
    # public key generated with cria_chave.py -d source 
    with open(src, "r") as a:
        text=""
        text+=a.read()
        return text.strip()
def conexao():
    # localhost or remote 
    # just do it with sure and ethical purposes

    host = "192.168.1.103"

    port = 3306
    try: 
        con = mariadb.connect(user="root",
                              password="1234",
                              host=host,
                              port=port,
                              database="home")
    except mariadb.Error as e:
        print(f"Error connecting to host: {e}")
        sys.exit(1)

    cur = con.cursor()
    return cur, con


def exec_query(cursor, query)-> int:
    # default maria db exec_query
    try:
        cursor.execute(query)
        
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 1
    # check if the cursor is on
    print(cursor)
    return 0

def get_server_data(cur, con):
    cur.execute("select name, pasw from users;")
    # get from localhost database 
    # if you want to remote access just change the host 

    data  = {}
    for (name, pasw) in cur:
        data[name] = pasw
        
    return data

# its supposed to be main 
def main(user: str | bytes , password: str | bytes):

    key = get_key()
    # get base64_codelike key from /home/kali/chaves.txt 
    # if that dont work maybe its the src="your_phrase_key.txt"
    if sys.argv[1] == "-d":
        cur, con = conexao()
        show_the_magik(cur, con, key)
        con.close()
        return 0
    en1 = encry_(key, user)
    # change this to a api-rest socket side
    #en1  = encry_(key, input("digite seu usuario: \ntype username: "))
    # change this to a api-rest socket side
    en2 = encry_(key, password)
    #en2  = encry_(key, input("digite sua senha: \ntype password: "))
    
    print("phrase 01: lenght ===", len(en1),"b","\n","phrase 02: lenght ===", len(en2), "b")
    cur, con = conexao()

    next_id = get_id_from(cur, con) + 1
    # get the current id from database 
    print(next_id)


    exec_query(cur, f"insert into users (id, name, pasw) values({next_id},\"{en1.decode()}\",\"{en2.decode()}\")")

    # make sure to commit and close
    con.commit()
    con.close()

def show_the_magik(cur, con, key):
    # break the rules 
    data = get_server_data(cur, con)
    # deprecate :P
    print(data)

    print("\n\n\n")
    print("="*64)
    for a in data:
        print(f"decryptin = {decry_(key, a)}")
        print(f"decryptin pass = {decry_(key, data[a])}")


#exec_query(cur, f"insert into users(id, name, pasw) values(0, \"{en1.decode()}\", \"{en2.decode()}\")")

if __name__ == "__main__":
    app = main(user = input(">>"),
     password = input(">>"))




