# http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib2

def newNothing(text):
   wordlist = text.split(" ");
   return wordlist[len(wordlist)-1]
 
sitename = ""
templatesite = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"
dividebytwo = False
for i in range(1,253):
    f = urllib2.urlopen(templatesite + nothing).read()
    if f == "Yes. Divide by two and keep going.":
        nothing = str(int(nothing) / 2)
    else:
        nothing = newNothing(f)        
    print f


