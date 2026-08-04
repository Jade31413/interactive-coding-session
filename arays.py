# Imports are always at the top of your file;
import numpy as np # import x as y x is the libarary name, y is the shorthand
# when libraries have short names, like math, we don;t use a shorhand.
import math 
import pandas as pd
# The first thing we are going to do is somethign we've done once or twice;
# import a library

# If a library is not installed, what do we do ? UV !
# in a regular terminal  -type: uv add pandas numpy 

# once you ve installed and imported a library you can access its content using the dot notation
print(math.pi)
print(math.sqrt(9))

# lets talk about arrays now. arrays are a new kind of object that live inside the numpy packages
my_arrays = np.array([1, 2, 3, 4, 5])# you can create an array by supplying a list of elements
print(my_arrays)
# it looks a lot like a list.
# you can index it:
print(my_arrays[1])
# you can slice it:
print(my_arrays[0:3])
# so waht's live the difference really ?
type(my_arrays)
# first difference: an array requires that alll its elements are of the same type.
my_list = ["Quentin", False, 42]
print(type(my_list[0]))# str
print(type(my_list[1]))# boolean

# what if I create an array from this ?
my_array = np.array(my_list)
print(my_list)# All the elements have been converted to string.
# In technical term, we say they were coverced to a common type.
# It finds a common type for All the elements to be converted to.

# because all elements of an array have the same type.
# arrays itself have what is called a dtype, short for data type.
print(my_arrays.dtype)
#other examples:
float_arrays = np.array([3.14, 2.16, 1.5])
print(float_arrays.dtype)
int_array = np.array([1, 2, 3])
print(int_array.dtype)

# second distination between listsL
# array have a FIXED SIZE.
# you cannot add or remove elements from an array after it was created.
my_list = [1, 2, 3, 4, 5]
my_list.pop()
print(my_list) # The pop method has removed the last element of the list
my_list.append(0)
print(my_list)# the append method has added an element to the list

# What about arrays now ?
my_array = np.array([1, 2, 3, 4, 5]) # I create it here
my_array.pop()
my_array.append()
my_array.insert() 
# All. the methods that allow you to insert, remove or append element to list
# do not exist on arrays.

# Instead you need to use functions to create new arrays
my_bigger_array = np.append(my_array, 6) # this will create a new array that has the same content
# as my_array, plus the elements 6 appended to the end.
print(my_array)# unchanged, still contain 1 2 3 4 5
print(my_bigger_array)# A new array was created

# Summary, arrays are more constrained. they have to have the same data type.
# They have a fixed lenth.

# These restrictions enable very powerful things.

# let me show you:
# first, lets not use arrays.
prices = [9.99, 19.99, 4.99, 14.99, 24.99]
quantities = [120, 75, 100, 50, 40]
# Say I want to calculate, for each product, the total revenue: price * quantities
# For each of these five products.
# How would I do that ?
totals = []
for (p, q) in zip(prices, quantities):
    t = p * q
    totals.append(t)
print(totals) # You can't really see it, but this operation is slow.

# What arrays allow you is to do VECTORIZED operations, Rather then taking the elements one by one
# and chcecking, one by one, if the operation is allowed and how it works, array are going to perform
# all the calculations at once on all the elements

arr_prices = np.array(prices)
arr_quantities = np.array(quantities)
arr_totals = arr_prices * arr_quantities
print(arr_totals) # I can just multiply the arrays directly,

# other examples:
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80, 25])# units sold for five different productm in Jan and Feb

totals = units_feb * units_feb
print(totals)
# How much more or less we sold in Feb compared to Jan ?
print(units_feb - units_jan)
# Growth rate over the two month ?
print(units_feb / units_jan)

# A restriction though !
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80])# only data for four products

print(units_feb - units_jan) # the two arrays do not have the same SHAPE
# The number of elements in an array is called the SHAPE
print(units_jan.shape)
print(units_feb.shape)# to sum, divide, or multiply two arrays, they need to have comparible shapes.
# By the way, this is why we cannot add or remove elements from arrays, we meed to know their shape at all times

# What else can you do with arrays ?

# we can compare them ! 
units_jan = np.array([120, 75, 300, 50, 40])
units_feb = np.array([150, 60, 330, 80, 25])# units sold for five different productm in Jan and Feb

feb_sold_more = units_feb > units_jan
print(feb_sold_more)

# You can square an array:
print(units_jan ** 2) # again applies the operation in a vectorized way to each of the elements

# you can also use the square root (if we are careful to use the numpy version)
print(np.sqrt(units_jan)) # The numpy library contains special version of common each operations
# that are specifically designed to work with arrays

# Error, We reached 10 fake transactions for each of the product in Jan
print(units_jan - 10)

# there are many operation you can apply to arrays.... and arrays also have methods that you can inspect ! 
units_jan.mean() # you can call the method mean(), to know the mean vaclue of an array... if the array has a numerit dtype.
units_jan.std()