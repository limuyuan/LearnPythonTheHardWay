x = "There are %d types of people." % 10 # variable x
binary = "binary"   #variable binary
do_not = "don't"    #variable do_not
y = "Those who know %s and those who %s." % (binary, do_not)    #variable y, String inside string #1

print x
print y

print "I said: %r" % x  #print string using %r String inside string #2
print "I also said: '%s'." % y   #print string using %s String inside string #3

hilarious = True   #variable hilarious
joke_evaluation = "Isn't that joke so funny?! %r"   #varioble joke_evaluation with %r

print joke_evaluation % hilarious   #String inside string #4

w = "This is the left side of..."
e = "a string with a right side."

print w + e     # string cat
