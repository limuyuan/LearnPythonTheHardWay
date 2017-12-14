a = raw_input('a = > ')
b = raw_input('b = > ')
c = raw_input('c = > ')

if b > a:
    a, b = b, a
if c > a:
    a, c = c, a
if c > b:
    b, c = c, b

print a,b,c
