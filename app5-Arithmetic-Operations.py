# --This Tutoria shows all the arithmetics operators in Python, and these are the same arithmetics that we have in Math.
# --We can add, subtract, multiply, divide, and much more. Bellow are some simple maths lessons.

# print(10 + 11)  # This is addition operator
# print(18 - 5)   # This is subtraction operator
# print(20 * 3)   # This is multiplication operator
# print(20 / 4)   # This is division operaor and if the division result is evenly divided, it will disply an integer number
# print(25 / 3)   # This is division operaor and if the division result is not evenly divided, it will disply a floating number
# print(25 // 3)  # This is division operaor. When you use double // forward slash, you will get an ininteger
# print(10 % 3)   # This is moduless operaor. The percentage sign gives you what left after you divide a number
# print(10 ** 3)  # This is exponent operaor. Double asterisk is use for raising power, 10^3 power. and it is called exponent

# --AugmentedAugmented assignment is the name given to certain assignment operators in certain programming languages.
# An augmented assignment is generally used to replace a statement where an operator takes a variable as one of its
# arguments and then assigns the result back to the same variable.
# X = 10
# X = X + 5 # Bellow are different ways to use orgmented assignment operator
# X += 5
# X -= 5
# X *= 5
# X /= 5
# print(X)

# --If you run the above code you will get this result:
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Users/brown/Pycvenv/app5-Arithmetic-Operations.py
# 21
# 13
# 60
# 5.0
# 8.333333333333334
# 8
# 1
# 1000
#
# Process finished with exit code 0
########################################################################################################################
# --Operator Precedence   --Operator Precedence   --Operator Precedence   --Operator Precedence  --Operator Precedence
########################################################################################################################

# X = 10 + 3 * 2 # --When you print this line you will [16]. This is because in math, multiplication and division are given
# # higher order than adddition and subtraction. [3*2=6 + 10 = 16]
# X = (10 + 3) * 2  # --When you print this line you will [26]. In Python operator precedent is also the same as in maths,
# # but you can change this by adding parentheses or bracket --[(10 + 3)=13 * 2 = 26]
# print(X)

#-----------------------------------------------------------------------------------------------------------------------
# --Comparison Operators     # --Comparison Operators     # --Comparison Operators     # --Comparison Operators
#-----------------------------------------------------------------------------------------------------------------------
# --Comparison operator are use to compare values and it called a [Boolien expression].
# --the value of the boolien expression are given as boolien --[True] OR [False]
# X = 3 > 2
# print(X)
# --If you run the above code you will get this result:
# True
#
# Process finished with exit code 0
# --These are different types of boolien expresssions
# X = 3 >= 2 # Greater or equal to
# X = 3 < 2  # Lesser than
# X = 3 <= 2 # Lesser or equal to
# X = 3 == 2 # Equal to
# X = 3 != 2 # NOT equal to

#----------------------------------------------------------------------------------------------------------------------
# --Logical Operators     --Logical Operators     --Logical Operators    --Logical Operators     --Logical Operators
#----------------------------------------------------------------------------------------------------------------------
# This shows that price is greater than 10
# price = 25
# print(price > 10)
# --If you run the above code you will get this result:
# True
#
# Process finished with exit code 0
#----------------------------------------------------------------------------------------------------------------------

# This shows that price is greater than 10 and lesser than 30 [Using [and]]
# price = 25
# print(price > 10 and price < 30)  #<<--[NOTE] Two values that are true is equal to True
# # --If you run the above code you will get this result:
# True
#
# Process finished with exit code 0
#----------------------------------------------------------------------------------------------------------------------

# This shows that price is greater than 10 or lesser than 30 [Using [or]]
# price = 15
# print(price > 10 or price < 30)  #<<--[NOTE] Two statements that are true and two statements that have only one true
# are considered to be True. And two statements that are false are considered to be false

# # --If you run the above code you will get this result:
# True
#
# Process finished with exit code 0
#----------------------------------------------------------------------------------------------------------------------

# This shows that price is NOT greater than 10, which is false, but when you add [not] it is true [Using [not]]
# price = 5
# print(not price > 10)  #<<--[NOTE] The statement price > 10 is false, but adding [not] before price will make the
# the statement true

# # --If you run the above code you will get this result:
# True
#
# Process finished with exit code 0

#######################################################################################################################
# --The If Statements   # --The If Statements    # --The If Statements   # --The If Statements   # --The If Statements
#######################################################################################################################

#   If statements are use to make decisions in Python.
#--[EXAMPLE]--[Temperature is greater than]

# temperature = 35
#
# if temperature > 30:
#     print("it's a hot day")
#     print("Drink plenty of water")

# --If you run the above code you will get this result if the condition is true
# --and if the condition if false it will not print the message. In this case the temperature is greater than 30.
# it's a hot day
# Drink plenty of water
#
# Process finished with exit code 0
#----------------------------------------------------------------------------------------------------------------------

#--[EXAMPLE]--[Temperature is lesser than] with-->>[if]
# temperature = 25
#
# if temperature > 30:
#     print("it's a hot day")
#     print("Drink plenty of water")
# print("Done")
# --If you run the above code you will see only Done, this is because the print line is not part of the if block
# --and the temperature is not grater than 30
# Done
#
# Process finished with exit code 0
#----------------------------------------------------------------------------------------------------------------------

#--[EXAMPLES]--[Temperature is greater than] with-->>[elif]

# temperature = 25
#
# if temperature > 30:
#     print("it's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a Nice Day")
#     print("take your kids to the park")
# print("Done")
# --If you run the above code you will see only the messages from the elif, and print line
# this is because the print line is not part of the if and elif block and the temperature is grater than 20 < 30.

# It's a Nice Day
# take your kids to the park
# Done
#
# # Process finished with exit code 0
#----------------------------------------------------------------------------------------------------------------------

#--[EXAMPLES]--[Temperature is greater than] with-->>[elif]

temperature = 25

if temperature > 30:             # <<--[NOTE] --This statement is false and will not be printed
    print("it's a hot day")
    print("Drink plenty of water")
elif temperature > 20:           # <<--[NOTE] --This statement is true and will be printed
    print("It's a Nice Day")
    print("take your kids to the park")
elif temperature > 10:           # <<--[NOTE] --This statement is true and will not be printed because there is a true
    # statement before this one and the system print the first true statement.
    print("It's a bit cold outside")
    print("Please dress warm")
else:
    print("It's cold")    # <<--[NOTE] --if all the statements above are false, then this will be printed
print("Done")
# --If you run the above code you will see only the messages from the elif, and print line
# this is because the print line is not part of the if and elif block and the temperature is grater than 20 < 30.

# It's a Nice Day
# take your kids to the park
# Done
#
# # Process finished with exit code 0