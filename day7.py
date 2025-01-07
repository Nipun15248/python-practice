# 1
# type error
# x = 5
# y = "hello"
# z = x + y

# 2
# x = 5
# y = "hello"
# try:
#     z = x + y
# except TypeError:
#     print("error : cannot add an int and a str")

# 3
# try and except statement - catching exceptions
# a = [1, 2, 3]
# try:
#     print("Second element = %d" %(a[1]))
#     print("fourth element = %d" %(a[3]))
# except:
#     print("an error occurred")

# 4
# catching specific exception
# def fun(a):
#     if a < 4:
#         b = a/(a-3)
#     print("value of b =", b)
# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("ZeroDivisionError occured and handled")
# except NameError:
#     print("NameError occured and handled")

# 5
# try with else clause
# def abyB(a, b):
#     try:
#         c = ((a + b) / (a - b))
#     except ZeroDivisionError:
#         print("a/b result in 0")
#     else:
#         print(c)
# abyB(2.0, 3.0)
# abyB(3.0, 3.0)

# 6
# Finally keyword in python
# try:
#     k = 5 // 0
#     print(k)
# except ZeroDivisionError:
#     print("can't divide by zero")
# finally:
#     print("this is always executed")

# 7
# raising exception
# try:
#     raise NameError("hi there")
# except NameError:
#     print("an exception")
#     raise

# 8
# user defined exceptions in python with examples
# class myerror(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return(repr(self.value))
# try:
#     raise(myerror(3*2))
# except myerror as error:
#     print("a new exception occured :", error.value)

# 9
# user defined class with multiple inheritance
# class error(Exception):
#     pass
# class zerodivision(error):
#     pass
# try:
#     i_num = int(input("enter a number : "))
#     if i_num == 0:
#         raise zerodivision
# except zerodivision:
#     print("input value is zero, try again")
#     print()

# 10
# deriving error from super class exception
# class Error(Exception):
#     pass
# class TransitionError(Error):
#     def __init__(self,perv, nex, msg):
#         self.perv = perv
#         self.next = nex
#         self.msg = msg
# try:
#     raise(TransitionError(2, 3 * 2, "Not Allowed"))
# except TransitionError as error:
#     print("exception occured : ", error.msg)

# 11
# how to use standard exception as a base class
# class Networkerror(RuntimeError):
#     def __init__(self, arg):
#         self.args = arg
# try:
#     raise Networkerror("Error")
# except Networkerror as e:
#     print(e.args)


# Constructors

# 12
# class ClassName:
#     def __new__(cls, parameters):
#         instance = super(ClassName, cls).__new__(cls)
#         return instance

# 13
# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = value


# 14
# a = 10
# b = 0
# c = a / b
# print("a / b =", c)

# 14
# try:
#     a = 10
#     b = 0
#     c = a / b
#     print("a / b =", c)
# except:
#     print("can't divide the number by zero. please provide different number")


# 15
# try:
#     a = int(input("enter value of a : "))
#     b = int(input("enter value of b : "))
#     c = a / b
#     print("the answer of a divide by b :",c)
# except ValueError:
#     print("enter value is wrong")
# except ZeroDivisionError:
#     print("can't divide by zero")


# 16
# try:
#     a = int(input("enter value of a : "))
#     b = int(input("enter the value of b : "))
#     c = a / b
#     print("the answer of a divide by b :",c)
# except(ValueError, ZeroDivisionError):
#     print("enter a valid number")


# 17
# try:
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     c = a / b
#     print("The answer of a divide by b:", c)

# except ZeroDivisionError:
#     print("Can't divide with zero")
# finally:
#     print("Inside a finally block")


# 18
# try:
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     c = a / b
#     print("The answer of a divide by b:", c)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# else:
#     print("We are in else block ")


# 19
# def simple_interest(amount, year, rate):
#     try:
#         if rate >+ 100:
#             raise ValueError(rate)
#         interest = (amount * year * rate) / 100
#         print("the simple interest is :", interest)
#         return interest
#     except ValueError:
#         print("rate should be less than 100")
# print("case 1")
# simple_interest(800, 6, 8)
# print("case 2")
# simple_interest(800, 6, 120)


# 20
# try:
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     c = a/b
#     print("The answer of a divide by b:", c)
# except ZeroDivisionError as e:
#     raise ValueError("Division failed") from e


# 21
# class Error(Exception):
#     """Base class for other exceptions"""
#     pass
# class ValueTooSmallError(Error):
#     """Raised when the input value is small"""
#     pass
# class ValueTooLargeError(Error):
#     """Raised when the input value is large"""
#     pass
# while(True):
#     try:
#         num = int(input("Enter any value in 10 to 50 range: "))
#         if num < 10:
#             raise ValueTooSmallError
#         elif num > 50:
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError:
#             print("Value is below range..try again")

#     except ValueTooLargeError:
#             print("value out of range...try again")

# print("Great! value in correct range.")


# 22
# class NegativeAgeError(Exception):
#     def __init__(self, age, ):
#         message = "Age should not be negative"
#         self.age = age
#         self.message = message
# age = int(input("Enter age: "))
# if age < 0:
#     raise NegativeAgeError(age)


# 23
# def sum_of_list(numbers):
#     return sum(numbers)
# def average(sum, n):
#     # ZeroDivisionError if list is empty
#     return sum / n
# def final_data(data):
#     for item in data:
#         print("Average:", average(sum_of_list(item), len(item)))
# list1 = [10, 20, 30, 40, 50]
# list2 = [100, 200, 300, 400, 500]
# # empty list
# list3 = []
# lists = [list1, list2, list3]
# final_data(lists)