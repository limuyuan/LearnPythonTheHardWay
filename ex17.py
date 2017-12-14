from sys import argv
from os.path import exists

script, from_file, to_file = argv
#we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read()

#indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()
print "Whether the output file exists: %r" % exists(to_file)

print "Copying from %s to %s" % (from_file, to_file)

#out_file = open(to_file, 'w')
#out_file.write(indata)

open(to_file, 'w').write(open(from_file).read())

#print "Alright, all done."
print "Done"

#out_file.close()
#in_file.close()
