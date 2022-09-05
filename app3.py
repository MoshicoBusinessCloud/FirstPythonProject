# --There are three types of data in Python:
numbers = 10
string = "Moses"
boolean = True or False

# --Type Conversions
# --This are some of the built in function for converting variables
# --int()   <<--[This is use for converting a value to and integer]
# --float() <<--[This is use for converting a value to flooting number [10.2 to 10] ]
# --bool()  <<--[This is use for converting a value to a boolien]
# --str()   <<--[This is use for converting a value to a string]
####################################################################################################################
# --The function is to read a user age. if you enter the year you were born, this function ca tell your age
# --When calling a function, the return value is a string even if the input as a number, the value is always a string
# birth_year = input("Enter your birth year: ")  # --This is an input function stored in a variable called [birth_year]
# age = 2022 - int(birth_year)  # --The [int] before [birth_year] is converting the values from strings to integers
# print(age)   # --The print function and the [age] in the bracket will print out your age.

###################################################################################################################
###################################################################################################################

# -- This function is to build a calculator program that takes only integers.
# --When calling a function, the return value is a string even if the input as a number, the value is always a string
first = input("first ") # --This is an input function stored in a variable called [first]
second = input("second ") # --This is an input function stored in a variable called [second]
sum = first + second  # --The return vavlue [first] is a string, so is the return value [second]
# --It should be writting as int(first) + int(second) = what ever numbers you calculating
print(sum)
# --If you run the above code you will get this result
# first 12
# second 13
# 1213  # --You get this result because the function cannot add strings, so it prints 12 and 13 instead of 12+13


first = input("first ") # --This is an input function stored in a variable called [first]
second = input("second ") # --This is an input function stored in a variable called [second]
sum = int(first) + int(second) # --The [int] before [first] and [second] is converting
#--the values from strings to integers
print(sum) # --And print function and the [sum] in the bracket will print out the answer of your calculation.

#############################################################################################################
#############################################################################################################

# -- This function is to build a calculator program that takes both floats and integers.
# --When calling a function, the return value is a string even if the input as a number, the value is always a string
first = input("first ") # --This is an input function stored in a variable called [first]
second = input("second ") # --This is an input function stored in a variable called [second]
sum = first + second  # --The return vavlue [first] is a string, so is the return value [second]
# --It should be writting as int(first) + int(second) = what ever numbers you calculating
print(sum)
# --If you run the above code you will get this result
# first 12
# second 13
# 1213  # --You get this result because the function cannot add strings, so it prints 12 and 13 instead of 12+13
#------------------------------------------------------------------------------------------------------------
# --To use this calcutor with a floating point numbers -[10.2] or [11.5] change the converting tool to float
# --Example --float(first) + float(second) once this is done you can calculate decimer points.
#--------------------------------------------------------------------------------------------------------------

# first = input("first ") # --This is an input function stored in a variable called [first]
# second = input("second ") # --This is an input function stored in a variable called [second]
# sum = float(first) + float(second) # --The [int] before [first] and [second] is converting
# #--the values from strings to integers
# print(sum) # --And print function and the [sum] in the bracket will print out the answer of your calculation.
#
# --If you run the above code you will get this result:
# first 10.9
# second 10
# 20.9
#
# Process finished with exit code 0
# ------------------------------------------------------------------------------------------------------------------
# --To display a label showing the answer to whatever you calculate, write the print funcution line this way
# --print("sum: " + str(sum):
# ------------------------------------------------------------------------------------------------------------------
# first = input("first ") # --This is an input function stored in a variable called [first]
# second = input("second ") # --This is an input function stored in a variable called [second]
# sum = float(first) + float(second) # --The [float] before [first] and [second] is converting
# #--the values from integer to float and the value from the sum is a float.
# print("sum: " + str(sum)) # --The reason for adding [str] before sum is to change [sum=float] to a string.
# # --This is because the system can only concatenate strings --["sum"] + ["sum"] and not ["Sum"] + [29.9]=floats.
#
# ------------------------------------------------------------------------------------------------------------------
# --We can also wtite the above code this way as shown bellow bay adding the conversion float to function variable:
# ------------------------------------------------------------------------------------------------------------------
# first = float(input("first ")) # --This is an input function stored in a variable called [first]
# second = float(input("second ")) # --This is an input function stored in a variable called [second]
# sum = first + second # --The [float] before [first] and [second] is converting
# #--the values from integer to float and the value from the sum is a float.
# print("sum: " + str(sum)) # --The reason for adding [str] before sum is to change [sum=float] to a string.
# --This is because the system can only concatenate strings --["sum"] + ["sum"] and not ["Sum"] + [29.9]=floats.
#
# --If you run the above code with numbers bellow, you should get this result:
# first 12.9
# second 21.1
# sum: 34.0
#
# Process finished with exit code 0