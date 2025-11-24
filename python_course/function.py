###
#
#
# Function
#
#
###

# def sum_numbers(n1, n2):
#     if type(n1) != int or type(n2) != int:
#         print("Only Integer Number!!")
#     else:
#         print(n1+n2)
#
# sum_numbers(3,'4')

#### ****packing and unpacking arguments**** ##### tuple
# my_list = [1,2,3,4]
# print(*my_list)


# def say_hello(*people):
#     print("People >>>>>>>", *people)
#     for name in people:
#         print(f"Hello {name}")
#
# say_hello("Ahmed", "Ali", "Nadin")

#### ****keyword arguments**** ##### dictionary
# def show_skills(**skills):
#     for skill_key , skill_value in skills.items():
#         print(f"{skill_key} >> {skill_value}")
#
# show_skills(Html="40%", Css="50%", Python="40%")

##### ****recursion function***#######
# def clean_word(word):
#     if len(word) <= 1:
#         return word
#
#     if word[0] == word[1]:
#         return clean_word(word[1:])
#
#     return word[0] + clean_word(word[1:])
# print(clean_word("wwwooorrrldd"))

#### ****lambda function****#########
# hello = lambda name: print(f"Hello{name}")
# hello(" Ahmed")

##### ****map function*****#####
# def format_text(text):
#     return (f"- {text} -")
#
# my_texts = ["Ahmed", "Ali", "Sara"]
# for name in map(format_text,my_texts):
#     print(name)

###### *****filter*****########
# def check_number(number):
#     if number > 10:
#         return number
# my_numbers = [1,3,5,9,11,45]
# my_results = filter(check_number, my_numbers)
# for num in my_results:
#     print(num)

# names = ["Ali", "Ahmed", "Mahmoud", "Nadin"]
# filtered_names = filter(lambda x : x.startswith("A"), names)
# for n in filtered_names:
#     print(n)

# def is_even(n):
#     return n % 2 == 0
# numbers = [1, 2, 3, 4, 5, 6]
# result = filter(is_even, numbers)
# print(list(result))

# numbers = [10, 15, 20, 25]
# result = filter(lambda x: x > 15, numbers)
# print(list(result))