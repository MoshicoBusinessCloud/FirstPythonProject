# --While loop is used to repeat a block of code multiple times
# The while loop requires relevant variables to be ready,
# in this example we need to define an indexing variable, i, which we set to 1

#######################################################################################################################
 #--While Loops--#   #--While Loops--#   #--While Loops--#   #--While Loops--#   #--While Loops--#   #--While Loops--#
#######################################################################################################################

#---[EXAMPLE]---#

# print("1")
# print("2")
# print("3")
# print("4")
# print("5")
# --This is not a good way to write the above block of code because if need
# --to print out number at great scale that will take long time to do.

# --If you run the above block code you will get the bellow result
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Users/brown/PycharmProvenv/app7-While-Loops.py
# 1
# 2
# 3
# 4
# 5
#
# Process finished with exit code 0
#######################################################################################################################
# --Using while loops [example bellow]is better way of writing the block of code
i = 1   # --This line is used to state the value of the condition

# while i <= 5: # --The is the condition that need to be met until it becomes false
#     print(i)  # --This is to print out the result of the condition
#     i = i + 1 # This line add one to the result everytime the system comes back to add 1 until the condition is false.

# --If you run the above block code and the one before you should the same result
# C:\Users\brown\PycharmProjects\helloWorld\venv\exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# 1
# 2
# 3
# 4
# 5
# 1
# 2
# 3
# 4
# 5
#
# Process finished with exit code 0
#######################################################################################################################
# --Using while loops [example bellow]is better way of writing the block of code
# i = 1
# #-------[If you you change the number of the condition it will execute it utill the condition becomes false.]-------#
# while i <= 1_000: # --The is the condition that need to be met until it becomes false
#     print(i)  # --This is to print out the result of the condition
#     i = i + 1 # This line add one to the result everytime the system comes back to add 1 until the condition is false.

# --If you run the above block code and the one before you should the same result
# C:\Users\brown\PycloWorld\venv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# 1
# 2
# 996
# 997
# 998
# 999
# 1000
#  As you can see this is more easier than writing 1000 line of codes
# Process finished with exit code 0
#######################################################################################################################

# --Using while loops [example bellow]is better way of writing the block of code
# --You ccan also w=hile loop to multiply expression
# i = 1
# #-------[If you you change the number of the condition it will execute it utill the condition becomes false.]-------#
# while i <= 10: # --The is the condition that need to be met until it becomes false
#     print(i * 'love')  # --Here we can multiply a number by a string to print out the result of the condition
#     i = i + 1 # This line add one to the result everytime the system comes back to add 1 until the condition is false.

# --If you run the above block code and the one before you should the same result
# C:\Users\brown\PycloWorld\venv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# love     # --[i = 1 = 1love]--#
# lovelove     # --[i = 1 + 1= 2love]--#
# lovelovelove     # --[i = 1 + 2 = 3love]--#
# lovelovelovelove     # --[i = 1 + 3 = 4love]--#
# lovelovelovelovelove     # --[i = 1 + 4 = 5love]--#
# lovelovelovelovelovelove     # --[i = 1 + 5 = 6love]--#
# lovelovelovelovelovelovelove     # --[i = 1 + 6 = 7love]--#
# lovelovelovelovelovelovelovelove     # --[i = 1 + 7 = 8love]--#
# lovelovelovelovelovelovelovelovelove     # --[i = 1 + 8 = 9love]--#
# lovelovelovelovelovelovelovelovelovelove     # --[i = 1 + 9 = 10love]--#
#
# Process finished with exit code 0


######################################################################################################################
# -----------------------------------LIST LIST LIST LIST LIST LIST LIST----------------------------------------------#
######################################################################################################################
#---[EXAMPLES]---#
# names = ["John", "James", "Jonah", "Josh", "Joe", "Jessy"]
# print(names)

# C:\Users\brown\PycharmProjevenv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# ['John', 'James', 'Jonah', 'Josh', 'Joe', 'Jessy']
#
# Process finished with exit code 0
#----------------------------------------------------------------------------------------------------------------------

# names = ["John", "James", "Jonah", "Josh", "Joe", "Jessy"]
# print(names [3]) # --index number in imperial bracket is used get individual element or elements from the list.
# --If we need to print only john use -[0], and if you want to print josh use --[3]

# C:\Users\brown\PycharmProjevenv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# John
# Process finished with exit code 0
#-----------------------------------------------------------------------------------------------------------------------

