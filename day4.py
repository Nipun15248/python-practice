# 1
# def sum():
#     num1 = int(input("enter the first number : "))
#     num2 = int(input("enter the second number : "))
#     sumofnum = num1 + num2
#     print(sumofnum)
# sum()


# 2
# def areaofrect():
#     l = int(input("eneter the length of the rectangle : "))
#     b = int(input("eneter the breadth of the rectangle : "))
#     a = l * b
#     print("the area of the rectangle is", a, "square units")
# areaofrect()


# 3
# def square(num):
#     print("sq of the number is :", num * num)
# n = int(input("enter the number : "))
# square(n)


# 4
# def word(words):
#     c = 0
#     l = words.split()
#     for i in l:
#         c += 1
#     print("total no of words :", c)
# str1 = input("enter any string : ")
# word(str1)


# 5
# def listsum(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     print(sum)
# l = [3, 2, 8, 5, 4]
# listsum(l)


# 6
# def factorial(num):
#     if num == 0:
#         print("factorial is : 1")
#     else:
#         fact = 1
#         for i in range (num, 0, -1):
#             fact *= i
#         print("factorial of a number is :", fact)
# n = int(input("enter the for factorial : "))
# factorial(n)


# 7
# def fullname(first_name, last_name):
#     Fullname = first_name + " " + last_name
#     print(Fullname)
# FirstName = str(input("Please enter your first name : "))
# LastName = str(input("Please enter your last name : "))
# fullname(FirstName, LastName)


# 8
# def avg(a, b, c = 9):
#     average = (a + b + c) / 3
#     print(average)
# avg(6, 7, 8)
# avg(6, 7)


# 9
# def pow(b, e):
#     res = 1
#     for i in range (1, e + 1):
#         res *= b
#     return res
# base = int(input("enter the base value : "))
# exp = int(input("enter the exponent : "))
# ans = pow(base, exp)
# print("result is :", ans)


# 10
# def vol(l, b, h):
#     volume = l * b * h
#     return volume
# L = int(input("enter the length of cuboid : "))
# B = int(input("enter the breadth of cuboid : "))
# H = int(input("enter the height of cuboid : "))
# result = vol(L, B, H)
# print("volume of cuboid is :", result)


# 11
# class employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def show(self):
#         print(self.name, self.age, self.salary)

# emma = employee("emma", 23, 7500)
# emma.show()

# kelly = employee("kelly", 25, 8500)
# kelly.show()


# 12
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name, self.age)
# emma = student("emma", 12)
# emma.show()
# kelly = student("kelly", 13)
# kelly.show()


# 13
# class vehicle:
#     def __init__(self, engine):
#         print("Inside vehicle constructor")
#         self.engine = engine

# class car(vehicle):
#     def __init__(self, engine, max_speed):
#         super().__init__(engine)
#         print("inside car constructor")
#         self.max_speed = max_speed

# class electric_car(car):
#     def __init__(self, engine, max_speed, km_range):
#         super().__init__(engine, max_speed)
#         print("Inside Electric car constructor")
#         self.km_range = km_range

# ev = electric_car("1500cc", 240, 750)
# print(f'engine={ev.engine}, max_speed={ev.max_speed}, km_range={ev.km_range}')


# 14
# class employee:
#     count = 0
#     def __init__(self):
#         employee.count += 1
# e1 = employee()
# e2 = employee()
# e3 = employee()
# print("the no of employee : ", employee.count)


# 15
# class person:
#     def __init__(self, name, sex, profession):
#         self.name = name
#         self.sex = sex
#         self.profession = profession

#     def show(self):
#         print(f'Name:{self.name}, sex:{self.sex}, profession:{self.profession}')
    
#     def work(self):
#         print(f'{self.name} is working as a, {self.profession}')

# jessa = person("jessa", "female", "sde")

# jessa.show()
# jessa.work()


# 17
# class student:
#     school_name = "abc school"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# s1 = student("harry", 12)
# print("student:", s1.name, s1.age)
# print("school name:", student.school_name)

# s1.name = "jessa"
# s1.age = 14
# print("student:", s1.name, s1.age)

# student.school_name = "def school"
# print("student:", student.school_name)