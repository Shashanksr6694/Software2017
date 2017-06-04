#!/usr/bin/python
import commands

#a=commands.getstatusoutput("sudo fdisk -l /dev/vda  | tail -1 | awk '{print $1}'")
#if a[1] != None : 
	#commands.getoutput("sudo pvcreate "+a[1])
	#commands.getoutput("sudo vgcreate smbvg "+a[1])
	commands.getoutput("sudo lvcreate --name smblv --size 1G smbvg")
	#commands.getoutput("sudo mkfs.xfs /dev/nfsvg/nfslv")
	#commands.getoutput("sudo mkdir /mnt/nfs")
	#commands.getoutput("sudo mount /dev/nfsvg/nfslv  /mnt/nfs")
	#commands.getoutput("sudo echo '\n /mnt/my *(rw,no_root_squash) \n' >>/etc/exports")
	#commands.getoutput("sudo exportfs -r")
	#commands.getoutput("setenforce 0")
#else :

	#print "partition not found"

