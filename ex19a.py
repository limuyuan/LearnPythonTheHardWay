def TenWays_to_Run(*wtf):
    arg1, arg2 = wtf
    print "Actually, this is a simple add func."
    print "%s + %s = %s" % (arg1, arg2, arg1 + arg2)
    print "Cool!\n"


# 1
TenWays_to_Run(1, 2)

# 2
TenWays_to_Run(1 + 2, 2 + 3)

# 3
a = 2
b = 3
TenWays_to_Run(a, b)

# 4
TenWays_to_Run(a, b + 2)

# 5
TenWays_to_Run(a + b, b - a)

# 6
TenWays_to_Run(a, 5)

# 7
TenWays_to_Run(a + 5, 5)

# 8
TenWays_to_Run(b + 7, a - b - 2)

# 9
TenWays_to_Run(a * 9, b * a)

# 10
TenWays_to_Run(a * a * b, b * b * b)

# 11
a1 = int(raw_input("a1 "))
a2 = int(raw_input("a2 "))
TenWays_to_Run(a1, a2)
