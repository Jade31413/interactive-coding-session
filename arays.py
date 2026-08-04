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

# we've already seen that you can index and slice arrays like list:
prices = np.array([10, 5, 20, 30, 8])
print(prices[0]) # the first price
print(prices[0:3])# the first three prices
# When you index with a single value, you get a value of the dtype of the array
# when you slice an array, you get a new array.

# when working with arrays, live with lists, you can edit the elements of the array:
# lets replace the first price by 15:
prices[0] = 15
print(prices)
# what if we want to now make the first two prices equal to 15 and 7 ?
prices[0:2] = [15, 7]
print(prices) # arrays are still mutable! we just cannot change their shape.

#everything that we've seen so far with indexing and slicing
#is identical to what we could do with lists.

# we can do more powerful stuff with arrays 

# 1. "masking" or "boolean indexing".
# we can index an array with a boolean array of the same shape.
my_mask = np.array([True, False, True, False, True]) # this is a mask
prices = np.array([15, 7, 20, 30, 8])
# I have my array and my mask
print(prices[my_mask])# I can index the prices using the mask: put the mask between square bracket after the array
# When you index with a mask, you are going to get in return only the aclues of the array
# where the corresponding position in the mask in True.
# Think of overlaying the mask on top of the arrayL the True are the cutouts, any value that is in the cutout is going to be returned

# when are mask useful ?
quantities = np.array([5, 10, 15, -5, -7, 10])# Quantities cannot be neggative, to this array.
# contains some coding errors.
# could we create a mask that would reveal these errors ?
my_mask = quantities < 0 # WE get a mask: an array of shape 6, that contains True or False elements
print(my_mask) # Now we have the mask.
# How can we use it to spot all the erronous value in quantitive ?
print(quantities[my_mask]) # we used the mask to se all the negative value in quantities 
# and get them in an array
#Now, can we use the mask to replace all these negative value by 0 ?
quantities[my_mask] = 0 # You use the mask to HIGHLIGHT all the negative vlaue and you assign the value to 0 to them.
print(quantities)

quantities = np.array([5, 10, 15, 0, 0, 10]) # this is the number of customrs a coffee shop had from monday through saturday
# 1. On average, how many customers did they see on these six days ?( reminder: mean() is a method that gives you the mean of an array)
# 2. On all the days they saw at least one customer, how many customer did they see on average? 
#A1. 
quantities.mean()

#A2. 
quantities = np.array([5, 10, 15, 0, 0, 10])
# 第一步：创建一个 mask，标记出"至少有一位顾客"的那些天
mask = quantities > 0
print(mask)  # [ True  True  True False False  True]
# 第二步：用这个 mask 筛选出对应的数值
active_days = quantities[mask]
print(active_days)  # [5 10 15 10]
# 第三步：对筛选后的数组求平均
print(active_days.mean())  # 10.0
# or 
# 一句话表达清楚:
print(quantities[quantities >= 1].mean())  # what is between square brackets is the mask:
# We don't need to store it into a variable first.

# Final thing with arrays: fancy indexing... and that's pretty fancy.
# let's say you have email from four customers.
emails = np.array(["quantin@colorado.edu", "gal@yale.edu", "puntoni@wharton.edu", "gino@mbs.edu"])
# how do we get the first email of the list ?
print(emails[0])   # The first
print(emails[0:2]) # The first two
# with lists you can only (i) index with a single value OR (ii) use a slice.
# with arrays you can index with multiple values.
# that's what fancy indexing is:
print(emails[[0, 0, 1, 2, 0]])  # when you give a LIST OF values as an index
# note the double bracket: outer bracket does the indexing, inner bracket defines the list.
# If it makes it easier to process, you can break it down into two lines:
my_indices = [0, 0, 1, 2, 0]
print(emails[my_indices])

# why fancy indexing? very common: select a random sample of rows in a dataset.

# Let's wrap up on arrays
# 1. an array is a new type of iterable. It works a lot like a list
# 2. exception 1: an array only contains values of the same type. The data type of an array is called dtype
# 3. exception 2: arrays have a fixed shape. They can't be pop()'ed, append()'ed, or insert()'ed.
# 4. thanks to these restrictions, arrays can be added to each other, subtracted from each other,
# and its elements can be multiplied, squared, divided, exponentiated... whatever you want. These operations
# are performed on all elements of the array and are much faster.
# 5. arrays can be compared, element-wise, to create boolean arrays (also called masking)
# 6. you can use these masks to filter arrays and re-assign values at specific positions
# 7. Arrays, like lists, can be indexed and sliced, both to select and to replace values.
# 8. Compared to lists, arrays accept two new forms of indexing: boolean indexing (only the values facing
# the True values in the mask are returned), and fancy indexing (all the indices specified in the list are returned)