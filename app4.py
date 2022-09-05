# --In this Tutoria, we are going to learn about strings in Python

# --Strings in Python are considard as objects that can be used to perform many tasks. Take your TV remote for example,
# --that contain all kind of buttons for different task on how to operate your tv, so is string inpython.
# --If you type course., you will find many cool strings capabilities that are available for course variable like:
# replace, upper, capitalization, casefold, count, center and many more
# Unlike the print and input function that is use for general purpose, the string functions here are specific to strings
# --These string functions in string object are considered as methods.
# --so when a function is part of an object string it call a method
########################################################################################################################

#---------------------------------------------------------------------------------------------------------------------
# --Here we are using an [upper] method.
#---------------------------------------------------------------------------------------------------------------------
# course = 'Python for beginners' # --This string variable here is considered an object
# print(course.upper()) # --Here we are using an [upper] method. If you run this code,
# # you should see the value of the string variable as upper case letters

# --If you run the above code you will get this result
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app4.py
# PYTHON FOR BEGINNERS

# Process finished with exit code 0

# --Running the upper method do not change the original string, for example:

# course = 'Python for beginners' # --This string variable here is considered an object
# print(course.upper()) # --Here we are using an [upper] method. If you run this code,
# print(course)
# # you should see the value of the string variable as upper case letters on one line and the original sring with no change

# --If you run the above code you will get this result:
# PYTHON FOR BEGINNERS
# Python for beginners
#
# Process finished with exit code 0

#----------------------------------------------------------------------------------------------------------------------
# Here we are using an [find] method. The find method is use to find characters or sequence of characters in a body of text.
#----------------------------------------------------------------------------------------------------------------------
# course = 'Python for beginners' # --This string variable here is considered an object
# print(course.find("y")) # --Here we are using an [find] method to the letter "y" in our string object.
# # you should see the value of the string variable as upper case letters on one line and the original sring with no change

# --If you run the above code you will get this result:
# 1   <<--[NOTE] This is because the letter "y" in [Python] is the 1 position on the index count --[0,1,2,3,4,5,]
#
# Process finished with exit code 0

#-----------------------------------------------------------------------------------------------------------------
# Here we are using an [find] method. The find method is use to find characters or sequence of characters in a body of text.
#-----------------------------------------------------------------------------------------------------------------

# course = 'Python for beginners' # --This string variable here is considered an object
# print(course.find("for")) # --Here we are using an [find] method to the letter "y" in our string object.
# # you should see the value of the string variable as upper case letters on one line and the original sring with no change

# --If you run the above code you will get this result:
# 7   <<--[NOTE] This is because the "for" in [Python [for] beginners] is the 7 position on the index count[0,1,2,3,4,5,6,7]
#
# Process finished with exit code 0

#-----------------------------------------------------------------------------------------------------------------
# Here we are using an [replace] method. This is used replace characters or sequence of characters in a body of text.
# --Just like the upper method, the replace method does not change the original string of the string.
#-----------------------------------------------------------------------------------------------------------------

# course = 'Python for beginners' # --This string variable here is considered an object
# print(course.replace("for", '4')) # --Here we are using an [find] method to the letter "y" in our string object.
# # you should see the value of the string variable as upper case letters on one line and the original sring with no change

# --If you run the above code you will get this result:
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app4.py
# Python 4 beginners
#
# Process finished with exit code 0

#--------------------------------------------------------------------------------------------------------------------
# course = 'Python for beginners' # --This string variable here is considered an object
# print(course.replace("for", '4')) # --Here we are using an [find] method to the letter "y" in our string object.
# print(course)
# # you should see the value of the string variable as upper case letters on one line and the original sring with no change

# --If you run the above code you will get this result:
# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe C:/Users/brown/PycharmProjects/helloWorld/venv/app4.py
# Python 4 beginners
# Python for beginners
#
# Process finished with exit code 0

#-----------------------------------------------------------------------------------------------------------------
# Here we are using an [in operator] The [in operator] is use to find characters or sequence of characters in a body of text.
#-----------------------------------------------------------------------------------------------------------------

# course = 'Python for beginners' # --This string variable here is considered an object
# print('Python' in course) # --Here we are using an [in operator] method to the letter "Python" in our course string object.
# --The value of a in operator is a Boolien True or False
# --If you run the above code you will get this result:
# True   <<--[NOTE] This is because the "for" in [Python [for] beginners] is the 7 position on the index count[0,1,2,3,4,5,6,7]
#
# Process finished with exit code 0
