# Talk about collections, Collections are objects
# Designed to hold other projects inside them.
# They're like bags of different kinds

# First, Lists

# A list is an ordered ollections of items
# It is created using square brackets 

my_empty_list = [] # This is a list that does not contain anything.
type(my_empty_list) # A List ! A new kind of object.
# What do lists do ? They are contain other objects.

my_favortie_number = [1, 2, 3, 4, 5]# This is a list of integers
print(my_favortie_number)

# Lists can contain other elements
my_favorite_color = ["red", "yellow", "green", "black"]# this is alist of strings
my_favorite_decimals = ["3.14", "23.21"]# this is a list of floats
my_favorite_booleans = ["True", "False", "False"] # lists can contain repeated elements

#List can contain different elements of eifferent kinds .
my_favortie_things = ["red, 3.14, 3, False"]

# You can put ANYTHING you want into a list, even other lists! 
my_mixed_list = [False, ["blue", 19], ["red", False], 3.14]
# so don't be surpiresed: lists are very flexible. you can just put a lot of things in them.

# lists are objects meaning.....
# They contain properties and methods!

# Let's see some methods of lists!
my_favorite_color.append("white") #["red", "yellow", "green", "black"]
# This did not print anything, weired...
print(my_favorite_color) # You will find out that white will be added into the list.

# this method 'append' is SUPER different from all the other methods that we saw before, 
# no strings for instance, why ?

# because it CHANGED the object directly. It "mutated" the original object.
# let's refresh our memories.
my_string = "Jade"
# what happens if i do:
my_string.upper() # I run this, It prints a string in upper case.
print(my_string) # the original string is still in lower case.
# In technical terms, the method COPIES the original object, changes it, and returns
# the copy. the original NEVER change.

# THis is because strings are 'immutable', Once created, their content will not change.
# The only way to make changes to a string is to createa a new one with a different content,

# back to lists: Let's see how methods affect them.
my_favorite_color # Now contain ['red', 'yellow', 'green', 'black', 'yellow', 'white']
print(my_favorite_color)

# I am going to run the append method to add another color: pink
a = my_favorite_color.append('pink')# what will my_favorite_color contains after I run this line?

print(my_favorite_color)

# the method mutated the original list. the content was changged directly by the method.
# But then what is inside of a ? what did the method return ?
print(a) # when you are working with a method that mutates the original.
# it will typically not return the original. It will simply do something on the original.
# and return none

# let's say we don't like that, we don;t like the fact that every time we are adding thing to my
# favorite colors, it changes the original
my_original_colors = ['pink', 'purple']
# I want to add a colror to this list, but NOT modify the original.
my_updated_colors = my_original_colors # I want this to be my backup.
# Cool, Now I can add something to my my_updated_colors, and my_original_colors will still exist somewhere.
my_updated_colors.append("orange") # I add orange to my_updated_colors
print(my_updated_colors) # Sweet, we added a color
# Now, what of my original colors?
print(my_original_colors)
my_original_colors.copy()
# If you prints the list with oragne in it!
# This is because lists are mutable, so when you give a list different name. 
# it will points to the same list, rather than creating a copy of the list
# If you don't want that, you need to use the copy() method to create a copy of the list

# Back to less confusing things
# other methods with lists:
my_favorite_color # ['red', 'yellow', 'green', 'black', 'yellow', 'white', 'pink', 'pink', 'pink']
# what if you want to remove an element of the list ?
# you can use a method called "pop".
# Pop is going to remove the last element of the list.
# and returns it to you
removed_color = my_favorite_color.pop()
# what will be the content of my_favortie_color? 
print(my_favorite_color) # ['red', 'yellow', 'green', 'black', 'yellow', 'white', 'pink']
print(removed_color) # "pink"

# What if I re-run this line?
removed_color = my_favorite_color.pop() # it will remove "white" from the list
# returns it to us, and it will get assigned to removed_color

# Something new with lists: If you run the same command multiple times, the behavior will change.
# The list is being mutated, so you not going to get the same results.

# what happens if you don;t assign the popped color ?
my_favorite_color.pop() # list now contains 'red', 'yellow', 'green', 'black'

# This is behavior that we've seen before, If a function or method returns something
# and we don;t 'catch' it into a variable, it 'falls' into the terminal.

# lists are ORDERED. Meaning you can reach into them at a specific position
# and grab the content.

