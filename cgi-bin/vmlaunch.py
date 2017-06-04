#!/usr/bin/python2

import os,cgitb
import commands
import cgi

cgitb.enable()

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
vm=data.getvalue('vm')

if vm != None : 
	commands.getstatusoutput("sudo virsh start server1")
	commands.getstatusoutput("sudo virsh start server2")
	commands.getstatusoutput("sudo virsh start server3")
	commands.getstatusoutput("sudo virsh start server4")
	commands.getstatusoutput("sudo ttyecho -n /dev/pts/0 virt-manager")
	
else:	 
	"print ok"

print "<script>alert('ALL VMs STARTED, PRESS OK TO CONTINUE')</script>"
print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.0.20/services.html'/>"




