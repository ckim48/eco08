# 4 types of variables: Integer/Float/String/Boolean
# % - Modulo(Mod) --> Remainder
# ** -> exponents(power), ex) 2 ** 3 -->8

# Conditionals - Conditionals allow your program to make decisions.-->
#                Your program has the choices

x = 10
# if statements
# if (conditions):
# In python, indentation is very important
# The indentation determines the block of code that should be executed when
# the condition specified in the if statement is true
if x > 3:
    print("Big")
    print("This number is big")
elif x > 0: # else if
    print("Mid")
elif x > -5:
    print("Mid2")
print("Bye")

y = -100
# if y > 0:
#     print("A")
# if y > -5:
#     print("B")

if y > 0:
    print("A")
elif y > -5:
    print("B")
elif y > -10:
    print("C")
elif y > -15:
    print("D")
else:
    print("Else Else")

x = 3
y = 3
if x > y:
    print("X is bigger than Y")
else:
    print("Y is bigger or equal to X")

a = 14
#1
if a % 2 == 0:
    print("Even")
if a % 2 == 1:
    print("Odd")
#2
if a % 2 == 0:
    print("Even")
elif a % 2 == 1:
    print("Odd")
# 3
if a % 2 == 0:
    print("Even")
else:
    print("Odd")
# You need to know the different between '=' vs '=='
# We use '=' to assign a value to a variable
# We use '==' to compare two numbers

# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# if a > b:
#     print("First number is bigger than second number")
# elif a < b:
#     print("Second number is bigger than first number")
# else:
#     print("They are same number")

# score = float(input("Enter your numeric score: "))
# if score >= 90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")
# if 90<= score<=100:
#     print("A")
# elif 80<= score <90:
#     print("B")
# "==" checks same or not  5==3 --> False
# "!="  5 != 3 --> True

# score = float(input("Enter your numeric score: "))
# if score >= 90:
#     if score >=97: # Nested-if
#         print("A+")
#     elif score >=95:
#         print("A")
#     else:
#         print("A-")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# Logical Operators
# Write a program that prints True if the number is bigger than 50 and even number
# print False otherwise.

# a = int(input("Enter a number"))
# if a > 50:
#     if a % 2 == 0:
#         print("True")
#     else:
#         print("False")
# else:
#     print("False")
#
# if a > 50 and a % 2 ==0:
#     print("True")
# else:
#     print("False")
#
# if a > 50 or a % 2 ==0:
#     print("True")
# else:
#     print("False")

# A and B
# True and True --> True
# True and False --> False
# False and True --> False
# False and False --> False

# A or B
# True or True --> True
# True or False --> True
# False or True --> True
# False or False --> False

# Print True if the number is divisible by 3 or 7. Otherwise False
# a = 14
# if a % 3 == 0 or a % 7 == 0:
#     print("True")
# else:
#     print("False")

# username = "scott2023"
# password = "abcd"
#
# get_pass = input("Enter a password for 'scott2023")
# if get_pass == password:
#     print("Succesfully Login!")
# else:
#     print("Wrong Password")
#
name = input("What's your name?")
if name == "Harry":
    print("Grynffindor")
elif name == "Hermione":
    print("Grynffindor")
elif name == "Ron":
    print("Grynffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Grynffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")