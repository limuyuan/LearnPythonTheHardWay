## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def barrk(self):
        print "Animal BARK!"

    pass

class Test(object):
    """docstring for Test."""
    def __init__(self, arg):
        super(Test, self).__init__()
        self.arg = arg


## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
    def bark(self):
        print "Wang!!Wang!!"


## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

Dog.bark(rover)
rover.bark()

#flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()

rover.bark()

test = Animal()

rover.barrk()