my_favorite_names = ["Quentin", "Zoe", "Mathilda"]
# Let's say I want to read what is a t the beginning of the list ?
# If you want to get an element, you can use an operation called INDEXING
# Indexing is : you put square brackets after the list, and use the INDEX of the element
# than you grab:
print(my_favorite_names[1])# R starts counting from 1, Pythom from 0.
# 0 returns the first element, 1 the second, 2 the third.... etc.
print(my_favorite_names[2])# Mathilda
print(my_favorite_names[0])# Quentin

# What happens if you index [3]
print(my_favorite_names[3]) # Returns an error.

# let's continue our discussion of indexing.
# we can also use NEGATIVE indices:
print(my_favorite_names[-1]) # -1 read the last value.
print(my_favorite_names[-2]) # The second to last calue

# we can also do something called SLICING to grab multiple values from a list:
my_favortie_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Indexing again first:
my_favortie_numbers[2] # Getting the 0, 1, 2; THiird value of the list.
# slicing now :
# the syntax for slicing is [start:stop:stop]. Let's see what that meansL
my_favortie_numbers[0:3:1] # this means: the values between the first and the fourth (excluded), and all of them.
#none examples:
my_favortie_numbers[1:6:1]# all values between the second and seventh(excluded)
# and all of them
my_favortie_numbers[3:8:1] # all values between the fourth and eight (or ninth excluded)
my_favortie_numbers[0:6:2] # Every other value between the first and the xith

# When you are slicing, you can amit some argumentsL
my_favortie_numbers[0:3] # By default, step is one (If amitted)
#this is equvalent to [0:3:1]
# waht about this ?
my_favortie_numbers[1:] # all of them starting from one. both and is amitted )so it defaults to 'until the end')
# and step is amitted (so it defaults to 1)
my_favortie_numbers[:4] # Start us anutted (so it defaults to 0, beginning).
# Stop is 4 (meaning until 4th element, excluded), step is amitted to 1:
my_favortie_numbers[::2]# start is amitted (to zero), stop is amitted (so until)
# the end, and step is 2: every otehr value in the entire list
#Practice slicing: type slices, and try to predict what you will get.
my_favortie_numbers[::-1]# tricky, try to guess!
# cool trick for reversing a list!

# Want to see something cool ?
my_name = "Haoqian Zhang"
my_name_but_mirroed = my_name[::-1]
my_name_but_mirroed # A string is an ordered collection of charcaters
# so you can slice it like a list.
my_name[0:4]

# Sofarm为learned that
# 1) lists are MUTABLE, meaning we can modify their content using mehtods.
# 2) lists are ITERABLE, meaning we can select a subset of their content using slices.

# Let's put these two things together!
my_favorite_names # ['Quentin', 'Zoe', 'Mathilda']
# It's weired to have my professor name as a favorite. let's replaceit with something else.
# How could I replace 'Quentin' to 'Jade' in these list?
my_favorite_names[0] = 'Jade' # we are indexing the first element of the list,
# and assigned the value 'Jade' at that positio
my_favorite_names # We have mutated the list!

# We can do the same thing with slices!
my_favorite_names[1:] # this is slicing ['Zoe', 'Mathilda']
my_favorite_names[1:] = ['Eve', 'Joshua']
my_favorite_names # So we can use slicing and indexing to read or update the content of a list.

# Bonus question: can we indexing or slicing to update the content of a string?
my_name[0] = "Z" # nope does not work. Strings are not mutable!
# If you want a new string, you need ti create a new string.

# Back to a few list methods: 
my_favorite_names.pop() # removes the last element of a list
my_favorite_names.append('Joshua') # add this element the end of the list
# Pop and append can take an additional arggument: The position!
my_favorite_names.pop(0) # this will pop the first element, Jade
my_favorite_names.insert(0, 'Jade')
my_favorite_names
# All these methods are modifying the original list. not returning a copy of the list.
# Let's try one more:
my_favorite_names.reverse() # what will this return?
# It 'returns' nothing: it changeing the order of the original list.
my_favorite_names


# Lists are collections of ordered items.
# Dictionaries are collections of key value paris

# let's start with an example:
my_friends_age = {"Nick": 40, "Sam": 35, "Juan": 37}
# Note the syntax: Curly brackets, contaning key:value pairsm seoarated by comma.

# Dictionaries can have different kinds of values:
my_information = {"name": "Quentin", "age": 39, "hobbies": ["coding", "skiing", "birding"]}
# Here, you have the key "name" that contains a stirng calue,
# the key "age" that contains a int value
# the key "hobbies" contains a list value

