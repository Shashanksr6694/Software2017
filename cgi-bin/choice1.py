#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

cgitb.enable()

#print "Content-type:text/html"
#print ""

data=cgi.FieldStorage()
gluster1=data.getvalue('gluster1')
gluster2=data.getvalue('gluster2')
gluster3=data.getvalue('gluster3')
gluster4=data.getvalue('gluster4')
gluster5=data.getvalue('gluster5')
gluster6=data.getvalue('gluster6')

#################gluster

if gluster1 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/gluster1.yml")

else :
	print ""	
	#print "server not installed"


if gluster2 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/gluster2.yml")
	
else :
	print ""
	#print "SERVICE NOT START" 


if gluster3 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/peer /etc/ansible/playbooks/gluster3.yml")
	

else :
	print ""
	#print "no peer added"


if gluster4 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/gluster4.yml")
	
else :
	print ""
	#print "no volume created "


if gluster5 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/gluster5.yml")
	

else :
	print ""
	#print "SERVICE STOP"

if gluster6 == "on" :
	a=os.system("sudo ansible-playbook -i /etc/ansible/gluster /etc/ansible/playbooks/gluster6.yml")
	

else :
	print ""
	#print "SERVER REMOVED"
