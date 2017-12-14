#import argv modules
from sys import argv

#unpack argv
script, filename = argv

#open a file using 'filename' and return a file object to 'txt'
txt = open(filename)

#print the 'filename'
print "Here's your file %r:" % filename
#call the read() function of file object
print txt.read()

#print a prompt
print "Type the filename again:"
#get user input as string and return to 'file_again'
file_again = raw_input("> ")

#open a file using "file_again" as name
txt_again = open(file_again)

#call the read() function of file object
print txt_again.read()

txt.close()
txt_again.close()
