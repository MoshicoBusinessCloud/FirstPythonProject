# weight =input("Weight: ")
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + converted)
# else:
#     converted = weight * 0.45
#     print("Weight in Kgs: " + converted)

# Weight: 210
# (K)g or (L)bs: l
# Traceback (most recent call last):
#   File "C:\Users\brown\PycharmProjects\helloWorld\venv\app6-weight calculator.py", line 7, in <module>
#     [[[converted = weight * 0.45] <<--[NOTE]the reason for the error is because we are trying multiply string and integer
# TypeError: can't multiply sequence by non-int of type 'float'
#
# Process finished with exit code 1
###2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

# weight = int(input("Weight: ")) # first we called the input function and ask the first question, [Weight]
# # and stored lavue in a variable called weight. Then, Putting [int] before the input function convert [Weight to an [integer]]
# unit = input("(K)g or (L)bs: ")  # Then we called the second input function and ask the second question, is this in
# # [(K)g or (L)bs]? And we stored that value in a variable called unit.
# if unit.upper() == "K":  # You add upper here because the the value from the input variable "K" is upper-case letter
#     converted = weight / 0.45  # Here we dividing a float into an integer, the value is a float. [converted = float]
#     print("Weight in Lbs: " + converted)  # there will be error here if you run the code without putting [str]
#     # before converted. this is because you cannot print or concatenate a string and a float:
#     # --Solution: Add [str] to converted with str(converted) in a bracket
# else:
#     converted = weight * 0.45  # Here we multiplying an integer and a float, the result is [converted]==[float]
#     print("Weight in Kgs: " + converted) # there will be error here if you run the code without putting [str]
#     # before converted. this is because you cannot print or concatenate a string and a float:
#     # --Solution: Add [str] to converted with str(converted) in a bracket

# C:\Users\brown\PycharmProjects\helloWorld\venv\Scripts\python.exe "C:/Users/brown/Pld/venv/app6-weight calculator.py"
# Weight: 210
# (K)g or (L)bs: l
# Traceback (most recent call last):
#   File "C:\Users\brown\PycharmProjects\helloWorld\venv\app6-weight calculator.py", line 27, in <module>
#     [[print("Weight in Kgs: " + converted)]] <<---[NOTE] You have to add str before converted --[str(converted)]
# TypeError: can only concatenate str (not "float") to str
#
# Process finished with exit code 1
###2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

weight = int(input("Weight: ")) # first we called the input function and ask the first question, [Weight]
# and stored lavue in a variable called weight. Then, Putting [int] before the input function convert [Weight to an [integer]]
unit = input("(K)g or (L)bs: ")  # Then we called the second input function and ask the second question, is this in
# [(K)g or (L)bs]? And we stored that value in a variable called unit.
if unit.upper() == "K":  # You add upper here because the the value from the input variable "K" is upper-case letter
    converted = weight / 0.45  # Here we dividing a float into an integer, the value is a float. [converted = float]
    print("Weight in Lbs: " + str(converted))  # Here we multiplying an integer and a float, the result is [converted]==[float]
else:
    converted = weight * 0.45  # Here we multiplying an integer and a float, the result is [converted]==[float]
    print("Weight in Kgs: " + str(converted)) # there will be error here if you run the code without putting [str]
    # before converted. this is because you cannot print or concatenate a string and a float:
    # --Solution: Add [str] to converted with str(converted) in a bracket

    # --If you run the above code to convert Lbs into Kg, you will get the bellow result
    # Weight: 201
    # (K)
    # g or (L)
    # bs: l
    # Weight in Kgs: 90.45
    #
    # Process
    # finished
    # with exit code 0
#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

weight = int(input("Weight: "))  # first we called the input function and ask the first question, [Weight]
# and stored lavue in a variable called weight. Then, Putting [int] before the input function convert [Weight to an [integer]]
unit = input("(K)g or (L)bs: ")  # Then we called the second input function and ask the second question, is this in
# [(K)g or (L)bs]? And we stored that value in a variable called unit.
if unit.upper() == "K":  # You add upper here because the the value from the input variable "K" is upper-case letter
    converted = weight / 0.45  # Here we dividing a float into an integer, the value is a float. [converted = float]
    print("Weight in Lbs: " + str(
        converted))  # Here we multiplying an integer and a float, the result is [converted]==[float]
else:
    converted = weight * 0.45  # Here we multiplying an integer and a float, the result is [converted]==[float]
    print("Weight in Kgs: " + str(converted))  # there will be error here if you run the code without putting [str]
    # before converted. this is because you cannot print or concatenate a string and a float:
    # --Solution: Add [str] to converted with str(converted) in a bracket

    # --If you run the above code to convert Kg into Lbs, you will get the bellow result

    # Weight: 94
    # (K)
    # g or (L)
    # bs: k
    # Weight in Lbs: 208.88888888888889
    # Weight: