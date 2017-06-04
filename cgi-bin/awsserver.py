#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

cgitb.enable()

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
awsapache=data.getvalue('awsapache')
awsmariadb=data.getvalue('awsmariadb')
awsnfs=data.getvalue('awsnfs')
awssamba=data.getvalue('awssamba')
awssmtp=data.getvalue('awssmtp')
awsftp=data.getvalue('awsftp')


if awsapache != None :
	commands.getstatusoutput("sudo echo '[http_servers]'  > /etc/ansible/awsapache")

	if str(type(awsapache))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+awsapache+" 'ansible_ssh_private_key_file=/var/www/Key/key1.pem ansible_ssh_user=ec2-user'' >> /etc/ansible/awsapache")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/awsapache")
		commands.getstatusoutput("sudo echo '[http_servers]'  > /etc/ansible/awsapache")
		
		for i in range(len(awsapache)):
			commands.getstatusoutput("sudo echo '"+awsapache[i]+" 'ansible_ssh_private_key_file=/var/www/Key/key1.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awsapache")
	
else :
	print "<script>alert('NO IP SELECTED FOR APACHE HTTP SERVER, PRESS OK TO CONTINUE')</script>"




if awsmariadb != None :
	commands.getstatusoutput("sudo echo '[mariadb_servers]'  > /etc/ansible/awsmariadb")
	
	if str(type(awsmariadb))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+awsmariadb+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awsmariadb")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/awsmariadb")
		commands.getstatusoutput("sudo echo '[mariadb_servers]'  > /etc/ansible/awsmariadb")
		for i in range(len(awsmariadb)):
			commands.getstatusoutput("sudo echo '"+awsmariadb[i]+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awsmariadb")	

else :
	print "<script>alert('NO IP SELECTED FOR MARIADB SERVER, PRESS OK TO CONTINUE')</script>"




if awsnfs != None :
	commands.getstatusoutput("sudo echo '[nfs_servers]'  > /etc/ansible/awsnfs")

	if str(type(awsnfs))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+awsnfs+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awsnfs")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/awsnfs")
		commands.getstatusoutput("sudo echo '[nfs_servers]'  > /etc/ansible/awsnfs")
		for i in range(len(awsnfs)):
			commands.getstatusoutput("sudo echo '"+awsnfs[i]+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awsnfs")
	
else :
	print "<script>alert('NO IP SELECTED FOR NFS SERVER, PRESS OK TO CONTINUE')</script>"





if awssamba != None :
	commands.getstatusoutput("sudo echo '[samba_servers]'  > /etc/ansible/awssamba")

	if str(type(awssamba))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+awssamba+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awssamba")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/awssamba")
		commands.getstatusoutput("sudo echo '[samba_servers]'  > /etc/ansible/awssamba")
		for i in range(len(awssamba)):
			commands.getstatusoutput("sudo echo '"+awssamba[i]+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awssamba")	

else :
	print "<script>alert('NO IP SELECTED FOR SAMBA SERVER, PRESS OK TO CONTINUE')</script>"





if awssmtp != None :
	commands.getstatusoutput("sudo echo '[smtp_servers]'  > /etc/ansible/awssmtp")

	if str(type(awssmtp))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+awssmtp+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awssmtp")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/awssmtp")
		commands.getstatusoutput("sudo echo '[smtp_servers]'  > /etc/ansible/awssmtp")
		for i in range(len(awssmtp)):
			commands.getstatusoutput("sudo echo '"+awssmtp[i]+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awssmtp")	

else :
	print "<script>alert('NO IP SELECTED FOR SMTP SERVER, PRESS OK TO CONTINUE')</script>"







if awsftp != None :
	commands.getstatusoutput("sudo echo '[ftp_servers]'  > /etc/ansible/awsftp")

	if str(type(awsftp))  == "<type 'str'>": 
		commands.getstatusoutput("sudo echo '"+awsftp+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awsftp")
	else :
		#commands.getstatusoutput("sudo echo   > /etc/ansible/awsftp")
		commands.getstatusoutput("sudo echo '[ftp_servers]'  > /etc/ansible/awsftp")
		for i in range(len(awsftp)):
			commands.getstatusoutput("sudo echo '"+awsftp[i]+" 'ansible_ssh_private_key_file=/var/www/Key/key2.pem ansible_ssh_user=ec2-user''  >> /etc/ansible/awsftp")	

else :
	print "<script>alert('NO IP SELECTED FOR FTP SERVER, PRESS OK TO CONTINUE')</script>"






if awsapache==None and awsmariadb==None and awsnfs==None and awssamba==None and awssmtp==None and awsftp==None:
	print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/cgi-bin/ec2table.py'>\n"
else :
	print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/awschoice.html'>\n"












