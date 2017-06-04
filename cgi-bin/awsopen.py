#!/usr/bin/python

import commands
import os
import webbrowser


os.system("sudo cat /etc/ansible/awsapache | cut -s -d' ' -f1 > /etc/ansible/apacheipread.txt")

lines = [line.rstrip('\n') for line in open('/etc/ansible/apacheipread.txt')]

for f in lines:
	url = 'http://'+f+'/adhoc.html'
	b = webbrowser.get('firefox')
	b.open_new_tab(url)
