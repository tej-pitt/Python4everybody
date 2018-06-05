"""
search for lines that start with 'Details: rev='
followed by numbers and '.'
Then print the number if is greater than zero
"""



import re 
fname = input("Enter file name: ")
try:
   fhand = open(fname)
except:
   print("Invalid file name")
for line in fhand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)' , line)
    if len(x) > 0 :
        print(x)
        