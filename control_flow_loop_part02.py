# You can consider that "advanced topics" in loops.

# One thing I said is that, in a for loop, the thing that we are looping over:
# for x in the_thing_we_are_looping_over is called an ITERABLE.
# An iterable means: something we can unpack into distinctive elements.

# We've seen some of them:
# Lists are iterable:
fruits = ["banana", "apple", "mango"]
for f in fruits:
    print(f)


# We've also seen that strings are iterable:
my_word = "Supercalifragilistic"
for letter in my_word:
    print(letter)
# When you loop over a string, you are getting the letters, one by one.

# Dictionaries are iterable:
my_info = {"name": "Quentin", "age": 39, "city": "Boulder"}
for info in my_info:
    print(info) # I am getting the keys of the dictionary, one by one.

# How would I print both the key and the value?
for key in my_info:
    value = my_info[key]
    print(f"The key is {key} and the value is {value}")

# If I want the value associated with the key "name":
print(my_info["name"])

# There is an even better way that I'm showing you so that you can recognize it:
my_info.items() # This is giving me each of the (key, value) pairs in succession.
# The best news is? We can ITERATE on that!

for (key, value) in my_info.items():
    print(f"The key is {key} and the value is {value}")

# Much simpler example of unpacking
fruits = ["banana", "apple", "mango"] # This list contains three elements
my_first_fruit, my_second_fruit, my_third_fruit = fruits
print(my_first_fruit)

fruits = ["banana", "mango", "apple"]
# I want to write a loop that prints me:
# Fruit 1: banana
# Fruit 2: mango
# Fruit 3: apple

# THe first function is called enumerate():
for (index, item) in enumerate(fruits):
    # When, instead of iterating on the ITERABLE directly
    # we used enumerate(ITERABLE), we are getting both the index, and the element
    # at each loop.
    print(f"The element at position {index} is {item}")

# Final one for today:
# Let's say we have multiple lists that are somehow connected to each other:
list_of_foods = ["pickle", "pepper", "cherry"]
list_of_tastes = ["sour", "spicy", "sweet"]
# Here, we might want to print: "a pickle is sour", "a pepper is spicy"...
# There is a way of connecting, zipping, multiple iterables together:

for (food, taste) in zip(list_of_foods, list_of_tastes):
    # At each iteration, we are getting one element of each list,
    # unpacked into their respective step variable.
    print(f"A {food} is {taste}")

# What if we have three lists?
list_of_colors = ["green", "red", "red"]
# It's not more complicated!

for (food, taste, color) in zip(list_of_foods, list_of_tastes, list_of_colors):
    # At each iteration, we are getting one element of each list,
    # unpacked into their respective step variable.
    print(f"A {food} is {color} and tastes {taste}")

# ---------------------- Week 05 --------------------- #

# Lets talk about range()

for i in [1, 2, 3, 4, 5]: # i is the step variable, [1, 2, 3, 4, 5]is the iterable
    print(i) # i is going to take, in turn, the vlaue of each of the lements in the iterable.

# Now, imagine, we wont to get all the numbers from the 0 to 1000:
# if we are writing the loop old way:
for i in [0, 1, 2, 3, 4, 5, 1000]: # A bit of pain to wirte to 1000.
    print(i)

# so ... enter range() 
# range is a function that create an iterable for you that you can loop on.
# range takes three arguments: start, stop, step.
# start is optional, and default to 0
# stop is optional, and default to 1
for i in range(1001): # all the number between 0 and 1001 are excluded.
    print(i)

#start, stop, step should remind you of slices:
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list[0:4]
my_list[::2]

for i in range(0, 1000, 2):
    print(i)

# all there is to know about range: A convenient way of getting an iterable of number to loop on.

# The final thing on loops I want to show you is something called 
# list comprehensions.

# Let's say I want the square of all the numbers between 0 and 9
# let's write a loop that iterates over numbers between 0 and 9,
# take the square of them, and store them in a list called my_squares.

my_squares = []
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    my_squares.append(i ** 2)
print(my_squares)

# This task, creating a new list from an existing iterable, is extremely common in python,
# That is what a shortcut called list comprehensions is doing
# Here, I could have done the same job by typing:
my_squares = [i ** 2 for i in range(10)]
#A list comprehension is surrounded by square bracket, THis is because we are creating a list.
# then you see an expression: i**2 this define how the step variable is going to be modified
# to create the elements of the list.
# Finally, you see the loop itself: for step_variable in iterable. note, there is no colon here,
print(my_squares)

my_list = [x.upper() for x in "quentin"]
print(my_list)

# one final thing on list comprehensions:
# we can add, after the (for step_variable in iterable) an optional IF statment,
# that filters the elements of the list.

my_filtered_squares = [i ** 2 for i in range (10) if i ** 2 < 30]
# only add to the list if the squares are less than 30:
my_filtered_squares

# very common use case for this filter:
paths = ["data.csv", "report.pdf", "summary.csv", "image.png", "notes.txt", "data2.csv"]
# lots of the filters of the different types.
# lets say I jsut want o keep the .csv files.
my_csv = [i for i in paths if i.endswith(".csv")]
print(my_csv)

# (考试的主要形式将会是给出几个公式选择，然后来选哪个match 题目的目的)
# How could i write a for loop that could do the same job:
my_csv = []
for path in paths:
    if path.endswith(".csv"):
        my_csv.append(path)
print(my_csv)