# What about the keys in a dictionary? What can they do ?
# They are typically int or str. the most important rules:
# They have to be UNIQUE (only one key must have a given name)
# and they have to be IMMUTABLE.

# How do we use dictionaries ?
# we can also reach inside them to see the values. That's again called
# 'INDEXING'. For a list, It is ordered, so we index with numbers.
# What do we index with when you have a dictionary?

my_friends_age["Nick"] # How do I get Nick's age? 
# I use square brackets to index, and I give the key for which I want to see the value

# what will I get if I type this ?
my_information["hobbies"]

# Dictionaries. like lists, are mutable. We can update them!
# Let's say my friend Nick just celebrated his birthday.
# How do I updated his age?
my_friends_age["Nick"] = 41 # you reach into the dict at the desired key
# and you assign a new value to it.
my_friends_age

# Let's try another example.
# Can I change my name to 'Quentin andre' ?
my_information['Quentin'] = 'Quentin Andre' # that is wrong

my_information['name'] = 'Quentin Andre' # that is right
my_information

#Throught your mistake, we learned something:
# we can add new keys to a dictionary!
# I want to add my job to my information
my_information['job tittle'] = 'marketing prof'
my_information
# we can use indexing to:
# 1) Read the value of an existing key.
# 2) Update the value of an existing key.
# 3) Create a key with a given vlaue.

# since dictionarie are OBJECTS... They have METHODS
my_information['address']
# If you accidentally check for a value taht does not exist, you will get a KeyError
# Errors aren't great when you're writing code, beacause they will stop your code.
# A better way to check if a key exists is to use the method get()
quentin_address = my_information.get("address") 
print(quentin_address) # This will print None. .get() returns None when the key is not found.

#Three other useful methods: Rather than blindly checking if a key exists, sometimes you wan to see 
# All the keys that exist in a dictionaryL
my_information.keys() # Check all the keys
# you can do the same things to see all the value with ... .values()
my_information.values()
# You can now know all the keys, all the alues... but you don't know to which each correspond.
# Solution ?
my_information.items()

# Reminder: The keys of dictionaries must be int or str.
# the values can be anything. so far we've seen
# str
#int
#list

# what is very common is to have dictionaries as values, to stroe more complex information.
# let me give you an example/
my_friends_info = {
    "Nick":{ # one key: Nick, one value: His dictionary.
        "age": 41, # Inside that dictionary, other keys (his information) and values (what they are)
        "city": "Boulder",
        "hobbies": ["skiing", "cooking"]
    },

    "Sam":{
        "age":35,
        "city": "Chicago",
        "hobbies": ["hiking", "coffee"],
        "job": "professor"
    }# Another key: Sam one vlaueL its dictionary of information
}

# How would we use a dictionary like this ?
# How would you get your friend Nick's age? 
my_friends_info["Nick"]
# So we just got Nick's dictionary
# Now, How would we get Nick's age from that dictionary?
my_friends_info["Nick"]["age"] # we index Nick's dictionary to get his age by using the 'age' index.
# How would we get Sam's 
my_friends_info["Sam"]["hobbies"]
# What if you're not sure if you have information about a friend's job ?
my_friends_info["Sam"].get("job") # If we do it for Sam, We got: professor
my_friends_info["Nick"].get("job") # If we do it for Nick, We get: nothing

# Mini Assignment. Sam recently picked up birdwatching, can you add this hobby to his list of hobbies?
# Hint: use .append() to add an element to a liest.
# can we reach for Sam's hobbies first?
my_friends_info["Sam"]["hobbies"] # we can verify that we are getting Sam's hobbies:
# This is a list. What do we know about lists ?
# They are mutable: We can modify them in places. We can changes their content. add to it .
# or remove from it.
# If we grab this list, we can add to it using append:
my_friends_info["Sam"]["hobbies"].append("birdwatching")
# It does not print anything, nothing gets returned.
# If we check Sam's habbies again:
my_friends_info["Sam"]["hobbies"]

# lists are ORDERED collections of elements of any kind.
# we access elements by their position
# we manipulate lists using INDEXING and SLICING to access and modify the elements that they contain.
# we can also use methods like .pop(), .append() or insert() to do that.

# Directionaries are ORDERED collections of key:value part
# we access the values by their key
# we manipulate directionaries using INDEXING to access and modify the values associated with given keys.
my_friends_info[0] # There is no key called 0, so it will return a KeyError.