#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

cgitb.enable()

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
gluster=data.getvalue('gluster')


if gluster != None :
	commands.getstatusoutput("sudo echo '[gluster]'  > /etc/ansible/gluster")
	
	if str(type(gluster))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+gluster+"'  >> /etc/ansible/gluster")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/gluster")
		commands.getstatusoutput("sudo echo '[gluster]'  > /etc/ansible/gluster")
		
		for i in range(len(gluster)):
			commands.getstatusoutput("sudo echo '"+gluster[i]+"'  >> /etc/ansible/gluster")
			commands.getstatusoutput("sudo echo '[peer]'  > /etc/ansible/peer")
			commands.getstatusoutput("sudo echo '"+gluster[0]+"'  >> /etc/ansible/peer")
			commands.getstatusoutput("sudo echo '[probing]'  >> /etc/ansible/peer")
			commands.getstatusoutput("sudo echo '"+gluster[1]+"'  >> /etc/ansible/peer")
			commands.getstatusoutput("sudo echo '"+gluster[2]+"'  >> /etc/ansible/peer")
			commands.getstatusoutput("sudo echo '"+gluster[3]+"'  >> /etc/ansible/peer")
			


else :
	print "<script>alert('NO IP SELECTED FOR GLUSTERFS, PRESS OK TO CONTINUE')</script>"


if gluster==None :
	print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/cgi-bin/table1.py'>\n"

else :

	print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/choice1.html'>\n"





