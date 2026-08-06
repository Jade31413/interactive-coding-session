import pandas as pd # go to reguler terminal, uv add pandas before typing this
# So what is a dataFrame? We are going to start a familar object
# to understand what it is and what it does.

data = {
    "Month": ["January", "February", "March", "April"],
    "Marketing_spend": [2000, 3000, 2500, 4000],
    "sales_spend": [5000, 7000, 6000, 8000],
    "Leads_Generated": [150, 200, 180, 250]
} # A dictionary where the keys are the column names
# and the values are lists, or arrays, containing the column values.
# Most importantL all these lists/arrays must have the same size.
# They determine how many rows you have in your data.

# Now that we ahve this data, we can create a dataFrame as such:
df = pd.DataFrame(data)
print(type(df))

#In practice, you are rarely going to type your data into a dictionary.
# and create a dataFrame from it. you are going to read data from files.
df = pd.read_csv("sales_data.csv") # we give the relaive path of the file we want to read.

# Now that we read it, let's see what we got inside the docs
print(df) # print the dataFrame
# this datast is very small, 12 rows only.
# If you print a dataFrame of hundred of thousands of rows, you terminal might crash.
# instead, it is recommanded to inspect a dataset using:
print(df.head()) # first five rows
# for good measure, you can also check the end of your dataL
print(df.tail()) # last five rows of the data.

# If you want a rich summary of your dataFrame, you can use the method info()
print(df.info())

# You can access a bunch of thes things individually
print(df.columns)# Note: no parentheseis, this is a property, not a method.
print(df.shape)# Exactly like the matrices we just saw, first is rows, second is columns,
print(df.dtypes)# Name of columns and corresponding dtypes.
print(df.index)# The index in dataFrame is 'The names of the rows'
# by default, when you read or create a dataset, the rows are going to be assigned
# name using a range(): First row will be 0 and second will be 1, so on.

# A dataFrame is: 
# An index, containing the name of the rows,
# A list of column names, containing the name of the columns
# A collection of arrays, mapped to individual column names.
# Like a mix of a dictionary and arrays.

# HOW DO YOU INDEX A DATAFRAME.
# How do you access individual rows and columns of the dataFrame
# for reading and writing data

# Lets first start easy: How do you read the content of a column in a dataFrame?
# Remember that dataFrames are a lot live dictionaries.

print(df["Month"]) # I index by the name of column, and get the content of the column back..
# .. A column in a dataframe is called a Series. For all intents and purposes, it's going to work like
# an array. with the row indices in front of each value.

print(df["Marketing_Spend"])

# you can ask for the content of multiple columns at once:
print(df[["Month", "Marketing_Spend"]]) # Note the double brackets: One to index, one to say:
# a list with multiple elements.
# when you ask for multiple columns, you get a dataframe.

# Much like on arrays, we can then replace the content of a column:

df["Marketing_Spend"] = df["Marketing_Spend"] * 1.1 # We get the content of the column
# Marketing spend, multiply it by 1.1, and store it back into the dataFrame.
print(df["Marketing_Spend"])

# We can also create new columns! 
# To add a new key to a dictionary, we simply did: my_dict['new_key] = 'value'
# We use the same logic to create a new column in a dataframe:
df["Cost_Per_Lead"] = df["Marketing_Spend"] / df["Leads_Generated"]
print(df.head())

# We saw how to index columns. Isefi;!
# Next, now do we index rows ?

# A typical reason why you would want to index rows is to identify
# rows that have a specific. THat is called filtering data.

# Let's say you want to flag the month (the rows) where the cost_per_lead was cheap:
# say < 35

# we can create a mask on a dataFrame using the same logic as on ID arrays:
mask = df["Cost_Per_Lead"] < 15
print(mask)

# Now we have the mask, and how do we use it ?
# Exactly like on an array: you index the dataFrame with the mask
print(df[mask]) # Returns a dataframe resricted to the rows for which the mask is True.

# wait, this is very confusing...
# We can index with the column names, and it works...
# and we can also index with a Boolean mask on the rows, and it works as well ?

# df("cost_per_lead") <- Gives me all the rows for this column only
# df[mask] <- gives me only the rows where the mask is True, and all the columns

# It is not super clean, and potentially confusing, to use the same way of indexing.
# both to get rows and columns

# On martices, we were doing two_d[row_index, cal_index]. that was cleaner.

# let's see how we can have the same [row_index, column_index] behavior on a dataframe.

# to do that, you type: df_loc[row_index, col_index]
# For instance, if I want a particular column and all the rows, I type:
print(df.loc[:, ["Month", "Marketing_Spend"]])
# If i want just the rows that I masked, and all the columns, I type:
print(df.loc[mask, :])
# ANd if I want just one column for the rows I masked, I type:
print(df.loc[mask, ["Month", "Marketing_Spend", "Leads_Generated"]])

# Final topic: Analyzing data.
# both dataFrames and Series (means: a single column in a dataFrame)contains methods for calculating stuff.

df.loc[:, "Cost_Per_Lead"].mean()# The series "Cost_Per_Lead" with all the rows.
# .mean() will return the mean cost per lead across all the rows.

df.loc[:, "Leads_Generated"].max() #300 is the maximum number of leads generated in the data.

# Methods on series work in exactly the same way as methods on array. They return the mean(),
# max(), min() value taken across all the values.

# What if you use these methods on DataFrame instead, meaning when you have multiple columns:
df.loc[:, ["Marketing_Spend", "Sales_Spend"]].max() # I am getting a dataFrame with all the rows and the 
# columns. WHat happens if i call max() on it ? When you call a method like max() or min(), on a dataframe
# that has multiple columns the default behavior is: calculating across the rows, for each of the column
# Here, we are getting the max value for marketing speed, and the max value for sales spend.

# What If I do this now ?
df.loc[:, ["Marketing_Spend", "Sales_Spend"]].sum() # Same behavior: We are taking the sum
# across all the rows, for each of the two column. We are getting one sum, across the 12 months
# for marketing_spend, and one sum across the 12 months for sales_spend

# But what if Instead, I wanted the total spend for each month ?
# Meaning, for each month, the sum if marketing_spend and the sum of sales_soend for that month.
df.loc[:, ["Marketing_Spend", "Sales_Spend"]].sum(axis=1) # We are collapsing all the columns 
# and keepting the rows. We are taking the sum of marketing + sales spend. for each of the rows.

# Now that we have calculated this total spend, we might want to save it in our dataFrame.
df["Total_Spend"] = df.loc[:, ["Marketing_Spend", "Sales_Spend"]].sum(axis=1) 

print(df.head())

# To summarize again: by default, methods on dataFrame are applied across rows, for each of the 
# Columns. If we want to instead apply, across columns for each of the rows,
# We use axis=1 as argument.

# Congrats! We have loaded data, marnipulated the rows and columns,
# And created two new columns.
# Now, Let's save our new dataFrame into a file.
df.to_csv("clean_sales_data.csv", index=False)
