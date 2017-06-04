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
<title>LINUX SERVERS</title>
<link rel="stylesheet" href="http://192.168.0.20/css/table.css">
<style>
#banner2{
	margin-top:0px;
	background-image:url(../images/log.jpg);
	box-shadow:inset 0 0 10px #000000;
	text-align:center;
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

<form action="http://192.168.0.20/cgi-bin/server.py" method="POST">


"""
print "<div id='banner2'>"


print "<div class='dpara'>"
print "<img src='http://192.168.0.20/images/server1.png' style='margin-top:20px;' height=150px ></br></br>"

print "<div class='para1'>""</div></br>"
for f in lines: 
	print "<span class='table'>"+f+" ::: <input type=checkbox value='"+f+"' name='apache'></input></span>"

print "<br>&nbsp;</br>"
print  "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/server2.png' style='margin-top:20px;' height=150px></br></br>"

print "<div class='para1'>""</div></br>"
for f in lines: 
	print "<span class='table'>"+f+" ::: <input type=checkbox value='"+f+"' name='mariadb'></input></span>"
print "<br>&nbsp;</br>"
print  "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/server3.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='nfs'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"

print "</br></br></br></br></br>"


print "<div class='dpara'>"
print "<img src='http://192.168.0.20/images/server4.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='samba'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/smtp.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='smtp'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/ftp.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='ftp'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"

print "<input type='SUBMIT' value='SUBMIT' class='button'></input>"

"</form>"

"""
</div>
</body>
</html>"""
