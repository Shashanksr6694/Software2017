#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi
import webbrowser

cgitb.enable()

#print "Content-type:text/html"
#print ""

data=cgi.FieldStorage()
http1=data.getvalue('http1')
http2=data.getvalue('http2')
http3=data.getvalue('http3')
http4=data.getvalue('http4')
http5=data.getvalue('http5')
http6=data.getvalue('http6')

mdb1=data.getvalue('mdb1')
mdb2=data.getvalue('mdb2')
mdb3=data.getvalue('mdb3')
mdb4=data.getvalue('mdb4')
mdb5=data.getvalue('mdb5')
mdb6=data.getvalue('mdb6')

nfs1=data.getvalue('nfs1')
nfs2=data.getvalue('nfs2')
nfs3=data.getvalue('nfs3')
nfs4=data.getvalue('nfs4')
nfs5=data.getvalue('nfs5')
nfs6=data.getvalue('nfs6')

smb1=data.getvalue('smb1')
smb2=data.getvalue('smb2')
smb3=data.getvalue('smb3')
smb4=data.getvalue('smb4')
smb5=data.getvalue('smb5')
smb6=data.getvalue('smb6')

smtp1=data.getvalue('smtp1')
smtp2=data.getvalue('smtp2')
smtp3=data.getvalue('smtp3')
smtp4=data.getvalue('smtp4')
smtp5=data.getvalue('smtp5')
smtp6=data.getvalue('smtp6')

ftp1=data.getvalue('ftp1')
ftp2=data.getvalue('ftp2')
ftp3=data.getvalue('ftp3')
ftp4=data.getvalue('ftp4')
ftp5=data.getvalue('ftp5')
ftp6=data.getvalue('ftp6')


############################http


if http1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/http1.yml")	

else :
	print ""	
	#print "Apache web server not installed"


if http2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/http2.yml")
	
else :
	print ""
	#print "SERVICE NOT START" 


if http3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/http3.yml")
	b=commands.getoutput("sudo ttyecho -n /dev/pts/0 python /var/www/cgi-bin/open.py")
	

else :
	print ""
	print ""
	#print "web page not hosted"


if http4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/http4.yml")
	b=commands.getoutput("sudo ttyecho -n /dev/pts/0 python /var/www/cgi-bin/openhttps.py")
	
else :
	print ""
	print ""
	#print "no use of SSL/TLS "


if http5 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/http5.yml")
	

else :
	print ""
	#print "SERVICE STOP"

if http6 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/http6.yml")
	

else :
	print ""
	#print "SERVER REMOVED"



##########################mariadb
if mdb1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/mariadb /etc/ansible/playbooks/mdb1.yml")
	 

else :
	print ""
	#print "mariadb server not installed"


if mdb2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/mariadb /etc/ansible/playbooks/mdb2.yml")
	
else :
	print ""	
	#print "SERVICE NOT START"


if mdb3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/mariadb /etc/ansible/playbooks/mdb3.yml")
	 

else :
	print ""
	#print "no security"


if mdb4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/mariadb /etc/ansible/playbooks/mdb4.yml")
	
else :
	print ""
	#print "no configuration"


if mdb5 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/mariadb /etc/ansible/playbooks/mdb5.yml")
	

else :
	print ""
	#print "SERVICE STOP"


if mdb6 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/mariadb /etc/ansible/playbooks/mdb6.yml")
	

else :
	print ""
	#print "SERVER REMOVED"




##############################nfs


if nfs1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/nfs /etc/ansible/playbooks/nfs1.yml")
	

else :
	print ""
	#print "nfs server not installed"


if nfs2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/nfs /etc/ansible/playbooks/nfs2.yml")
	
else :
	print ""
	#print "SERVICE NOT START"


if nfs3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/nfs /etc/ansible/playbooks/nfs3.yml")
	

else :
	print ""
	#print "no configuration"


if nfs4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/nfs /etc/ansible/playbooks/nfs4.yml")
	
else :
	print ""
	#print "no sharing"


if nfs5 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/nfs /etc/ansible/playbooks/nfs5.yml")
	

else :
	print ""
	#print "SERVICE STOP"


if nfs6 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/nfs /etc/ansible/playbooks/nfs6.yml")
	 

else :
	print ""
	#print "SERVER REMOVED"




############################samba

if smb1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/samba /etc/ansible/playbooks/smb1.yml")
	 

else :
	print ""
	#print "Samba server not installed"


if smb2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/samba /etc/ansible/playbooks/smb2.yml")
	
else :
	print ""
	#print "SERVICE NOT START"


if smb3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/samba /etc/ansible/playbooks/smb3.yml")
	 

else :
	print ""
	#print "no configuration"


if smb4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/samba /etc/ansible/playbooks/smb4.yml")
	
else :
	print ""
	#print "no sharing"


if smb5 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/samba /etc/ansible/playbooks/smb5.yml")
	 

else :
	print ""
	#print "SERVICE STOP"


if smb6 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/samba /etc/ansible/playbooks/smb6.yml")
	

else :
	print ""
	#print "SERVER REMOVED"








############################smtp

if smtp1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/smtp /etc/ansible/playbooks/smtp1.yml")
	

else :
	print ""
	#print "Smtp server not installed"


if smtp2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/smtp /etc/ansible/playbooks/smtp2.yml")
	
else :
	print ""
	#print "SERVICE NOT START"


if smtp3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/smtp /etc/ansible/playbooks/smtp3.yml")
	 

else :
	print ""
	#print "no configuration management"


if smtp4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/smtp /etc/ansible/playbooks/smtp4.yml")
	
else :
	print ""
	#print "no security"


if smtp5 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/smtp /etc/ansible/playbooks/smtp5.yml")
	

else :
	print ""
	#print "SERVICE STOP"


if smtp6 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/smtp /etc/ansible/playbooks/smtp6.yml")
	

else :
	print ""
	#print "SERVER REMOVED"







############################ftp

if ftp1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/ftp /etc/ansible/playbooks/ftp1.yml")
	

else :
	print ""
	#print "FTP server not installed"


if ftp2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/ftp /etc/ansible/playbooks/ftp2.yml")
	
else :
	print ""
	#print "SERVICE NOT START"


if ftp3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/ftp /etc/ansible/playbooks/ftp3.yml")
	

else :
	print ""
	#print "no configuration"


if ftp4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/ftp /etc/ansible/playbooks/ftp4.yml")
	
else :
	print ""
	#print "no security"


if ftp5 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/ftp /etc/ansible/playbooks/ftp5.yml")
	

else :
	print ""
	#print "SERVICE STOP"


if ftp6 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/ftp /etc/ansible/playbooks/ftp6.yml")
	 

else :
	print ""
	#print "SERVER REMOVED"


#print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/output.html'>\n"













