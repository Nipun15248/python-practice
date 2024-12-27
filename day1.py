# 1
# age = input("enter your age : ")
# age = int(age)
# if age >= 18:
#     print("you are elegible to vote")
# else:
#     print("you are not elegible to vote")


# 2
# num1 = 30
# num2 = 20
# if num1 > num2:
#     diff = num1 - num2
#     print("diff of num1 and num2 is", diff, "and num1 is greater than num2")
# elif num1 == num2:
#     diff = num1 - num2
#     print("diff of num1 and num2 is", diff, "because they are equal")
# else :
#     diff = num2 - num1
#     print("diff of num1 and num2 is", diff, "and num2 is greater than num1")


# 3
# num = -1
# if num > 0:
#     print("number is positive")
# elif num == 0:
#     print("number is zero")
# else :
#     print("number is negative")


# 4
# signal = "GrEen"
# if signal == "red" or signal == "Red" or signal == "RED":
#     print("Stop")
# elif signal == "yellow" or signal == "Yellow" or signal == "YELLOW":
#     print("slow")
# elif signal == "green" or signal == "Green" or signal == "GREEN":
#     print("Keep going")
# else :
#     print("please write the correct color and in correct format that is either in lower case or upper case or in camel case")


# 5
# num1 = float(input("enter the first number : "))
# num2 = float(input("enter the second number : "))
# op = input("enter the operator (+ , - , * , /) here : ")
# if op == "+":
#     result = num1 + num2
#     print("result is", result)
# elif op == "-":
#     result = num1 - num2
#     print("result is", result)
# elif op == "*":
#     result = num1 * num2
#     print("result is", result)
# elif op == "/":
#     if num2 == 0:
#         print("you can't divide by zero")
#     else :
#         result = num1 / num2
#         print("result is", result)


# 6
# for x in "PYTHON":
#     print(x)


# 7
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in numbers:
#     print(x)


# 8
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in numbers:
#     if x % 2 == 0:
#         print(x, "even no")
#     else:
#         print(x, "odd no")


# 9
# for num in range(11):
#     if num > 0:
#         print(num * 10)


# 10
# for x in range(1, 11):
#     print(x)


# 11
# for x in range(1, 21):
#     if x % 2 == 0:
#         print(x)


# 12
# for x in range(10, 0, -1):
#     print(x)


# 13
# sum = 0
# for x in range(0, 51):
#     sum += x
#     print(sum)


# 14
# mul = 5
# for x in range(1, 11):
#     # print(mul * x)
#     print(f"{mul} * {x} = {mul*x}")


# 15
# for x in range(1, 51, 3):
#     if x == 3:
#         x = 0
#         continue
#     else:
#         print(x)

# 15
# # Initialize a counter for skipping
# skip_count = 0

# # Loop through numbers from 1 to 50
# for i in range(1, 51):
#     # Increment the skip counter
#     skip_count += 1

#     # If skip counter is 3, reset it and skip this iteration
#     if skip_count == 3:
#         skip_count = 0
#         continue

#     # Print the number
#     print(i, end=" ")


# 16
# for x in range(1, 11):
#     print(x ** 2)


# 17
# sum = 0
# for x in range(1, 51):
#     if x % 2 == 0:
#         continue
#     sum += x
# print(sum)

# 17
# li = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
# sum = 0
# for i in range(0, len(li), 2):
#     sum += li[i]
#     print(li[i])
# print(sum)


# 18
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()


# 19
# sum = 0
# for i in range(1, 31):
#     if i % 3 != 0:
#         continue
#     sum += i
#     print(sum)

# 19
# sum=0
# for i in range(1, 31):
#     if i % 3 == 0:
#         sum += i
# print(sum)


# 20
# for num in range(1, 51):
#     if num > 1:  # Prime numbers are greater than 1
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of the number
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)

#20
# for i in range(1, 51):
#     if i > 1:
#         prime = True
#         for j in range(2, i + 1):
#             if i % j == 0:
#                 prime =False
#                 break
#             if prime:
#                 print(i)
