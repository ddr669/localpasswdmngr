#!/bin/python3.13
#-*-encode: utf-8-*-
#-*-By: __DDr669__-*-
#-*-Date: __/__/__-*-

#import db_con 
import threading
from os import system
from platform import system as operational
import socket


SRC_LOG = "//var//log//api_.log" if operational == "Linux" else "api_.log"
print(f"[ . ] Log source: {SRC_LOG}")

def recv_conn(conn, host):
        print("connection from~: ", host)
        conn.send(bytes("[rest~api]\r\n200\tHi\r\n\tI,am a local api that save encrypted passwords\r\n\t>>").encode("utf-8"))
        stdout_log(host, conn.recv(1024).decode())
        conn.send(bytes("[rest~api]\r\n200\tUser, accept\r\n>>"))
        stdout_log(host, conn.recv(1024).decode())
def stdout_log(host, msg):
        global SRC_LOG
        try:
                with open(SRC_LOG, "w") as a:
                        a.write(f"[{host}~:] {msg}\n")
		
        except FileNotFoundError as err:
                SRC_LOG = "api_.log"
                system("echo > api_.log")
                print("[ ! ] log initializated ... ")
def _main():
        host = "192.168.1.103"
        port = 4445

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(5)
        
        while True:
                thread_01 = threading.Thread(recv_conn, s.accept())
                thread_01.start()
        thread_01.join()
        



if __name__ == "__main__":
	#app = stdout_log("EU", "ola")
        app = _main()
                

