#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author: Codebot

#import module
import threading
import socket
import configparser
import os
import time

#import config
os.getcwd()
os.chdir("./data")
config = configparser.ConfigParser()
config.read("config.ini")

#variable config
default = config['SETTINGS']['FIRST_USE']
host = config['SETTINGS']['HOST']
port = int(config['SETTINGS']['PORT'])
if default == "true":
	username = ""
else:
	username = config['SETTINGS']['USERNAME']

def Initial(default, username):
    print("---------------------------")
    print("Welcom on Pychat software !")
    print("---------------------------")

    if default == "true":
        print("\n\nWelcome on the first use configuration panel !")

        username = str(input("Please enter your username :"))
        while username == "" or username == " ":
            username = input("Please enter a correct username :")

        default = "false"

        config['SETTINGS']['USERNAME'] = username
        config['SETTINGS']['FIRST_USE'] = default

        with open('config.ini', 'w') as configfile :
            config.write(configfile)
    else:
        print('Hello ' + username)


class Server(threading.Thread):
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Server started successfully\n")
        hostname=''
        port=51412
        self.sock.bind((hostname,port))
        self.sock.listen(1)
        print("Listening on port %d\n" %port)     
        #time.sleep(2)    
        (clientname,address)=self.sock.accept()
        print("Connection from %s\n" % str(address)) 
        while 1:
            chunk=clientname.recv(4096)            
            print(str(address)+':'+str(chunk))

class Client(threading.Thread):    
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):
        msg = msg.encode()               
        self.sock.send(msg)         
        print("Sent\n")
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            lastconnexion = input("Do you want to load the last connexion ? (Y/N)")
            if lastconnexion.upper() == 'Y' :
                host = config['SETTINGS']['HOST']
                port = int(config['SETTINGS']['PORT'])
            elif lastconnexion.upper() == 'N' :
                host=input("Enter the hostname\n>>")            
                port=int(input("Enter the port\n>>"))
                config['SETTINGS']['HOST'] = host
                config['SETTINGS']['PORT'] = str(port)
                with open('config.ini', 'w') as configfile :
                    config.write(configfile)
        except EOFError:
            print("Error")
            return 1
        
        print("Connecting\n")
        self.connect(host,port)
        print("Connected\n")
        while 1:            
            print("Waiting for message\n")
            msg=input('>>')
            if msg=='exit':
                break
            if msg=='':
                continue
            print("Sending\n")
            self.client(host,port,msg)
        return(1)


if __name__=='__main__':
    try:
        Initial(default, username)
        srv=Server()
        srv.daemon=True
        print("Starting server")
        srv.start()
        time.sleep(1)
        print("Starting client")
        cli=Client()
        print("Started successfully")
        cli.start()
    except KeyboardInterrupt:
        print('GoodBye ' + username + ' !')
