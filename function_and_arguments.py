# we've been using function from Day 1 (or almost)
# print(), type(), round(), str(), float(), int(), bool(), len()
len("Jade") # give the number of elements in a string or a sequence

# what is a function? 
# A function is live a machine: it does something.
# It usually takes one or more inputs and usually return a result

# print() <- what does it take ?
# Any expression that we want to print.
# what does it do ? It print stuff to the user.
# str() <- what does it take ?
# It takes any expression
# WHAT DOES IT DO? it returns it into a string, and returns it to the user.

# what does it mean to RETURN something ?
# let's take print() as exampleL
print("1234") # it is going to print "1234" inthe terminal
my_content = print("1234")
my_content # my_content is emptu, print('1234') did not store anything in it.
# why ?

# some function (most) return something. Think of them as a conveyor belt:
# They are going to take an object on one side, do things to it, and them RETURN
# the result of what it did on the other side of the machine.

# Other Functions are just doing stuff: THink of them as an engine.
# you are going to put some gas into them, they are going to do something;
# but they are not going to hand you back anything.

# Let's write functions together to better understand this distinction.
# We are going to write a function that takes a price, a ratem and returns the price updated with the rate

# How do we create a new function ? WE use this syntax: 
def print_total(price, rate): # def, followed by function name, parenthesis (argument)
    total = price * (1 + rate)
    print(total)
    # you will see that your cursor move to the rightL
    # This defines the body of the function. every code inside.
    # is going to define what the function will do.

# We've create our functionm let's druve ut!
print_total(10,1) # let's run this , and practice tracing the code
# let's say : I want to store this data for later use:
my_total = print_total(10, 1)
my_total #nothing include my total. Why ? lets create the fnuction back again.
#engine, not conveyor belt.

# let's write anoter function then that solves this issue.
def calculate_total(price, rate): #some structure as before.
    total = price * (1 + rate)
    return total # on the other side of the conveyor belt, spit out the total

my_total = calculate_total(10, .1) # what happen when i run that ?
print(my_total) # success: this function calculated somethin.
# RETURNED it back to me, and now I can store it into a variable.
# what happen if you don't store it ?
calculate_total(10, .1) # just falls into the terminal and gets printed
# Always better to have functions that RETURN stuff. Gives more flexbillity to the user.

# Some vocabulary: The inputs of a function are called the ARGUMENT.
# They come into top flavors.
# 1. "positional arguments", defined by the order in which you enter them.
round(3.14, 1) # Rounds the first number to the number of digit in the second number
round(1, 3.14)

calculate_total(10, .1)
calculate_total(.1, 10) # position argument are expected in a certain order,
# and give into a certain order.

# some function take a variable number of argument:
round(3.14)# Here, the second argument is not compulsory, it has a default, which is a.
print("ABC") # print 'ABC'
print("ABC", "DEF", "HIJ") # print

# print isan example of a function that takes an arbitrary number of arguments.
# you can give as many as you want, and it's going to print them all.
# second flavor of argument: 'named' argument, or 'keyword' argument.
# These are argument that are added by specifying their name.
print("a", "b", "c", "d", sep = "*") # Here, sep is named argument, and I give it the value "*"
# name argument are not compulsorym and have a default value.
# Default armument for sep is a space
print("A", "B", "C", "D", sep = "-", end = "!")

def add_excitement(string):
    excited_string = string + " !!!!!!!!!!"
    return excited_string
    print(" The function ran successfully") # added this after return
    # nothing is gonna excuted after 'return', anything added after return is not going work.

python_is_fun = add_excitement("python is fun")
python_is_fun