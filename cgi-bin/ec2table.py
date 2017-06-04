#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

cgitb.enable()

print "Content-type:text/html"
print ""


lines = [line.rstrip('\n') for line in open('awsipread.txt')]


print """<html>
<head>
<meta charset="utf-8">
<link rel="shortcut icon" href="http://192.168.0.20/images/favicon.png"/>
<title>LINUX SERVERS</title>
<link rel="stylesheet" href="http://192.168.0.20/css/ec2table.css">
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
<script>
	function launch(){
		window.open("https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Instances:sort=instanceId",'_blank');
		return true;
	}
</script>
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

<div id="banner1">
<section id="container">

<iframe style="margin-top:14px;" height="436px" width="55%" src="http://192.168.0.20:4200/" id="container"></iframe>


	<form action="http://192.168.0.20/cgi-bin/ec2.py" method="POST" style="width:30%; float:right;  padding-right:2%;"> 
	<fieldset>
		<legend style="font-size:30px; font-family:Arial; color:white;"> Launch Instances</legend>
		<table>
        	    	<tr>
			<td><select style="width:363px;height:50px;margin-bottom:20px;font-size:20px;color:darkred;background-color:white" name="osl"><option>Select OS</option><option style="font-size:20px;" name="amzlinux" value="amzlinux">Amazon Linux AMI 2016.09.1</option><option style="font-size:20px;" name="rhel" value="rhel">Red Hat Enterprise Linux 7.3</option><option style="font-size:20px;" name="ubun" value="ubun">Ubuntu Server 16.04 LTS</option></select></td>
			</tr>
                        <tr>
			<td><select style="width:363px;height:50px;margin-bottom:20px;font-size:20px;color:darkred;background-color:white;" name="sgs"><option>Select Security </option><option style="font-size:20px;" name="s1" value="sg-8cf20df7">Security Group1</option><option style="font-size:20px;" name="s2" value="sg-fdf40b86">Security Group2</option></select></td>
			</tr>
			<tr>
			<td><select style="width:363px;height:50px;margin-bottom:20px;font-size:20px;color:darkred;background-color:white;" name="icou"><option>No of Instances</option><option style="font-size:20px;" name="c1" value="1">1</option><option style="font-size:20px;" name="c2" value="2">2</option><option style="font-size:20px;" name="c3" value="3">3</option><option style="font-size:20px;" name="c4" value="4">4</option></select></td>
			</tr>
			<tr>
			<td><select style="width:363px;height:50px;margin-bottom:20px;font-size:20px;color:darkred;background-color:white;" name="iflav"><option>Select Flavour</option><option style="font-size:20px;" name="t2.micro" value="t2.micro">1--vcpu & 1GB--RAM & EBS </option><option style="font-size:20px;" name="t2.small" value="t2.small">1--vcpu & 2GB--RAM & EBS</option></select></td>
			</tr>
			<tr>
			<td><select style="width:363px;height:50px;margin-bottom:20px;font-size:20px;color:darkred;background-color:white;" name="ikey"><option>Select Key</option><option style="font-size:20px;" name="k1" value="key1">key1</option><option style="font-size:20px;" name="k2" value="key2">key2</option><option style="font-size:20px;" name="k3" value="key3">key3</option></select></td></br>
			</tr>
		</table>
		<section id="buttons">
			<input type="submit" name="submit" id="submitbtn" class="button" tabindex="7" value="LAUNCH" onclick="return launch();">
			<br style="clear:both;">
</fieldset>
</form>
</section>
</div>



<form action="http://192.168.0.20/cgi-bin/awsserver.py" method="POST">
"""
print "<div id='banner2'>"
print "<h1> Deploy Servers, Apps and Configure them on Amazon Elastic Compute Cloud(EC2) !</h1>" 

print "<div class='dpara'>"
print "<img src='http://192.168.0.20/images/server1.png' style='margin-top:20px;' height=150px ></br></br>"

print "<div class='para1'>""</div></br>"
for f in lines: 
	print "<span class='table'>"+f+" ::: <input type=checkbox value='"+f+"' name='awsapache'></input></span>"

print "<br>&nbsp;</br>"
print  "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/server2.png' style='margin-top:20px;' height=150px></br></br>"

print "<div class='para1'>""</div></br>"
for f in lines: 
	print "<span class='table'>"+f+" ::: <input type=checkbox value='"+f+"' name='awsmariadb'></input></span>"
print "<br>&nbsp;</br>"
print  "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/server3.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='awsnfs'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"

print "</br></br></br></br></br>"


print "<div class='dpara'>"
print "<img src='http://192.168.0.20/images/server4.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='awssamba'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/smtp.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='awssmtp'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"


print "<div class='para'>"
print "<img src='http://192.168.0.20/images/ftp.png' style='margin-top:20px;' height=150px></br></br>"
print "<div class='para1'>""</div></br>"
for g in lines: 
	print "<span class='table'>"+g+" ::: <input type=checkbox value='"+g+"' name='awsftp'></input></span>"
print "<br>&nbsp;</br>"
print "</div>"

print "<input type='SUBMIT' value='SUBMIT' class='button'></input>"

"</form>"

"""
</div>
</body>
</html>"""
