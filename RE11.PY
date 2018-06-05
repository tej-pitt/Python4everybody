"""
Search for lines start with ' X ' followed by any 
non whitespace characters and ':' followed by a space
and any number. The number can include a decimal.
Then print the number if it is greater than zero. 
"""



import re 
fname = input("Enter file name: ")
try:
   fhand = open(fname)
except:
   print("Invalid file name")
for line in fhand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)' , line)
    if len(x) > 0 :
        print(x)