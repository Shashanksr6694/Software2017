#!/usr/bin/python

import commands
import os
import webbrowser

os.system("sudo cat /etc/ansible/apache | cut  -d' ' -f1 | grep 192.168.122.* > /etc/ansible/httpipread.txt")

lines = [line.rstrip('\n') for line in open('/etc/ansible/httpipread.txt')]

for f in lines:
	url = 'http://'+f+'/adhoc.html'
	b = webbrowser.get('firefox')
	b.open_new_tab(url)
