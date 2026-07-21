print("Hello world")
print(2+2)
# Here, Nothing get excuted when press enter
# How can I ran this code ?
# Two way :
# 1. You can put the caret on a line and press the shift + enter
# It's gonna sent the line to REPL and run it.
print("Hello world")
# 2. the second way is run the file,
# send the entire content of the file to python, and all the lines will be executed in sequence.
# press the run button at the top right of the central panel
# you will want to do this once you finished writing your scripts

# Reminder 1: we can create variables in python and assign a content to them.
my_name = "Jade Zhang"
print(my_name) # this is the print of the content of the variable.
# Lets sent line 16 (print) to the REPL.
# I get a NameError: Normal, I have not define this variable in the REPL yet.

# The four big types of data in python
this_is_an_integer = 10
this_is_a_float = 3.14
this_is_a_string = "Hello world"
this_is_a_boolean = True/False #note that in python with Cap Letter, in R is all cap

# print using the print() function
print(this_is_an_integer)
print(this_is_a_float)
print(this_is_a_string, this_is_a_boolean) # we can print multipple string at once, separated by a comma
print(my_non_exisiting_variable)

# print() is something called a funtion. a function is something that takes between 0
#and many argument, and taht has a specific behaviour, it is an "action"


# you can print 
#a value 
print(3.14)
print("hello world")
# a variable
print(my_name)
# An expression. something that has not been calculated yet
print(2 + 2)
# remember expression are calculated "inside out"
# Rstill: when reading code, try to always understnad what is going to happen
# and in which order, 'Tracing the code' : understanding the steps the machine is taking
# #to arrive at a result.
print(this_is_an_integer)
print(this_is_an_integer + 5)# can you track this ?
# 1. Read the value contained inside the variable "this_is_an_integer"
# 2. Do the operation, Here, a sum, between this_is_an_integer (10) and 5
# 3. print the result of that operation.

# How do you figure out the type of a variable ?
what_is_this = type(this_is_an_integer)
print(what_is_this)
# We can also set that by simply typing the name of the variable we created.
what_is_this
what_is_this = type(3.14)
print(what_is_this)

# Calculations !
print(2 + 3)
print(2 + 3*5)
print((2 + 3)*5) # PANDAS

print(1 + 2)
print((1 + 2) == 3)# double equal: a logical comparison, checking if the elements on the right
# and on the left have the same value.
# logical comparitions always return a Boolean. True or False
print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3 )
# Floating point error.
# Do not expect float operation to be exact
# What can you do ?
my_rounded_edition = round((0.1 + 0.2), 1) # this is a function that takes two arguments
# the element to be rounded
# the digits of precision required
print(my_rounded_edition) # the way to deal with floating point error is to round.
round(3.14) # Function can have non-complitory arguments, default argument. For round, might is equal to 0
# if not specified.

# Logical comparisions:
print(3 == 5) # Equallity comparision 
print(3 != 5) # Not equal, different
print(3 > 5) # Greter
print(3 < 5) # less
print(3 <= 5) # less or equal
print(3 >= 5) # more or equal

# You can combine logical comparisions using AND or OR
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) #true
print(condition_1 and condition_3) #false
# and only returns True when ALL the conditons are True
print(condition_1 and condition_2 and condition_3) # False
print(condition_1 or condition_2) #True
print(condition_1 or condition_3) #True
print(condition_3 or condition_4) #False
# Or returns True as soon as at least one condition is True

# Let's do a few more calculations !
print(True + True) # so here True is 1, False are zero
print(True == 1)
print(False == 0)
print(True * 5) # This is 5, because for Python, True is 1
# amd False is 0
print(10 / 0) # Cannot divide by zero
print(10 / False) # False is zero

# Let's do some strings manipulation
# 'Calculating the string'

greeting = "Hello " + "world"
print(greeting)
# why does it work ?
#when used with strings, + is interpreted as a 
# 'contatention operator', technical word for 'putting things up'
# next to each other.
laugh = "ha" * 3
print(laugh)
# For string, the multiplication sign is interpreted as a "repeat"
# operation.

weird_laught = "ha" * 3.12 
# becareflul when mixing up differeng types. sometime tolerated
# but often rejected.... and always confusing to read 
very_complicated_laugh = "ha" + ('Hello' == 'world')*3
print(very_complicated_laugh) # Don't do thisl
# keep things simple (stupid)(KISS principal: Keep It simple stupid)

# How dowe keep things simple ? we make sure to convert variables
#before working with them

number = 42
is_this_a_number = "42"
print(number + 10) # 52
print((is_this_a_number) + 10)# How do we solve this ?
# Create a new variabke with the appropriate type;
now_this_is_a_number = int(is_this_a_number)
# int() turns something that is not a number into a number
print(now_this_is_a_number)
int("15") == 15
# what would I get If typed this?
int("fifteen")# you will get an error
int("jade")# also error
int(False)# this one works! 

# one more example.
my_age = 22
my_intro = "Hello, my name is Jade and I am" + my_age 
#How can I fix this then ?
my_intro_corrected = "Hello, my name is Jade and I am" + str(my_age)
print(my_intro_corrected)
# str(), float(), int() and bool() are functions
# that can turn an input into the desired type..
# ...assuming this is possible. 
str(3.14)
float('1e10')