# --You can also use negertive numbers to call and print individual names on the list going from right ot left
# names = ["John", "James", "Jonah", "Josh", "Joe", "Jessy"]
# print(names [-2]) # --negertive index numbers can also be use to print names on the list backward [left<<---right]
# --index number in imperial bracket is used get individual element or elements from the list.
# --If we need to print only john use --[0], and if you want to print josh use --[3]

# C:\Users\brown\PycharmProjevenv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# Joe
# Process finished with exit code 0

# #-----------------------------------------------------------------------------------------------------------------------
#
# # --You can also use negertive numbers to call and print individual names on the list going from right ot left
# names = ["John", "James", "Jonah", "Josh", "Joe", "Jessy"]
# names [0] = "jon" # --This is used if you want to make change to a name on the list
# print(names) # --negertive index numbers can also be use to print names on the list backward [left<<---right]
# # --index number in imperial bracket is used get individual element or elements from the list.
# # --If we need to print only john use --[0], and if you want to print josh use --[3]

# C:\Users\brown\PycharmProjevenv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# ['jon', 'James', 'Jonah', 'Josh', 'Joe', 'Jessy']
# Process finished with exit code 0

#-----------------------------------------------------------------------------------------------------------------------

# --You can also use negertive numbers to call and print individual names on the list going from right ot left
# names = ["John", "James", "Jonah", "Josh", "Joe", "Jessy"]
# names [0] = "jon" # --This is used if you want to make change to a name on the list
# print(names[0:3]) # --index numbers can also be use this way if need to print only need to print specific names on the list
# print(names) # --Printing specific names o the list doesn't change the original list.
# # --index number in imperial bracket is used get individual element or elements from the list.
# # --If we need to print only john use --[0], and if you want to print josh use --[3]

# C:\Users\brown\PycharmProjects\helloWorld\venv\ScC:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# ['jon', 'James', 'Jonah']
# ['jon', 'James', 'Jonah', 'Josh', 'Joe', 'Jessy']
#
# Process finished with exit code 0

#######################################################################################################################
#---List Methods---#   #---List Methods---#   #---List Methods---#  #---List Methods---#  #---List Methods---#
#######################################################################################################################
#---[EXAMPLE] Using [Append]---#

# numbers = [1,2,3,4,5,6,]
# numbers.append(7) # --Append is use to add a number to a list
# print(numbers)
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Userects/helloWorld/venv/app7-While-Loops.py
# [1, 2, 3, 4, 5, 6, 7]
#
# Process finished with exit code 0
#======================================================================================================================

#---[EXAMPLE] Using [insert]---#

# numbers = [1,2,3,4,5,6,]
# numbers.insert(0, -1) # --insert is use to insert a number to a list at any index possition on the list.
# # here we are inserting [-1] before 1
# print(numbers)
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Userects/helloWorld/venv/app7-While-Loops.py
# [-1, 1, 2, 3, 4, 5, 6, 7]
#
# Process finished with exit code 0

#======================================================================================================================

#---[EXAMPLE] Using [remove]---#
#---[EXAMPLE] Using [insert]---#
#---[EXAMPLE] Using [Append]---#

# numbers = [1,2,3,4,5,6,]
# numbers.remove(4) # --insert is use to insert a number to a list at any index possition on the list.
# # here we are inserting [-1] before 1
# numbers.insert(0, -1)  # --insert is use to insert a number to a list at any index possition on the list.
# # # here we are inserting [-1] before 1
# numbers.append(7) # --Append is use to add a number to a list
# print(numbers)
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Userects/helloWorld/venv/app7-While-Loops.py
# [-1, 1, 2, 3, 5, 6, 7]
#
# Process finished with exit code 0

#======================================================================================================================

#---[EXAMPLE] Using [remove method]---#
#---[EXAMPLE] Using [insert method]---#
#---[EXAMPLE] Using [Append method]---#
#---[EXAMPLE] Using [clear  method]---#

# numbers = [1,2,3,4,5,6,]
# numbers.remove(4) # --insert is use to insert a number to a list at any index possition on the list.
# # here we are inserting [-1] before 1
# numbers.insert(0, -1)  # --insert is use to insert a number to a list at any index possition on the list.
# # # here we are inserting [-1] before 1
# numbers.append(7) # --Append is use to add a number to a list
# numbers.clear()  # --The clear method is use to clear the list and in this case, the clear method superceed all.
# print(numbers)

# --If you run the above block code, the [clear method] will have the last action and you will see an empty list [].
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Userects/helloWorld/venv/app7-While-Loops.py
# []
#
# Process finished with exit code 0

#======================================================================================================================

