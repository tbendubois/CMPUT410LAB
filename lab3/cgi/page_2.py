#!/usr/bin/env python
 
import cgi
from random import randint
form = cgi.FieldStorage()

val1 = form.getvalue("name", "Not named yet")
val2 = form.getvalue("family", "No family yet")
print "Content-type: text/html"
print 
print """
<style type='text/css'>
p {
  background-color: #FFFFFF;
  font-size: 15pt;
}
</style>
<body background="/background.gif">
<marquee behavior="scroll" direction="left" scrollamount="30" bgcolor="#0000FF">
<font color="#00FFFF" size="200%">"""
print "Contratulations! You are visitor #%i!</font></marquee><br/>" %randint(1000, 100000)
print "<p>Your carefully collected data:<br/>"
print "Your Name is: %s" %val1
print "<br/>"
print "Your Family is: %s" %val2
print "</p><br/><br/>"


print """<form method="post" action="page_1.py">
<p>Birthday:</p> <input type="text" name="birthday">
<br/>
<p>Favourite Hobby:</p> <input type="text" name="hobby">
<input type="submit" value="Submit">
</form>
</body>
"""