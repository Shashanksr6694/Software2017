#!/usr/bin/python
import os,cgitb
import commands
import cgi

cgitb.enable()
print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
first=data.getvalue('OS Image')
last=data.getvalue('CPU')
username=data.getvalue('Type')
password=data.getvalue('passwd')
cpassword=data.getvalue('passwd1')

checkme=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep " + username + " | awk '{print $1}'")

print checkme[1]
print username

if username == checkme[1] :  

	print "<script>alert('user already exist')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.0.20/login.html'/>"

else : 
	if password == cpassword :
	
		f=open("/var/www/html/users.txt",'a+')
		f.write(username + " : " + password + "\n")
		f.close()
		 
		commands.getstatusoutput("sudo useradd  " + username)
		commands.getstatusoutput("sudo echo '"+cpassword+"' |sudo passwd " + username + " --stdin ")
                print "<script>alert('User Created, Please Login to Continue')</script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.0.20/login.html'/>"
	else :
	
		print "<script>alert('PASS WRONzg')</script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.0.20/login.html'/>"

	
