# ************Use input***************
# name = input("What's your name?")
# age = input("How old are you?")
# print(f"Hello, your name is: {name} and your age is: {age}")
from curses.textpad import rectangle
from logging import exception

# orange_input = input ("Please, Enter number of orange you take: ")
# oranges_number = 5 - int(orange_input)
# print(f"Total amount avoid of oranges is {str(oranges_number)}")

# ***************Nested Loop*****************
# for num1 in range(2):
#     for num2 in range(2):
#         print(f"[{num1}, {num2}]")

# for char1 in "mahmoud":
#     for char2 in "Barakat":
#         print(f"{char1} {char2}")

# *************Program Gues Number between 1 : 10 ************
# num = 7
# chance = 0
# while chance <= 2:
#     guess_num = input ("Please Enter Guess Number between 0 to 10 : ")
#     if num == int(guess_num):
#         print("Bravo!!")
#         break
#     else:
#         print("Try , Again: ")
#         chance +=1

# ************Program to replace o to 0 *************
# message = "Good morning Mahmoud Barakat"
# res = ""
# for char in message:
#     if char.lower() == "o":
#         res += "0"
#     else:
#         res += char
# print(res)

# **********Program to return even or odd number************
# def is_num_even_or_odd(num):
#     if num % 2 == 0:
#         print("This Number is even")
#     elif num % 2 !=0:
#         print("This Number is odd")
#
# is_num_even_or_odd(10)

# **********Program to calculate grade percentage**********
# def calc_grade_percentage(grade, full_mark=50):
#     print((grade/full_mark) *100)
#
# calc_grade_percentage(34, 70)

# class Color():
#     def black(self):
#         print("Black")
#     def blue(self):
#         print("Blue")
#
# color1 = Color()
# color1.blue()
# color1.black()
# color1.red = "Red"
# print(color1.red)

# ************Program to calculate rectangle area*************
# class Rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def rectangle_area(self):
#         area = self.width * self.length
#         print(f"Rectangle Area = {area}")
#
# rectangle1 = Rectangle(3,4)
# rectangle1.rectangle_area()

# *************try and except******************
# a = 5
# try:
#     print(b)
# except:
#     print("Error")