#---[EXAMPLE] Using [remove method]---#
#---[EXAMPLE] Using [insert method]---#
#---[EXAMPLE] Using [Append method]---#
#---[EXAMPLE] Using [in  method]---#
#---[EXAMPLE] Using [len  method]---#

# numbers = [1,2,3,4,5,6,]
# numbers.remove(4) # --insert is use to insert a number to a list at any index possition on the list.
# # here we are inserting [-1] before 1
# numbers.insert(0, -1)  # --insert is use to insert a number to a list at any index possition on the list.
# # # here we are inserting [-1] before 1
# numbers.append(7) # --Append is use to add a number to a list
# print(1 in numbers)  # --Use the [in] method to find a number on a list and it returns a boolien value, [True or False].
# print(numbers)
# print(len(numbers)) # --len is use to check how many items on a list.

# --If you run the above block code, you should see all the methods executed bellow.
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Userects/helloWorld/venv/app7-While-Loops.py
# True
# [-1, 1, 2, 3, 5, 6, 7]
# 7

# Process finished with exit code 0

#######################################################################################################################
#---Using For Loops VS While Loops---#  #---Using For Loops VS While Loops---#  #---Using For Loops VS While Loops---#
#######################################################################################################################

#---[EXAMPLE] Using [remove method]---#

# numbers = [1, 2, 3, 4, 5 ,6,] # --Declearation of numbers
# for item in numbers:  # --This is [For Loop] variable sting, and it use to print out items on separate line
#     print(item)
#
# #  --if you compare the two you will that the for loop is much easier and shorter than the while loop
# # --One, we dont have to use sqare bracket notation, the len function, we dont have to declear a loop variable, and
# # we dont vave to write another line to increment it explicitely.
# i = 0
#
# while i < len(numbers):
#     print(numbers[i])  # --This is [While Loop] variable sting, and it use to print out items on separate line
#     i = i + 1
# --If you run the above block code, you should see one set of numbers for [For Loop] and [While Loop].
# C:\Users\brown\PycharmProjects\hel\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# 1
# 2
# 3
# 4
# 5
# 6
#----------------For Loop above and While Loop bellow
# 1
# 2
# 3
# 4
# 5
# 6
#
# Process finished with exit code 0

#######################################################################################################################
#---THE RANGE() FUNCTION---#                 #---THE RANGE() FUNCTION---#                  #---THE RANGE() FUNCTION---#
#######################################################################################################################

# numbers = range(5) # --Declearation of numbers
# # for numbers in numbers:  # --This is [For Loop] variable sting, and it use to print out items on separate line
# print(numbers)

# --If you run the above block code, you should see this:
# range(0, 5)
#
# Process finished with exit code 0

#=======================================================================================================================

# numbers = range(5) # --This Declearation print the numbers 0 ---4
# numbers = range(5, 10) # This Declearration will display a range of 5 to 10 but will only display 5 to 9 shown bellow.
# numbers = range(5, 10, 2)  # --This Declearation is use to count in sequence of 2 as shown bellow.
# for numbers in range(10):  # --This is [For Loop] variable sting, and it use to print out items on separate line
# # --You can also use the for loop to declear the variable without writing a different line of code for the variable.
#     print(numbers)
#-----------------------------------------------------------------------------------------------------------------------
# --If you run the above block code, you should see this:
# 0
# 1
# 2                      range(5) function
# 3
# 4

# Process finished with exit code 0
#-----------------------------------------------------------------------------------------------------------------------
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exen/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# 5
# 6
# 7                      range(5, 10) function
# 8
# 9
#
# Process finished with exit code 0
#-----------------------------------------------------------------------------------------------------------------------
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exen/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# 5
# 7                     numbers = range(5, 10, 2)  function
# 9
#
# Process finished with exit code 0
#-----------------------------------------------------------------------------------------------------------------------
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe/PycharmProjects/helloWorld/venv/app7-While-Loops.py
# 0
# 1
# 2
# 3
# 4
# 5                     for numbers in range(10): function
# 6
# 7
# 8
# 9
#
# Process finished with exit code 0

########################################################################################################################
#----------------TUPLES--------------#   #----------------TUPLES--------------#   #----------------TUPLES--------------#
########################################################################################################################
#---[EXAMPLE] Using [Tuples in Python are immutable or unchangeable. tuples cannot be change once they are created]---#

numbers = (1, 2,2,2, 3, 4,4,4,4,4, 5, 6,6,6,6) # unlike list where you use [bracket to define a list], with tuples you use parentences
numbers.count(4)

print(numbers)