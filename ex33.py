i = 0
numbers = []
'''
# Original version
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
'''


# While func
def whilelist(num, step):
    """
    Make a list of size num with step then print the numbers out.
    With the test variable printed at the top and bottom.
    """
    judge = True
    i = 0
    while judge:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        judge = i < num

# For func
def forlist(num, step):
    for i in range(0, num, step):
        print "At the top i is %d" % i
        numbers.append(i)
        # i = i + step need to be removed
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


whilelist(30,-3)
print "\nNow use forlist:\n"
numbers = []
forlist(30,3)

print "The numbers: "

for num in numbers:
    print num
