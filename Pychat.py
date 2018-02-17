#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Author: Codebot

#import module
import sys
import os
from threading import Thread
import socket
import xml.etree.ElementTree as ET
#import lxml

#import local files
os.chdir(os.getcwd() + "/data/")
tree = ET.parse('settings.xml')
root = tree.getroot()
for username in root.iter("username"):
	if username.text is None :
		nusername = input("username :")
		username.text = nusername
	else:
		print(username.text)