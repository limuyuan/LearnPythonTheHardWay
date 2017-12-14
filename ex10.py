tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print """
I'm "hungry"
and I want to test ''' and ""\"
That's all.
"""

print '''
I
will try
"""triple-single-quote""" instead
this time.
'''

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
