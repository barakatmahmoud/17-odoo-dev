###
#
#
# String Methods
#
#
###


# ### len() ###
# text1 = "I love Egypt"
# print (len(text1))
#
# ### strip(), rstrip(), lstrip() ###
# text2 = "      I love Egypt   "
# print(text2.strip())
# print(text2.rstrip())
# print(text2.lstrip())
#
# ### title() ###
# print(text1.title())
#
# ### capitalize() ###
# print(text1.title())
#
# ### zfill ###
# a1 , a2, a3 = "1", "11", "111"
# print(a1.zfill(3))
#
# ### upper ###
# print(text1.upper())
#
# ### lower ###
# print(text1.lower())
#
# ### split() ,, rsplit() ###
# text3 = "Mahmoud Ali Barakat"
# print(text3.split(" ",1))
#
# ### swapcase() ###
# print(text3.swapcase())
#
# ### startswith(), endswith() ###
# text4 = "_ I love egypt"
# print(text4.startswith("_"))
#
# ### index() , find() ###
# text5 = "I love my Family"
# print(text5.index("v"))
# print(text5.find("F"))
#
# ### rjust() , ljust() ###
# text6 = "Ahmed"
# print(text6.rjust(10,"*"))
# print(text6.ljust(10,"*"))
#
# ### splitlines() ###
# text7 = """
# Ahmed
# Ali
# Barakat
# """
# print(text7.splitlines())
#
#
# ### replace() ###
# text8 = "one one one two one three"
# print(text8.replace("one", "1",1))
#
# ### join(iterable) ###
# l1 = ["Ahmed", "Ali", "Sara"]
# print(" ".join(l1))
#
# ### Example1 ###
# name = "Mahmoud"
# age = 27
# country = "Egypt"
# print(f"My name is {name} \n and my age is {age} \n and my country is {country}")
#
#
# ### Example2 ###
# name = "elzero"
# print(name[1:3], "\n", name[3], "\n")
#
# ### Example3 ###
# name = "#@#@Elzero#@#@"
# name_s = (name.split("#@#@"))
# print(" ".join(name_s))
#
# # Example4 ###
# msg = "I Love Python And Although Love Elzero Web School"
# print(msg.count("Love"))

###
#
#
# List Methods
#
#
###


# ### append() ###
# l1 = ["Ahmed", "ali", "Sara"]
# l1.append("Mazen")
# print(l1)
#
# ### extend() ###
# l2 = ["Maryum", "Nadin"]
# l1.extend(l2)
# print(l1)
#
# ### remove() ###
# l2.remove("Maryum")
# print(l2)
#
# ### sort() ###
# l3 = [4,7,0,-1,66]
# l3.sort()
# print(l3)
#
# ### clear() ###
# l4= [1,2,3,4,5]
# l4.clear()
# print(l4)
#
# ### copy() ###
# l5= ["Ali", "Sayed", "Mazen"]
# l6 = l5.copy()
# print(l5)
# print(l6)
# l5.append("RRR")
# print(l5)
# print(l6)
#
# ### count() ###
# l5= ["Ali", "Sayed", "Mazen", "Ali"]
# print(l5.count("Ali"))
#
# ### index() ###
# print(l5.index("Mazen"))
#
# ### insert() ###
# l5.insert(0, "Sara")
# print(l5)
#
# ### pop() ###
# l5.pop(0)
# print(l5)

### Example1 tuple##
# friends = ("Osama", "Ahmed", "Sayed")
# friends_list = list(friends)
# friends_list[0] = "elzero"
# print(friends_list)


###
#
#
# Set Methods
#
#
###

# s1 = {"Ahmed", "Ali", 3,(1,2,3)} #only accept immutable data like (string, number, tuple)
# ### clear() ###
# s1.clear()
# print(s1)
#
# ### union() ###
# s2 = {"Sara", "Mohamed", 4, 5}
# s3 = {"Karem", "Marwan", 6,(7,8,9)}
# print(s2.union(s3))
# print(s2 | s3)
#
# ### add() ### only add one item
# s2.add("Osama")
# print(s2)
#
# ### copy() ### sallow copy
# s4 = s2.copy()
# print(s4)
#
# ### remove() ###
# s4.remove("Sara")
# print(s4)
#
# ### discard() ###
# s4.discard(4)
# print(s4)
#
# ### pop() ###
# print(s4.pop())
#
# ### difference() ###
# a = {1,2,3, "x", "y"}
# b = {3,4,5 , "y", "z"}
# print(a.difference(b))
#
# ### difference_update() ###
# a.difference_update(b)
# print(a)
#
# ## intersection() ###
# print(a.intersection(b))
#
# ## intersection_update() ###
# a.intersection_update(b)
# print(a)
#
# ## symmetric_difference()
# print(a.symmetric_difference(b))
#
#
# ## symmetric_difference_update()
# a.symmetric_difference_update(b)
# print(a)
#
# ### issuperset() ###
# x = {1,2,3,4}
# y = {1,2,3}
# print(x.issuperset(y))
#
# ### issubset() ###
# print(y.issubset(x))
#
# ### isdisjoint() ###
# print(x.isdisjoint(y))
