### List Comprehensions
# x = int(input("Please enter a number"))
# y = int(input("Please enter a number"))
# z = int(input("Please enter a number"))
# n = int(input("Please enter a number"))
# result = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 result.append([i,j,k])
# print(result)


### Find the Runner-Up Score!
# n = int(input())
# numbers = list(map(int, input().split()))
# numbers = list(set(numbers))   # إزالة التكرار
# numbers.sort()                 # ترتيب القائمة
# print(numbers[-2])             # ثاني أكبر عنصر


### Nested Lists
# students = []
# number_of_student = int(input("Enter Number of Student"))
# for n in range(number_of_student):
#     name = input("Enter Name")
#     grade = float(input("Enter Grade"))
#     students.append([name, grade])
# print(students)
#
# # استخراج الدرجات فقط
# grades = [s[1] for s in students]
# print("Grades",grades)
#
# # # ترتيب الدرجات المميزة
# unique_grades = sorted(set(grades))
# print('Unique Grades',unique_grades)
#
# # # ثاني أقل درجة
# second_lowest = unique_grades[1]
# print('Second Lowest',second_lowest)
#
# # # أسماء الطلاب الذين لديهم ثاني أقل درجة
# names = [s[0] for s in students if s[1] == second_lowest]
#
# # # ترتيب الأسماء أبجديًا
# names.sort()
# for name in names:
#     print(name)


### Finding the percentage
# n = int(input("Enter Number Of Students"))
# student_marks = {}
# for _ in range(n):
#     data = input("Enter Data Of Student").split()
#     name = data[0]
#     scores = list(map(float, data[1:]))
#     student_marks[name] = scores
#
# query_name = input("Enter Name Of student")
# marks = student_marks[query_name]
# average = sum(marks) / len(marks)
# print(f"{average:.2f}")