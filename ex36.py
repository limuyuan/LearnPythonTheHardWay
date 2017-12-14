prompt = '--> '

def Luban7():
    print "Your opponent is BAILISHOUYUE!"
    print "\nWhat should you do? Run or Kill him?\n"

    next = raw_input("Run / Kill?" + prompt)


    if "Run" in next:
        dead("One, Two, Three shots, BAILISHOUYUE kills you!")
    elif "Kill" in next:
        print "Perfect! You'have killed BAILISHOUYUE!"
        story()
    else:
        dead("Libai shuashuashua kills you!")


def Diaochan():
    print "Your opponent is DAJI!"
    DZReady = True
    while True:
        print "\nWhat should you do? Run or Kill her?\n"
        next = raw_input("Run / Kill?" + prompt)
        if "Run" in next and DZReady == True:
            print "DAJI chase you and Heart, Boom, Moon, you're not dead!"
            DZReady = False
        elif "Kill" in next and DZReady == True:
            dead("Heart, Boom, Moon, DAJI kills you!")
        elif "Kill" in next and DZReady == False:
            print "You killed DAJI! Awesome!"
            story()
        else:
            dead("What are you doing? Your crystal was boomed!")

        
def Lvbu():
    print "Your opponent is DIANWEI!"
    print "He turn on his DAZHAO and going to kill you!"
    DZReady = True
    while True:
        print "\nWhat should you do? Run or Kill him?\n"
        next = raw_input("Run / Kill?" + prompt)
        if "Run" in next and DZReady == True:
            print "DIANWEI can't chase you!"
            DZReady = False
        elif "Kill" in next and DZReady == True:
            dead("DIANWEI: Ahahaha, you're no match for me!")
        elif "Kill" in next and DZReady == False:
            print "You killed DIANWEI! Awesome!"
            story()
        else:
            dead("What are you doing? Your crystal was boomed!")

def SelectRole():
    print "Welcome to WangzhePythonyao v1.0"
    print "Please select your role to play:"
    print """
    We now have:
    1. Luban7
    2. Diaochan
    3. Lvbu
    """
    role = raw_input("Enter number " + prompt)

    if role == "1":
        selectLocation("Luban7")
    elif role == "2":
        selectLocation("Diaochan")
    elif role == "3":
        selectLocation("Lvbu")
    else:
        dead("We only have these 3 heroes!")

def dead(str):
    print "You dead! " + str
    exit(0)

def selectLocation(role):
    print """
    You have five places to go:
    TOP, MID, ADC, JUG, SUP
    Where do you want to go?
    """
    place = raw_input("Enter role " + prompt)
    if place == "TOP":
        start(TOP(role)[0], TOP(role)[1])
    elif place == "MID":
        start(MID(role)[0], MID(role)[1])
    elif place == "ADC":
        start(ADC(role)[0], ADC(role)[1])
    elif place == "JUG":
        start(JUG(role)[0], JUG(role)[1])
    elif place == "SUP":
        start(SUP(role)[0], SUP(role)[1])
    else:
        dead("Why don't you fly into the sky?")

def TOP(role):
    if role == "Luban7" or role == "Diaochan":
        dead("Five people hidden for gank you!")
    elif role == "Lvbu":
        return [role, "TOP"]
    else:
        print "This should never run!"

def MID(role):
    if role == "Luban7" or role == "Lvbu":
        dead("Diaochan bb at you and exit the game!")
    elif role == "Diaochan":
        return [role, "MIDDLE"]
    else:
        print "This should never run!"

def JUG(role):
    if role == "Luban7" or role == "Diaochan":
        dead("Hanxin kicked your ass off!")
    elif role == "Lvbu":
        return [role, "JUGLE"]
    else:
        print "This should never run!"

def SUP(role):
    if role == "Luban7":
        dead("You lose a key team fight and enemies boom your crystal!")
    elif role == "Lvbu" or role == "Diaochan":
        return [role, "SUPPORT"]
    else:
        print "This should never run!"

def ADC(role):
    if role == "Lvbu" or role == "Diaochan":
        dead("The enemy ADC's shooting your body happily!")
    elif role == "Luban7":
        return [role, "ADC"]
    else:
        print "This should never run!"


def start(role,location):
    print "\nGood! You have made the right choice!"
    print "You are %s, and your location is %s!\n" % (role, location)

    print "Game start!"
    print "The enemies will show up now!"

    if role == "Luban7":
        Luban7()
    elif role == "Diaochan":
        Diaochan()
    elif role == "Lvbu":
        Lvbu()
    else:
        "This should never run!"

def story():
    print "\nA new story begins here!"
    print "To be continue.."
    
SelectRole()
