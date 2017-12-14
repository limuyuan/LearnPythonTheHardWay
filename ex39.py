# create a mapping of state to abbreviation
states = {
    'Liaoning': 'LN',
    'Zhejiang': 'ZJ',
    'Guangxi': 'GX',
    'Jilin': 'JL',
    'Sichuan': 'SC'
}

# create a basic set of states and some cities in them
cities = {
    'LN': 'Dalian',
    'ZJ': 'Hangzhou',
    'SC': 'Chengdu'
}

# add some more cities
cities['GX'] = 'Guilin'
cities['JL'] = 'Changchun'

# print out some cities
print '-' * 10
print "Liaoning State has: ", cities['LN']
print "Guangxi State has: ", cities['GX']

# print some states
print '-' * 10
print "Zhejiang's abbreviation is: ", states['Zhejiang']
print "Sichuan's abbreviation is: ", states['Sichuan']

# do it by using the state then cities dict
print '-' * 10
print "Jilin has: ", cities[states['Jilin']]
print "Liaoning has: ", cities[states['Liaoning']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
    
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
    
# now do both the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Beijing', None)

if not state:
    print "Sorry, no Beijing."

# get a city with a default value
city = cities.get('BJ', 'Does Not Exist')
print "The city for the state 'BJ' is: %s" % city