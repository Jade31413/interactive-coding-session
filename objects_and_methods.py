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
my_upper_name