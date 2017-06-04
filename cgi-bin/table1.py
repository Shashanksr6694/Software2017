#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

cgitb.enable()

print "Content-type:text/html"
print ""


lines = [line.rstrip('\n') for line in open('ipread.txt')]


print """<html>
<head>
<meta charset="utf-8">
<link rel="shortcut icon" href="http://192.168.0.20/images/favicon.png"/>
<title>STORAGE</title>
<link rel="stylesheet" href="http://192.168.0.20/css/table1.css">
<style>
#banner2{
	padding-top:60px;
	margin-top:0px;	
	background-image:url(../images/log.jpg);
	text-align:center;
	height:640px;
	background-size:cover;
	background-position:center;
	width:100%;
}
</style>
</head>

<body>

<div id="menu"> 
	<ul class="list">
	<a class="mya" href="http://192.168.0.20/home.html"><li>HOME</li></a>
       	<a class="mya" href="http://192.168.0.20/about.html"><li>ABOUT</li></a>
        <a class="mya" href="http://192.168.0.20/services.html"><li>SERVICES</li></a>
	<a class="mya" href="http://192.168.0.20/monitoring.html"><li>MONITORING</li></a>
    	<a class="mya" href="http://192.168.0.20/contact.html"><li>CONTACT</li></a>
    	</ul>
</div>

<div id="banner3">
<a href="http://192.168.0.20/about.html"><img src="http://192.168.0.20/images/logo1.png" height=60px class="logo"></a>
</div>

<form action="http://192.168.0.20/cgi-bin/glusterfs.py" method="POST">


"""
print "<div id='banner2'>"

print "<div class='linux1'><h2>STORAGE AUTOMATION</h2>"
print "<p style='text-align:justify;'>GlusterFS is a scalable network filesystem creates large, distributed storage solutions for media streaming, data analysis. Storage Automation Service automates High Availability Distributed Replicated Storage Solution using GlusterFS. </p></div>"

print "<div class='para'>"
print "<img src='http://192.168.0.20/images/gluster.png' height=200px ></br></br>"


print "<div class='para1'>""</div></br>"
for f in lines: 
	print "<span class='table'>"+f+" ::: <input type=checkbox value='"+f+"' name='gluster'></input></span>"
print "<br><br><br>"
print "<input type='SUBMIT' class='button' value='SUBMIT'>"
print "<br>&nbsp;&nbsp;&nbsp;</br>"
print  "</div>"



"</form>"

"""
</div>
</body>
</html>"""
