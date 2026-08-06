# difference between one dimension arrays and multi dimension arrays
import numpy as np
# Reminder: This is one-dimensioned array:
one_d = np.array([1, 2, 3, 4, 5])
# Reminder: We can use the property shape to see the shape of an array.
print(one_d.shape) # Why there is a comma in the print

# The innovation for this morning: We are going to introduce 2-d arrays.
# 2-d Array is like a martrix with rows and colums

# How do we create a two-d array?
# Like this: 
two_d = np.array([ # Here， I also have a single argument，
    [1, 2, 3],
    [4, 5, 6]
])# I Have a list, that itself contains two lists.
# Each of these inside lists correspond to a row of value in the matrix.

print(two_d) # it shows a matrix with rows and colums.
# How many rows: The number of inside lists;
# How many columns: The number of elements in these inside lives.

print(two_d.shape)
# The first number is always the number of rows 
# The second number is always the number of columns
# ORDER : ROWS AND COLUMNS

# What do you think happens if you index a 2-D array ?
print(two_d[0])# You are going to get the first row:[1, 2, 3]. This is an array.
# (one-dimensional array.)
print(two_d[1]) # second row: [4, 5, 6]

# So far, its eexactly live what we saw with lists and ond-d array:
# When you index with a numbers you get the corresponding element.
print(two_d[0:2]) # We get the first and second row. Our original 2-d array.
# You can also slice a 2-d array, and it works in the same way.

# So what's new then ?
# Since 2-D arrays have two dimension, we can use TWO sets of indices separated by a comma:
# The first one for the rows, the second one for the colums:
print(two_d[0, 0]) # We get the first element at the first row and first column.
print(two_d)
print(two_d[1, 1]) # Element at the second row and second column is 5.

# Let's practice a few nireL 
print(two_d[0, 0:2])
print(two_d[1, 1:2])
print(two_d[1:2, 1:3]) # 2D array here again
print(two_d[-1, -1])# Pay attention to what you are getting
# If you use a slice, you keep that dimension
# If you use a index, you get a single element.

# I'm going to introduce a new notation:
print(two_d[:, 0])# Just an empty colon, called an empty slice,
# you get all the elements. # All the rows, just colum 0.
# This is a one-d array

two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) # This is a square matrix.

print(two_d)

# like on 1-0 array, we can use slices and indexing to replace values.
# Exercise: replace the value 5 by 999 using indexing.
two_d[1, 1] = 999
print(two_d) # Now, make the final column be [7, 14, 21]

two_d[:, 2] = [7, 14, 21]
print(two_d) # always, rows, and columns

# Again, same logic as on 1:0 arrays.
# Let's restore our 2-D array
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) 

# 2-D arrays are arrays, Meaning we can do the same thing we saw Tuesday on 1-D arrays.

# Can you create an arrays that flags all the value in two_d
# that are greater than 5 (strictly greater).
mask = (two_d > 5)
print(mask)

# Can we use this mask to replace all the values strictly greater than 5 with 999

two_d[mask] = 999
print(two_d)

# refresher on Boolean indexing
a = np.array([1, 2, 3, 4, 5])# am array
b = np.array([False, True, True, False, True]) # A mask of the same shape
a[b] # We can apply the mask to the array and only get the values where the mask is True
# Another thing we saw is that we can use Boolean indexing to replace values:
a[b] = 999
print(a)

# Let's restore our 2-D array one last time 
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) 

mask = (two_d > 5)
print(mask)

print(two_d[mask])

# Let me re-show you a few things that we can do with arrays


a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [1, 1],
    [2, 4]
])

# We already saw that when arrays have compatible shapes, we can sum them:
print(a + b)
# subtract them
print(a - b)
# multiply them
print(a * b)
# divide them
print(a / b)
# you can add a single number to them: 
print(a + 10)

# Final thing I want to teach you:
# On tuesday, we saw that array have methods:
one_d = np.array([1, 2, 3, 4, 5])
print(one_d.sum())
print(one_d.max())

# Two-d arrays also have methods .... with a very small twist.
units_sold = np.array([
    [120, 190, 130, 170],
    [75, 60, 90, 80],
    [300, 330, 310, 330]
    ])# One thing I haven't mentioned: when creating an array, 
# all the rows need to have the same number of elements.

print(units_sold) # rows are products, Columns are months (Jan - Apr)
# what happen if we do :
print(units_sold.sum())# This is the Grand sum, all the sum of all the product
# sold in all the months.

# But what if we wanted instead to have the total per product ?
# Or the total per month ?
# This is where a nifty keyword comes in: axis= 
# This is an argument on most array methods.
print(units_sold.sum(axis=0))
# The axis tells us the dimension that we are collapsing.
# That we are taking the method over.
# Herem we sum the dimension (0) (the rows) and are thus left with the columns.
print(units_sold.sum(axis=1))# here, we do the opposite:
# We take the sum across the columns and are left with the rows.

# Exercise: The method mean() gives you the mean of an array,
# It also takes an optional axis argument.
# Use this method to give me the mean units sold in each of the four months.
print(units_sold.mean(axis=0))
# using the method max() Find the highest number of unit sold across all the products and months.
print(units_sold.max())
# Final exercise: FInd the minimum number of sale for product 4. across the four months.
print(units_sold[0, :].min())