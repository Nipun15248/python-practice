# 1
# num = int(input("Enter the number : "))
# if num % 7 == 0:
#     print("Hello")
# else:
#     print("bye")


# 2
# elec_bill = int(input("Please enter the units consumed: "))
# if elec_bill <= 0 and elec_bill <= 100 :
#     elec_bill *= 0
#     print(elec_bill,"Rs")
#     print("No Charges")
# elif elec_bill > 100 and elec_bill <= 200 :
#     elec_bill = elec_bill * 5
#     print(elec_bill,"Rs")
#     print("Rs 5 per unit")
# elif elec_bill > 200 :
#     elec_bill = elec_bill * 10
#     print(elec_bill,"Rs")
#     print("Rs 10 per unit")

# 2
# elec_unit = int(input("Please enter the units : "))
# elec_bill = 0
# if elec_unit > 0:
#     elec_unit = elec_unit - 100
#     if elec_unit < 100:
#         elec_bill = elec_bill + elec_unit * 5
#     else:
#         elec_bill = elec_bill + 100 * 5
#     elec_unit = elec_unit - 100
#     if elec_unit > 0:
#         elec_bill = elec_bill + elec_unit * 10
# print("your electricity bill is :", elec_bill, "Rs")

# 2
# amt = O
# nu = int(input("Enter number of electric unit"))
# if nu <= 100:
#     amt = O
# if nu>100 and nu <= 200:
#     amt = (nu - 100) * 5
# if nu > 200:
#     amt = 500 + (nu - 200) * 10
# print("Amount to pay :",amt)


# 3
# num = 1234124124124
# print(num % 10)


# 4
# num = int(input("enter the number : "))
# id = num % 10
# if id % 3 == 0:
#     print("the last number is divisible by 3")
# else:
#     print("the last number is not divisible by 3")


# 5
# num = int(input("enter the number : "))
# for i in range (1, 11):
#     print(num, " * ", i, " = ", num * i)


# 6
# fact = 1
# num = int(input("enter the number : "))
# for i in range (num, 1, -1):
#     fact *= i
# print(fact)


# 7
# num = int(input("enter the first number : "))
# sum = 0
# while(num):
#     r = num % 10
#     sum += r
#     num = num // 10
# print(sum)


# 8
# for i in range (1, 5):
#     for j in range (1, i + 1):
#         print(j, end = " ")
#     print()


# 9
# for i in range (4, 0, -1):
#     for j in range (i):
#         print("*", end = " ")
#     print()

# s = '2'
# ans = ""
# for i in range(1,int(input("Enter number of terms: "))+1):
#     ans += ',' + s*i
# ans = ans.replace(',','',1)
# print(ans)

# s = '2'
# sm = 0
# for i in range(1,int(input("Enter number of terms: "))+1):
#     print(s*i)
#     sm += int(s*i)
# print(sm)