ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

#return a list of the sections in ten_things, using ' ' as the delimiter
#call split with ten_things and ' '
stuff = ten_things.split(' ') # split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:

    #remove and return last item in more_stuff
    #call pop with more_stuff
    next_one = more_stuff.pop() # pop(more_stuff)
    print "Adding: ", next_one
    
    #append next_one to the end of stuff
    #call append with stuff and next_one
    stuff.append(next_one) # append(stuff, next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #whoa! fancy

#remove and return last item in stuff
#call pop with stuff
print stuff.pop() #pop(stuff)

# join stuff with ' ' between them.
# Call join with ' ' and stuff. 
print ' '.join(stuff) #what? cool! join(' ', stuff)
print '#'.join(stuff[3:5]) #super stellar! join('#', stuff[3:5])