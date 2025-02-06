# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("apple is present in thislist")

# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "papaya", "pineapple"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# thislist = ["apple", "banana", "cherry"]
# for x in range(len(thislist)):
#     print(x)

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ['apple', 'banana', 'cherry']
# newlist = [x for x in fruits if x == 'banana']
# print(newlist)

# list1  = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
#     print(list1)

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# newlist = []
# for x in fruits:
#     newlist.append(x)
# print(newlist)

# thislist = ["apple", "banana", "cherry"]
# newlist = [x for x in thislist if "a" in x]
# print(newlist)

# thislist = ["apple", "banana", "cherry"]
# newlist = [x for x in thislist if x != "banana"]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunction(n):
#     return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunction)
# print(thislist)

# thisdict = {
#     "id1" : 1,
#     "id2" : 2,
#     "id3" : 3,
#     "id4" : 2
# }
# print(thisdict)

# thisdict = {
#     "id1" : 1,
#     "id2" : 2,
#     "id3" : 3,
#     "id2" : 4
# }
# print(thisdict)

# x = {'type' : 'fruit', 'name' : 'banana'}
# print(x['type'])

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
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])

# a = 10
# b = 12
# if a > b: print("a is greater than b")
# else : print("b is greater than a")

# a = 10
# b = 12
# print("a") if a > b else print("b")

# x = 12
# if x > 10 :
#     print("above 10")
#     if x > 20:
#         print("and also above 20")
#     else:
#         print("but not above 20")

# a = 330
# b = 329
# print("a") if a > b else print("=") if a == b else print("b")

# i = 1
# while i < 6:
#     print(i)
#     i += 1

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")

# fruits = ["apple","banana", "cherry"]
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2, 6):
#     print(x)

# for x in range(6):
#     print(x)
# else:
#     print("finished")

# for x in range(6):
#     if x == 3 : break
#     print(x)
# else:
#     print("finished")

# for x in range(6):
#     if x == 3 : continue
#     print(x)
# else:
#     print("finished")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#     for y in fruits:
#         print(x, y)

# def newfunc():
#     print("hello")
# newfunc()

# def myfunc(hmm):
#     print(hmm + " references")
# myfunc("email")
# myfunc("tobias")
# myfunc("linus")

# def my_function(*kids):
#   print("The youngest child is " + kids[1])
# my_function("Emil", "Tobias", "Linus");