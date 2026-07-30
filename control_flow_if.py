# Control flow is a term describing all the tools in Python that governs.
# whetehr, when and how much/often a block of code is going to run.
# Up until now, every live that we were writting was running.

# First up: Conditional logic.
# This is what governs wheter a block of code is going to be executed.

my_name = "Quentin"
my_gender = "None"

if my_gender == "Male":# A conditional logic block always starts with IF.
    # followed by a condition： It's statement that element to True of False
    # The line ends with a colon : 
    # Then, the line below, you start an indented block:
    # This indented block describes the line of code(s) that will run 
    # ONLY if the condition evaluated the True
    # For the most simple conditional logic block, that's all you need.
    # A block with just on IF is binary: Either the block gets executed  (if CONDITION is True)
    # or it isn't (if CONDITION is False)
    print("Hello Mr " + my_name)
    # Sometimes the world is more complicated. THere's more than one possibility.
    # That is where you can add some bells and whistles to your conditional block
    # Using the Keyword "elif and else"

elif my_gender == "Female":
    # It describes a second possible condition
    # that is ONLY going to be checked if the previous conditions evaluated to False
    # It's sequential: we start is True.
    # if it is True, we end here,
    # if it is False. we check the second condition
    # If it is False again,we check the third condition.
    # we can have zero, one, or many specific condition.
    print("Hello Ms " + my_name)

elif my_gender == "Non-Binary":
    print("Hello " + my_name)   

else:   # When at the bottom, after all the elif statements (if any)
    # We can have the "else" block. the else block means:
    # If All the conditions turneds out to be False
    # Heres what you should do 
    print("Hello " + my_name + ", how should we address you ?")
    # If there is no else statement, nothing happens when all the other condition
    # Evaluate to False


# A very common GOTCHA with conditional logic block:
# Conditional: logic blocks are very common inside functions: 
# They allow you t ohace functions that have a different behavior as a function of their 
# inputs:

def status_checker(age):
    # We wamt this function to return the 
    if age >= 13:
        return "you are a teenage"
    elif age >= 18:
        return "you are an adult"
    elif age >= 4:
        return "you are a child"
    elif age >= 2:
        return "you are a todler"

    else:
        return "you are a baby"

# lets test our status check fnction
status_checker(1)
status_checker(3)
status_checker(9)
status_checker(14) # 'you are a teenage'
status_checker(39) # If returns 'you are a teenage' 
# why ? The forst statement that is check is (39 >= 14)
# if evaluate to True, the function then returns "you are a teenager"
# lets try to fix this behavior


def correct_status_checker(age):
    # We should simply flip the first two two conditions:
    # Statemnt are now ordered from Most to Least restructive
    # Meaning if a statement is True, all the other statemnet that follow are also True.
    if age >= 18:
        return "you are an adult"
    elif age >= 13:
        return "you are an teenager"
    elif age >= 4:
        return "you are a child"
    elif age >= 2:
        return "you are a todler"
    else:
        return "you are a baby"

# If a conditional logic statement is not behaving as expected,
# you should always check that the conditions are in order.

# what happens when you have multiple conditions that you want to check ?

def can_leagally_drink(country, age):
    # The answer depends on the contry and t he age:
    # to do that, we can nest conditional logic blocks:
    # first, we pick one conditionL
    if country == "USA":
        # Here, inside the block, we handle the other condition
        if age >= 21:
         return "You can leaglly drink in the USA"

        else:
            return "You can not legally drink in the USA"
    elif country == "Canada":
        if age >= 19:
            return "you can leagally drink in Canada"
        else:
            return "You can't leagally drink in Canada "
    elif country == "France":
        if age >= 16:
            return "You can leagally drink in the France"
        else:
            return "You can't leaglly drink inthe France"
    else:
        return "Country not recognized"

can_leagally_drink("France", 18)

# When you have a simple ccondition, you can write a conditional logic block
# in a single lineL that is called "TERNARY OPERATOR"

age = 20
status = "Adult" if age >= 18 else "minor"
# Value_if_true if condition else value_if_False

# Second trick, very useful and very common:
# A use case for conditional logic block is when you need output one value 
# depending on another value:
# Let's say I want to output the currency of a country, depending on the country name
# of course you can do :

def get_currency_country(country_name):
    if country_name == "France":
        return "Euro"
    elif country_name == "USA":
        return "US Dollars"
    elif country_name == "Canada":
        return "Canada Dollars"
    # many lines live there
    else:
        return "unknow country"

# Instead, a better solution:
country_currencies = {
    "USA": "US Dollars",
    "France": "Euro",
    "Canada": "Canada Dollars",
    "UK": "British Pounds",
    "Japan": "Yen",
    "China": "RMB"
} # this achieves the same structure, with much fewer words:

# How do we use this then ?
country_currencies["Canada"] # Achieves the same goal as a conditional block.
# But it only works if you want to match the same variable to different possible values.

# One small caveat:
country_currencies["Iran"] # Here, we get an error, with the function we should get " Unkonw country"....Error
# unless we use the .get() method that we saw before.
country_currencies.get("Iran") # you will get none which is not gonna cause a error