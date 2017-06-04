#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

cgitb.enable()

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
apache=data.getvalue('apache')
mariadb=data.getvalue('mariadb')
nfs=data.getvalue('nfs')
samba=data.getvalue('samba')
smtp=data.getvalue('smtp')
ftp=data.getvalue('ftp')


if apache != None :
	commands.getstatusoutput("sudo echo '[apache]'  > /etc/ansible/apache")

	if str(type(apache))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+apache+"' >> /etc/ansible/apache")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/apache")
		commands.getstatusoutput("sudo echo '[apache]'  > /etc/ansible/apache")
		for i in range(len(apache)):
			commands.getstatusoutput("sudo echo '"+apache[i]+"'  >> /etc/ansible/apache")
	
else :
	print "<script>alert('NO IP SELECTED FOR APACHE HTTP SERVER, PRESS OK TO CONTINUE')</script>"




if mariadb != None :
	commands.getstatusoutput("sudo echo '[mariadb]'  > /etc/ansible/mariadb")
	
	if str(type(mariadb))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+mariadb+"'  >> /etc/ansible/mariadb")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/mariadb")
		commands.getstatusoutput("sudo echo '[mariadb]'  > /etc/ansible/mariadb")
		for i in range(len(mariadb)):
			commands.getstatusoutput("sudo echo '"+mariadb[i]+"'  >> /etc/ansible/mariadb")	

else :
	print "<script>alert('NO IP SELECTED FOR MARIADB SERVER, PRESS OK TO CONTINUE')</script>"




if nfs != None :
	commands.getstatusoutput("sudo echo '[nfs]'  > /etc/ansible/nfs")

	if str(type(nfs))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+nfs+"'  >> /etc/ansible/nfs")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/nfs")
		commands.getstatusoutput("sudo echo '[nfs]'  > /etc/ansible/nfs")
		for i in range(len(nfs)):
			commands.getstatusoutput("sudo echo '"+nfs[i]+"'  >> /etc/ansible/nfs")
	
else :
	print "<script>alert('NO IP SELECTED FOR NFS SERVER, PRESS OK TO CONTINUE')</script>"





if samba != None :
	commands.getstatusoutput("sudo echo '[samba]'  > /etc/ansible/samba")

	if str(type(samba))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+samba+"'  >> /etc/ansible/samba")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/samba")
		commands.getstatusoutput("sudo echo '[samba]'  > /etc/ansible/samba")
		for i in range(len(samba)):
			commands.getstatusoutput("sudo echo '"+samba[i]+"'  >> /etc/ansible/samba")	

else :
	print "<script>alert('NO IP SELECTED FOR SAMBA SERVER, PRESS OK TO CONTINUE')</script>"





if smtp != None :
	commands.getstatusoutput("sudo echo '[smtp]'  > /etc/ansible/smtp")

	if str(type(smtp))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+smtp+"'  >> /etc/ansible/smtp")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/smtp")
		commands.getstatusoutput("sudo echo '[smtp]'  > /etc/ansible/smtp")
		for i in range(len(smtp)):
			commands.getstatusoutput("sudo echo '"+smtp[i]+"'  >> /etc/ansible/smtp")	

else :
	print "<script>alert('NO IP SELECTED FOR SMTP SERVER, PRESS OK TO CONTINUE')</script>"







if ftp != None :
	commands.getstatusoutput("sudo echo '[ftp]'  > /etc/ansible/ftp")

	if str(type(ftp))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+ftp+"'  >> /etc/ansible/ftp")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/ftp")
		commands.getstatusoutput("sudo echo '[ftp]'  > /etc/ansible/ftp")
		for i in range(len(ftp)):
			commands.getstatusoutput("sudo echo '"+ftp[i]+"'  >> /etc/ansible/ftp")	

else :
	print "<script>alert('NO IP SELECTED FOR FTP SERVER, PRESS OK TO CONTINUE')</script>"






if apache==None and mariadb==None and nfs==None and samba==None and smtp==None and ftp==None:
	print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/cgi-bin/table.py'>\n"
else :
	print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/choice.html'>\n"












