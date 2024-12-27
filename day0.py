# x = "awesome"
# def myfunction():
#     print("python is " + x)
# myfunction()


# x = "awesome"
# def myfunction():
#     x = "fantastic"
#     print("python is " + x)
# myfunction()
# print("python is " + x)


# x = "awesome"
# def myfunction():
#     global x
#     x = "fantastic"
# myfunction()
# print("python is " + x)


# x = 5
# print("1", type(x))

# x = "Hello world"
# print("2", type(x))

# x = 5.5
# print("3", type(x))

# x = 1j
# print("4", type(x))

# x = ["apple", "banana"]
# print("5", type(x))

# x = ("apple", "banana")
# print("6", type(x))

# x = {"name" : "John", "age" : 36}
# print("7", type(x))

# x = {"apple", "banana"}
# print("8", type(x))

# x = frozenset({"apple", "banana"})
# print("9", type(x))

# x = True
# print("10", type(x))

# x = b"hello"
# print("11", type(x))

# x = bytearray(5)
# print("12", type(x))

# x = memoryview(bytearray(5))
# print("13", type(x))

# x = None
# print("14", type(x))


# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))


# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


# import random
# print(random.randrange(1, 10))


# for x in "banana":
#   print(x)


# txt = "The best things in life are free!"
# print(" hi " in txt)


# txt = "The best things in life are free!"
# print("expensive" not in txt)


# b = "Hello, World!"
# print(b[2:5])


# b = "Hello, World!"
# print(b[5:-2])


# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


# a = "Hello, World!"
# print(a.replace("H", "J"))


# age = 36
# txt = f"My name is John, I am {age} years old"
# print(txt)


# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)


# # thislist = ["apple", "banana", "cherry"]
# # thislist.remove("banana")
# # print(thislist)


# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# del thislist


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if x != "apple"]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in range(10)]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in range(10) if x < 5]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(newlist)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)


# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)


# def myfunc(n):
#   return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)


# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])


# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)


# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)


# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)


# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)


# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])


# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1


# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)


# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)


# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)


# thisset = {"apple", "banana", "cherry", False, True, 0}
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)


# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.intersection_update(set2)
# print(set1)


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# print(x)


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964,
# "color" : "white"
# }
# x = car.items()
# print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


# x = {'type' : 'fruit', 'name' : 'banana'}
# print(x['type'])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


# myfamily = {
#     "child1" : {"name" : "Emil", "year" : 2004},
#     "child2" : {"name" : "Tobias", "year" : 2007},
#     "child3" : {"name" : "Linus", "year" : 2011}}
# print(myfamily)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily)


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.setdefault("model", "Bronco")
# print(x)


# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")


# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")


# a = 200
# b = 33
# if a > b: print("a is greater than b")


# a = 2
# b = 330
# print("A") if a > b else print("B")


# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")


# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")


# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")


# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")


# x = 41
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")


# a = 33
# b = 200
# if b > a:
#   pass


# i = 1
# while i < 6:
#   print(i)
#   i += 1


# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


# fruits = ["apple", "banana", "cherry"]
# for x in "banana":
#   print(x)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)


# for x in range(6):
#   print(x)


# for x in range(2, 6):
#   print(x)


# for x in range(2, 30, 3):
#   print(x)


# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")


# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#   for y in fruits:
#     print(x, y)


# def my_function(fname):
#   print(fname + " Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(fname, lname):
#   print(fname + " " + lname)
# my_function("Emil", "Refsnes")


# def my_function(fname, lname):
#   print(fname + " " + lname)
# my_function("Emil") #If you try to call the function with 1 or 3 arguments, you will get an error


# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# def my_function(**kid):
#   print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(country = "Norway"):
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(food):
#   for x in food:
#     print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)


# def my_function(x):
#   return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# def my_function(x, /):
#   print(x)
# my_function(3)


# def my_function(x):
#   print(x)
# my_function(x = 3)


# def my_function(x, /):
#   print(x)
# my_function(x = 3)


# def my_function(*, x):
#   print(x)
# my_function(x = 3)


# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)
# my_function(5, 6, c = 7, d = 8)


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
# print("Recursion Example Results:")
# tri_recursion(3)


# def cal(n):
#     if(n == 0):
#         return 0
#     return cal(n-1) + n
# sum = cal(10)
# print(sum)


# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)
# fruits = ["mango","litchi", "apple", "banana"]
# print_list(fruits)


# x = lambda a : a + 10
# print(x(5))


# x = lambda a, b : a * b
# print(x(5, 6))


# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))


# def myfunc(n):
#   return lambda a : a * n
# mytripler = myfunc(3)
# print(mytripler(11))


# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))


# class MyClass:
#   x = 5
# print(MyClass)


# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name}({self.age})"
# p1 = Person("John", 36)
# print(p1)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("John", 36)
# p1.myfunc()


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
# p1 = Person("John", 36)
# p1.myfunc()


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
# p1 = Person("John", 36)
# p1.age = 40
# p1.myfunc()
# print(p1.age)


# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
# p1 = Person("John", 36)
# p1.myfunc()
# del p1
# print(p1)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# #Use the Person class to create an object, and then execute the printname method:
# x = Person("John", "Doe")
# x.printname()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   pass
# x = Student("Mike", "Olsen")
# x.printname()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
# x = Student("Mike", "Olsen")
# x.printname()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
# x = Student("Mike", "Olsen")
# x.printname()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
# x = Student("Mike", "Olsen")
# x.printname()


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019
# x = Student("Mike", "Olsen")
# print(x.graduationyear)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
# x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year
#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# x = Student("Mike", "Olsen", 2024)
# x.welcome()


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))


# mystr = "banana"
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# mytuple = ("apple", "banana", "cherry")
# for x in mytuple:
#   print(x)


# mystr = "banana"
# for x in mystr:
#   print(x)


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration
# myclass = MyNumbers()
# myiter = iter(myclass)
# # for x in myiter:
# #   print(x)


# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Drive!")
# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Sail!")
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Fly!")
# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object
# for x in (car1, boat1, plane1):
#   x.move()


# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def move(self):
#     print("Move!")
# class Car(Vehicle):
#   pass
# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")
# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")
# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object
# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()


# mystr = "banana"
# for x in mystr:
#   print(x)