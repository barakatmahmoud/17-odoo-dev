###
#
#
# Class, Object, Instance att,
#
#
###

#### ***class and create new obj**** ####
###create new class###
# class Car:
#     pass
###create new object###
# my_car = Car()

###Instance attribute###
# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand      # instance attribute
#         self.year = year        # instance attribute
#
# my_car = Car("Toyota", 2020)
# print(my_car.brand)

###Instance method###
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hello(self):   # instance method
#         print("Hello, I am", self.name)
#
# p = Person("Omar")
# p.say_hello()

###Class att and Class method###
# class Person:
#     count = 0 ## Class att
#
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls): ## Class method
#         return cls.count
#
# Person("Ali")
# Person("Sara")
# print(Person.get_count())

###Class static###
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# print(Math.add(5, 3))

### Example Class, Object, Object att, Object method, Class att, Class method, Static method###
# class Person:
#     species = "Human"  # class attribute
#     counter = 0
#
#     def __init__(self, name, age):
#         self.name = name            # instance attribute
#         self.age = age
#         Person.counter += 1
#
#     def say_hi(self):               # instance method
#         print(f"Hi, I'm {self.name}")
#
#     @classmethod
#     def get_counter(cls):           # class method
#         return cls.counter
#
#     @staticmethod
#     def is_adult(age):              # static method
#         return age >= 18
#
#
# p1 = Person("Ali", 20)
# p2 = Person("Sara", 15)
#
# p1.say_hi()                 # instance method
# print(Person.get_counter()) # class method
# print(Person.is_adult(20))  # static method

###
#
#
# Inheritance
#
#
###
### Example of inheritance ###
# class Parent():
#     pass
# class Child(Parent):
#     pass
#
# class Animal:
#     def eat(self):
#         print("I can eat")
#
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
#
# d = Dog()
# d.eat()     # inherited from Animal
# d.bark()    # in Dog

### ***Inherit __init__ constructor*** ###
### If the child class has no __init__, it uses the parent's.
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Student(Person):
#     pass
#
# s = Student("Ali")
# print(s.name)

###Child replaces parent behavior.
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Student(Person):
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
# s = Student("Ali", 50)
# print(s.grade)

#### If I create __init__ and i want to inherit super __init__
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)   # call parent __init__
#         self.grade = grade
#
# s = Student("Ali",40)
# print(s.name)

###***Method Overriding***###
# class Animal:
#     def sound(self):
#         print("Some sound")
#
# class Cat(Animal):
#     def sound(self):
#         print("Meow")
# c = Cat()
# c.sound()

###***If I create method on the same name and I not want Overriding Original Method ***###
# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         super().sound()    # call parent method
#         print("Dog barking")
# Dog().sound()

###***Multiple Inheritance***###
# class A:
#     def a(self):
#         print("A")
#
# class B:
#     def b(self):
#         print("B")
#
# class C(A, B):
#     pass

###***Multilevel Inheritance***###
# class A:
#     def a(self):
#         print("A")
#
# class B(A):
#     def b(self):
#         print("B")
#
# class C(B):
#     def c(self):
#         print("C")
# c = C()
# c.a()
# c.b()

#### Inheritance Example ###
# class Person:
#     species = "Human"
#
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print(f"My name is {self.name}")
#
#
# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name)    # call parent constructor
#         self.grade = grade
#
#     def info(self):               # override method
#         super().info()            # call parent method
#         print(f"My grade is {self.grade}")
# s = Student("Ali", "A")
# s.info()

###**** Polymorphism ****#### Same method name, different behavior
# class Dog:
#     def speak(self):
#         return "Woof!"
#
# class Cat:
#     def speak(self):
#         return "Meow!"
#
# class Cow:
#     def speak(self):
#         return "Moo!"
# animals = [Dog(), Cat(), Cow()]
# for a in animals:
#     print(a.speak())

####****Encapsulation ****######
####1- Public
# class Person:
#     def __init__(self, name):
#         self.name = name   # public attribute
#
# p = Person("Ahmed")
# print(p.name)

####2- Protected
# class Person:
#     def __init__(self, name, age):
#         self._age = age   # protected attribute
#
# p = Person("Ahmed", 30)
# print(p._age)   # allowed but NOT recommended

#####3- Private
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private attribute
# acc = BankAccount(1000)
# print(acc.__balance)   # ❌ Error

### You Can access Private Data Use Getter & Setter
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):      # getter
#         return self.__balance
#
#     def set_balance(self, amount):   # setter
#         if amount > 0:
#             self.__balance = amount
#         else:
#             print("Invalid amount")
#
# acc = BankAccount(1000)
# print(acc.get_balance())
#
# acc.set_balance(2000)
# print(acc.get_balance())

#####***** Property Decorator ****##### allows you to use methods like attributes.
# class Employee:
#     def __init__(self):
#         pass
#
#     @property
#     def say_hello(self):
#         return "Hello"
# a = Employee()
# print(a.say_hello)

####**** Abstract ***###You create a general blueprint (abstract class) that tells subclasses what to implement, but not how.
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#
#     @abstractmethod
#     def sound(self):
#         pass
# a = Animal()   # ❌ Error

#### Implementing the Abstract Class ###
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
#
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# d = Dog()
# print(d.sound())
#
# c = Cat()
# print(c.sound())























