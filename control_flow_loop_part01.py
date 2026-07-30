# loops are code blocks that are going to run multiple times.
# We are going to learn, or relearn about two different kinds of loops:
# while loops. and for loops/

# Let's start with the while loop:
count = 0 # don't worry about this for now
while count < 5: # while keyword, followed by a CONDITION: A statemnt that evaluates to True or False
    print(count)
    count = count + 1

# A while loop is going to execute AS LONG AS THE condition is True.
# As soon as the condition becomes False, It will no longer run.
# That means a while loop will run zero, one, two, ..... infinitely many times.

# The typical structure of a while loop:
# 0. Initiallization; The condition must be equal to something.
# 1. inside the loop, something will happen to the condition.
# if the condition is never changed, the loop will run forever.

# A very common use case for a while loop is to WAIT until some condition becames True.

user_input = "" # Initiallization
while user_input == "":
    user_input = input("Please enter something")
print("You entered " + user_input)

# let's use a while loop to process a to do list:
to_do = ["laundry", "dished", "yard cleaning", "dog walikng"] # Initiallization
while len(to_do) != 0:
    item = to_do.pop() # Remaining the last item of a list, and returns it.
    print("Now I am doing this: " + item)

# the still that we are going to practice, and that is important for reading code.
# is called TRACING a loop:
# Understanding, at each iteration, what happens.
# Iteration 0: after iteration 0, what is item equal to ? "dog walking".
# What is to_do equal to ? ["laudry", "dishes", "yard cleaning"]
# what is len(to_do) equal to ? 3 
# so is the while loop going to run again ?
# Iteration 1: After this loop, what is item equal to ?

# One small detour: 
# let me tell you about f-string
my_age = 39
my_name = "Quentin"
my_school = "CU Boulder"
greeting = "Hello, I'm " + my_name + " I,m " + str(my_age) + " and I teach at " + my_school
print(greeting)

# this works, nothing wroing with that but,
# it is ugly and long to write
# and I need to remmeber to convert any non-str variable into string before I am add it.

better_greeting = f"Hello, I,m {my_name}, I'm {my_age},and I teach at {my_school} "
# adding an f in front of the first quote
print(better_greeting)
# f-string

# Next, for loops.
# remember a while loop is somethingthat checks if a condition is True,
# and runs for as long as the condition is True.

# what is a For Loop ?
# If is something that Iterates on an object, and runs as many times as the number of elements
# in the obeject.

for number in [1, 2, 3, 4, 5]: # it starts with the keyword for
    # then it names a variable, called the 'STEP' variable
    # then the in keyword
    # then an ITERABLEL: Something that contains a number of elements.
    # while the for loop is running, 
    # the STEP variable is going to take the value of all the elements
    # in the iterable, one by one.
    print(f"The number is {number}")

# A for loop is meant to run a KNOW number of items: the length of the iterable.

# Another example:
for letter in "Quentin":
    print(letter)

# Here, the loop was just printing the element. we can do mroe complicated things:

list_of_numbers = [1, 2, 3, 4, 5, 6]
for number in list_of_numbers:
    square = number**2
    print(f"The square root of {number} is {square}")

# lets practice TRACING that loop:
# Iteartion #, number square
# first iteration, 1, 1
# second 2, 4
# third 3, 9

# let's end up the difficulty slightly,
# here, we were printing the squares
# We were not saving them anywhere.
# let's build another for loop that stores the squares in a new list
list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_squares = [] # this is what will contain our square number once we calculate them.
for number in list_of_squares:
    square = number ** 2 
    list_of_squares.append(square) # reminder that .append() adds to the existing list,
    # modifying it in place.

# Iteration #, number, square, list_pf_numbers
# first, 1, 1, [1]
# second, 2, 4, [1, 4]
# third, 3, 9, [1, 4, 9]

# After the loop concludes:
# Final, 6, 36, [1, 4, 9, 16, 25, 36 
print(list_of_squares)

# lets say, you are confused. you really do not understand how a long is working.
# by reommandation? add a print statement tracking exactly whats going on

list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_squares = [] # this is what will contain our square number once we calculate them.
for number in list_of_squares:
    square = number ** 2 
    list_of_squares.append(square) # reminder that .append() adds to the existing list,
    #modifying it in place
    print(f"current Iteration: number is {number}, square is {square}, list_of_number is {list_of_numbers}")

# Very common use case for a for long: Accumulate something, 
list_of_numbers = [4, 8, 15, 23, 42 ,9]
# I want to know what all these number sum to:
# This is what you get when you add them all, one by one.
total = 0 # very important: otherwise we cannnot start adding
for number in list_of_numbers:
    total = total + number
    print(f"The sum of {list_of_numbers} is {total}")

print(total == sum(list_of_numbers))

# now let's do a for loop that get up the maximum value in a list of numbers
list_of_numbers = [4, -3, 9, -7, 14, 52]
max_value = -99999999999999999
for x in list_of_numbers:
    if x > max_value:
        max_value = x
    # If x is SMALLER than our current max, we don't care, we move on

# Iteration #, x, max_value:
# First, 4, 4
# second -3, 4
# third 9, 9
# fourth -7. 9
# fifth 14, 14
#.... and so on
print(max_value == max(list_of_numbers))