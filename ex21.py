def add(a, b):
    print "ADDING %f + %f" % (a,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %f - %f" % (a,b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %f * %f" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %f / %f" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

what = add(1, subtract(2, add(3, subtract(4, multiply(5, divide(6, 7))))))

print "That becomes: ", what, "Can you do it by hand?"

what = subtract(add(24.0, divide(34.0, 100.0)), float(raw_input("1023.0: ")))

print "That becomes: ", what, "Can you do it by hand?"
