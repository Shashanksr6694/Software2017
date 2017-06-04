#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi
import webbrowser

cgitb.enable()

#print "Content-type:text/html"
#print ""

data=cgi.FieldStorage()
http1=data.getvalue('checkhttp1')
http2=data.getvalue('checkhttp2')
http3=data.getvalue('checkhttp3')
http4=data.getvalue('checkhttp4')


mdb1=data.getvalue('checkmdb1')
mdb2=data.getvalue('checkmdb2')
mdb3=data.getvalue('checkmdb3')


nfs1=data.getvalue('checknfs1')
nfs2=data.getvalue('checknfs2')
nfs3=data.getvalue('checknfs3')


smb1=data.getvalue('checksmb1')
smb2=data.getvalue('checksmb2')
smb3=data.getvalue('checksmb3')

smtp1=data.getvalue('checksmtp1')
smtp2=data.getvalue('checksmtp2')
smtp3=data.getvalue('checksmtp3')


ftp1=data.getvalue('checkftp1')
ftp2=data.getvalue('checkftp2')
ftp3=data.getvalue('checkftp3')


gluster1=data.getvalue('checkgluster1')
gluster2=data.getvalue('checkgluster2')
gluster3=data.getvalue('checkgluster3')
gluster4=data.getvalue('checkgluster4')


############################http


if http1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/checkhttpd.yml")	

else :
	print ""	
	#print "Apache web server not installed"


if http2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/apache /etc/ansible/playbooks/http2.yml")
	
else :
	print ""
	#print "SERVICE NOT START" 


if http3 == "on" :
	b=commands.getoutput("sudo ttyecho -n /dev/pts/0 python /var/www/cgi-bin/open.py")
	

else :
	print ""
	#print "web page not hosted"


if http4 == "on" :
	b=commands.getoutput("sudo ttyecho -n /dev/pts/0 python /var/www/cgi-bin/openhttps.py")
	
else :
	print ""
	#print "no use of SSL/TLS "

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

############################glusterfs

if gluster1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/checkgluster1.yml")

else :
	print ""	
	#print " server not installed"


if gluster2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/gluster2.yml")
	
else :
	print ""
	#print "SERVICE NOT START" 


if gluster3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/peer /etc/ansible/playbooks/checkgluster3.yml")
	

else :
	print ""
	#print "no peer added"


if gluster4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/checkgluster4.yml")
	
else :
	print ""
	#print "no volume created "

#print "<META HTTP-EQUIV='refresh'  content='0; url=http://192.168.0.20/output.html'>\n"


