#!/usr/bin/python

import commands
import os

os.system("sudo nmap -sP 192.168.122.* --exclude 192.168.122.1 > nmap.txt")
os.system("sudo cat nmap.txt | grep -i Nmap | cut -f5 -d' ' | grep 192.* >ipread.txt")
