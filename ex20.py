from sys import argv

script, input_file = argv

def print_all(f):
    # print the content of f
    print f.read()

def rewind(f):
    # offset to the start of file
    f.seek(0)

def print_a_line(line_count ,f):
    # print line count and the content of that line -> \n
    print line_count, f.readline()

# open a file given in argv
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print current_file.tell()

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print current_file.tell()

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
print current_file.tell()

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
print current_file.tell()

current_line = current_line + 1
print_a_line(current_line, current_file)
print current_file.tell()
