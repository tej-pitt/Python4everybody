"""
search for lines that start with From and a character
followed by a 2 digit integer between 00 and 99 followed by ":"
then print the number if it is greater than zero
"""

import re 
fname = input("Enter file name: ")
try:
   fhand = open(fname)
except:
   print("Invalid file name")
for line in fhand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):' , line)
    if len(x) > 0 :
        print(x)
        
        