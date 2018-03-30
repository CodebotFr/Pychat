#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author: Codebot

#import module
from threading import Thread
import socket
import configparser
import os

#import config
os.getcwd()
os.chdir("./data")
config = configparser.ConfigParser()
config.read("config.ini")
default = config['DEFAULT']['FIRST_USE']

