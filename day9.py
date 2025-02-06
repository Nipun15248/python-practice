# ****************functions****************


# def myfunction():
#     print("hello")
# myfunction()

# def myfunction(fname):
#     print("hello " + fname)
# myfunction("Nipun")

# def myfunction(fname, lname):
#     print(fname + " " + lname)
# myfunction("Nipun", "Tiwari")

# def myfunction(*kids):
#     print("The youngest kid is", kids[1])
# myfunction("rohan", "sohan", "mohan")

# def myfunction(child1, child2, child3):
#     print("the youngest child is", child3)
# myfunction(child1 = "Rohan", child2 = "Sohan", child3 = "Mohan")

# def myfunction(**kids):
#     print("his last name is " + kids["lname"])
# myfunction(fname = "Rohan", lname = "Kuch to hai")

# def myfunction(country = "Norway"):
#     print("t am from " + countr]y)
# myfunction("Sweden")

# def myfunction(food):
#     for x in food:
#         print(x)
# fruits = ["apple", "banana", "cherry"]
# myfunction(fruits)

# def myfunction(x):
#     return x * 5
# print(myfunction(3))

# def myfucntion(x, /):
#     print(x)
# myfucntion(3)

# def myfunction(*, x):
#     print(x)
# myfunction(x = 3)

# def myfunction(a, b, /, *, c, d):
#     print(a + b + c + d)
# myfunction(5, 6, c = 7, d = 8)

# def trirecursion(k):
#     if (k > 0):
#         result = k + trirecursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
# print("recursion results : ")
# trirecursion(6)



# ****************Lambda****************


# x = lambda a, b : a * b
# print(x(5, 6))

# def myfunction(n):
#     return lambda a : a * n
# mydoubler = myfunction(2)
# print(mydoubler(10))



# ****************Arrays****************


# cars = ["Ford", "Volvo", "BMW"]
# for x in cars:
#     print(x)

# cars.append("Honda")
# print(cars)

# cars.pop(-1)
# print(cars)

# cars.remove("Ford")
# print(cars)



# ****************Classes & Object****************


# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = person("john", 36)
# print(p1.name)
# print(p1.age)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} ({self.age})"
# p1 = person("john", 36)
# print(p1)

# lass person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunction(self):
#         print("hello my name is " + self.name)
# p1 = person("john", 36)
# p1.myfunction()

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunction(abc):
#         print("hello my name is " + abc.name + " and my age is " + str(abc.age))
# p1 = person("john",36)
# p1.myfunction()

# p1.age = 40
# p1.myfunction()

# del p1
# p1.myfunction()



# ****************Inheritance****************


# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)
        
# x = person("john", "doe")
# x.printname()

# class student(person):
#     def __init__(self, fname, lname):
#         person.__init__(self, fname, lname)
#         super().__init__(fname, lname)

# x = student("mike", "olsen")
# x.printname()

# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)
# class student(person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
# x = student("mike", "olsen", 2024)
# print(x.graduationyear)

# class student(person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
#     def welcome(self):
#         print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# x = student("mike", "olsen", 2024)
# x.welcome()



# ****************Iterators****************


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class mynumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x
# myclass = mynumber()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class mynumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# myclass = mynumber()
# myiter = iter(myclass)
# for x in myiter:
#     print(x)



# ****************Polymorphism****************


# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("drive")
# class boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("sail")
# class plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("fly")
# car1 = car("ford", "mustang")
# boat1 = boat("yacht", "sailor")
# plane1 = plane("boeing", "747")
# for x in (car1 , boat1, plane1):
#     x.move()

# class vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("move")
# class car(vehicle):
#     pass
# class boat(vehicle):
#     def move(self):
#         print("sail")
# class plane(vehicle):
#     def move(self):
#         print("fly")
# car1 = car("ford", "mustang")
# boat1 = boat("yacht", "sailor")
# plane1 = plane("boeing", "747")
# for x in (car1, boat1, plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()