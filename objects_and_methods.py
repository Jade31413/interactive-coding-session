this_is_an_integer = 10
this_is_a_string = "Jade"
type(this_is_an_integer)
type(this_is_a_string)

# after creating a variable in python, you can check a ll the things 
#that are contatined in that variable using the .doc in VSCode
#After you press the doc, it will reveal a list of hings
#contained in the object.
#These things come in two flavours:
# PROPERTIIES: Signal by the wrench icon, contains information, data
# METHODS: Described by a purple box. Describes all the actions that 
#can be performers by the objects
print(this_is_an_integer .numerator) #10
print(this_is_an_integer .denominator) #1
# Properties are describing the state of the object that we created.
another_integer = 5
print(another_integer .numerator)
# Can we check some properties of the string now ?
print(this_is_a_string) # no propertiees in there !

# what is really useful are methods,
# methods allow us to do stuff with the objectthat we created 
#They are live a function, in what they can dothings
# but they are specfiically attached )we say 'bound' to the object
# let's check out some methods of this is a string.
this_is_a_string .upper() #A method requires parathesis, because they
# are attions, they're like a function, so you need to 'call' them.
# All string will have this method. all objects of a given type
#share the same methods.
this_is_a_string .lower() # everything is lower case.
# we can store the result of that somewhere
my_upper_name = this_is_a_string.upper()

#what else is in there?
this_is_a_string.endswith("!") # shows not end with a "!"
this_is_a_string.endswith("ade")# Returns true !
# Methods are a way of pairin functions to specific types of objects.

this_is_an_integer.real 

#Let me show you a few more methods for sring.
# string contain al ot of methods
# because there are a lot of things that we can do with them
# we're already seen Upper(), Lower(), Title() (Capitalling the first)
#letter of each world
my_sentence = "Hello my name is Jade"
my_sentence.title()
# we've also seen endswith(), let me show you a few more.
lots_of_white_space = "        Jade"
lots_of_white_space.strip()
# Let me show you a practical example of how these methods can be useful
entry = "     Jade.Zhang@colorado.edu      "
# This could be somethin someone entered into a form.
# I want to check if this person has a .edu email adress
is_it_edu = entry.endswith("edu")
is_it_edu# it is false beacuse of the whitespace
stripped_entry = entry.strip()
is_it_edu_for_real = stripped_entry.endswith("edu")
is_it_edu_for_real
#is it a boolean
type(is_it_edu_for_real)
# Final thin on this: We could write is_it_edu_for_real more clearly.
# Here, we have created a new variable with strip(), and then used the 
# endswith() method on this new varible. BUt we can skip this step:
is_it_edu_for_real = entry.strip().endswith("edu")
# entry.strip() returns a string. meaning we can directly call
# the method endswith() on this nearly created string

# This is called CHAINNING. You call methods on an object that is returned
# by another method.

# Common errors with methods and properties
entry.shout() # AttributeError: 'str' object has no attribute 'shout'
# You try to call a method that does not exist on the object. 
price = 12
type(price)
price.numerator() # TypeErrorL int object is not callable
type(price.numerator) # numerator is a property of the interer 1, stored into price.
# is contain an integer, which is 12.
# but an integer does not do anythin. it is not a function or a methods.
# You cannot call it. THat's what the " not callable" is telling you.
# The error attempting to call a property. You can only call a method inside an object
price.numerator

# let's do a few more exploration.
price.is_integer # This is a method: purple box, and it is an action that we are doing.
# what will happen if I run this line ?
# WE need the parenthesis to call the method! Otherwise it is not doing anything.
price.is_integer()

#So far, we've seen four big types of objects:
#str, float, int, boolean
# In python, you are often going to create other objects
# let me show you one object that is going to solve a problem we had before
from decimal import Decimal # Not seen yet, soon! don;t worry
# what is Decimal ? It is a factory for manufacuring a new kind of object: Decimal object.
# Tocreate a str, you only needed to put quotes arround something
# To create a float or int, you just needed to type a float or an int.
# To create a boolean, you just neede to type True or False, or have a local comparition

# To create Decimal object, we are going to use the Decimal:thins we just imported 
a = Decimal(".1")
# We have created a new decimal object, with the value .1
type(a)
b = Decimal(".2")
type(b)
print(.1 + .2) # what are we gotting? A floating point error.
# This is because by default, python represents floats with a limited number of zeros
print(a + b) # if you print the sum of the Decimal object, you et an exact representation
# That's the problem that Decimal is solving.
a. # if you reach into a Decimal orbject with the dot, you are going to see a lot of new methods and properties! 

