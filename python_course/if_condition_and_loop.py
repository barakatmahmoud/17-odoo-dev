###
#
#
# IF Condition
#
#
###

# invoice = int(input("Please Enter Your Invoice: "))
# first_visit = False
#
# if first_visit:
#     if invoice <= 1000:
#         print("Your Discount will be 20%")
# else:
#     if 0< invoice <= 1000:
#         print("Your Discount will be 10%")
#     elif 1000< invoice <=2000:
#         print("Your Discount will be 20%")
#     else:
#         print("Your Discount will be 25%")

# grade = 55
# print("You Passed" if grade>50 else "You Failed")


#### ****IF Condition Example**** #################
# admins = ['Ahmed', 'Mahmoud', 'Esraa', 'Mazen']
# #Login Process
# name = input("Enter Your Name: ").strip().capitalize()
# if name in admins:
#     print(f"Hello {name}")
#     option = input("Update or Delete your name? ").strip().capitalize()
#     if option == 'Update' or option == 'U':
#         new_name = input("Enter Your new name ").strip().capitalize()
#         admins[admins.index(name)] = new_name
#         print("UPDATED.")
#         print(admins)
#     elif option == 'Delete' or option == 'D':
#         admins.remove(name)
#         print("DELETED.")
#         print(admins)
#     else:
#         print("Your choose wrong options")
# else:
#     print("Your name not in admin")

###
#
#
# Loop
#
#
###

#### ***while Loop*** ####
# x = 0
# while x < 10:
#     print(x)
#     x += 1
# print("While Loop Done")

# correct_password = "Asd@123"
# input_password = input("Please Enter Password ")
# tries = 3
# while correct_password != input_password:
#     tries -=1
#     print(f"Password Wrong, You have {tries} Chance Left")
#     input_password = input("Please Enter Password")
#     if tries == 0:
#         print("All Tries Finished!!")
#         break
# else:
#     print("Correct Password")

#### ****for loop**** #####
# my_numbers = [1,2,3,4,5,6,7,8,9]
# for i in my_numbers:
#     if i % 2 ==0:
#         print(f"{i} Is Even Number")
#     elif i % 2 != 0:
#         print(f"{i} Is Odd Number")
# else:
#     print("Loop Finished")

#### **** loop in dictionary**** #####
# my_skills = {
#     'Html': '80%',
#     'Css': '50%',
#     'Python': '70%',
#     'OOP': '65%',
# }
#
##### ****1st Way*** ####
# for skill in my_skills:
#     print(f"My Skills is {skill} and Degree {my_skills.get(skill)}")
#
##### ***2nd Way ****####
# for skill_key, skill_value in my_skills.items():
#     print(f"{skill_key} and >> {skill_value}")