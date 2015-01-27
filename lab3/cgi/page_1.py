#!/usr/bin/env python
 
import cgi
from random import randint
form = cgi.FieldStorage()

val1 = form.getvalue("birthday", "No birthday yet")
val2 = form.getvalue("hobby", "No hobby yet")
print "Content-type: text/html"
print 
print "<p>Your carefully collected data:<br/>"
print "Your Birthday is: %s" %val1
print "<br/>"
print "Your Favourite Hobby is: %s" %val2
print "<br/><br/>"

print """<form method="post" action="page_2.py">
<p>Your name:</p>
<input type="text" name="name">
<br/>
<p>Family name:</p>
<input type="text" name="family">
<input type="submit" value="Submit">
</form>
<marquee behavior="scroll" direction="right" scrollamount="30"
        width = "50%" bgcolor="#000000"
        onmouseover="this.stop();" 
        onmouseout="this.start();">
            <blink><font color="#00FF00">Arbitrary Feature #2!</font></blink>
</marquee>
"""