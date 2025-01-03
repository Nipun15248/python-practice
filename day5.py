# 1
# class vehicle:
#     def vehicle_info(self):
#         print("inside vehicle class")

# class car(vehicle):
#     def car_info(self):
#         print("inside car class")

# car = car()

# car.vehicle_info()
# car.car_info()


# 2
# class person:
#     def person_info(self, name, age):
#         print("def person_info function")
#         print(f'Name: {name}, Age: {age}')

# class company:
#     def company_info(self, company_name, location):
#         print("def company_info function")
#         print(f'Company: {company_name}, Location: {location}')

# class employee(person, company):
#     def employee_info(self, salary, skills):
#         print("def employee_info function")
#         print(f'Salary: {salary}, Skills: {skills}')

# emp = employee()
# emp.person_info('jessa', 28)
# emp.company_info('google', 'Atlanta')
# emp.employee_info(12000, 'Machine Learning')


# 3
# class vehicle:
#     def info(self):
#         print("this is vehicle class")

# class car (vehicle):
#     def car_info(self, name):
#         print("car name is", name)

# class truck(vehicle):
#     def truck_info(self, name):
#         print("truck name is", name)

# obj1 = car()
# obj1.info()
# obj1.car_info("Rolls Roys")

# obj2 = truck()
# obj2.info()
# obj2.truck_info("Tata")


# 4
# class vehicle:
#     def vehicle_info(self):
#         print("Inside vehicle class")

# class car(vehicle):
#     def car_info(self):
#         print("inside car class")

# class truck(vehicle):
#     def truck_info(self):
#         print("inside truck class")

# class sportscar(car, vehicle):
#     def sports_car_info(self):
#         print("inside sports car class")

# s_car = sportscar()

# s_car.vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()


# 5
# class company:
#     def company_name(self):
#         return "google"
    
# class employee(company):
#     def info(self):
#         c_name = super().company_name()
#         print("jessa works at", c_name)

# emp = employee()
# emp.info()


# 6
# class company:
#     def fun1(self):
#         print("inside parent class")

# class employee(company):
#     def fun2(self):
#         print("inside child class")

# class player:
#     def fun3(self):
#         print("inside player class")

# print(issubclass(employee, company))

# print(issubclass(employee, list))

# print(issubclass(player, company))

# print(issubclass(employee, (list, company)))

# print(issubclass(company, (list, company)))


# 7
# class vehicle:
#     def max_speed(self):
#         print("max speed is 100 km/hr")
    
# class car(vehicle):
#     def max_speed(self):
#         print("max speed is 200 km/hr")

# car = car()
# car.max_speed()


# 8
# student = ["emma", "jessa", "kelly"]
# school = "abc school"
# print(len(student))
# print(len(school))


# 9
# s = "ANSHIKA"
# str = s.replace("ANSHIKA", "ANSHIKZ")
# print(str)


# 10
# class vehicle:
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price

#     def show(self):
#         print(f'details : {self.name}, {self.color}, {self.price}')

#     def max_speed(self):
#         print("vehicle's max speed is 150")

#     def change_gear(self):
#         print("vehicle change 6 gear")

# class car(vehicle):
#     def max_speed(self):
#         print("car's max speed is 240")
    
#     def change_gear(self):
#         print("car change 7 gear")

# car = car("car x1", "red", 20000)
# car.show()
# car.max_speed()
# car.change_gear()

# vehicle = vehicle("truck x1", "white", 75000)
# vehicle.show()
# vehicle.max_speed()
# vehicle.change_gear()


# 11
# class shopping:
#     def __init__(self, basket, buyer):
#         self.basket = list(basket)
#         self.buyer = buyer
#     def __len__(self):
#         print("redefine lenght")
#         count = len(self.basket)
#         return count * 2
# shopping = shopping(["shoes", "dress", "watch"], "jessa")
# print(len(shopping))


# 12
# class ferrari:
#     def fuel_type(self):
#         print("petrol")
#     def max_speed(self):
#         print("max speed 350")
# class bmw:
#     def fuel_type(self):
#         print("diesel")
#     def max_speed(self):
#         print("max speed 240")
# ferrari = ferrari()
# bmw = bmw()
# for car in (ferrari, bmw):
#     car.fuel_type()
#     car.max_speed()


# 13
# class ferrari:
#     def fuel_type(self):
#         print("petrol")
#     def max_speed(self):
#         print("max speed 350")
# class bmw:
#     def fuel_type(self):
#         print("diesel")
#     def max_speed(self):
#         print("max speed 240")
# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()
# ferrari = ferrari()
# bmw = bmw()
# car_details(ferrari)
# car_details(bmw)


# 14
# student = ["emma", "jessa", "kelly"]
# school = "abc school"
# print("Reversed string")
# for i in reversed("Nipun Tiwari"):
#     print(i, end = " ")
# print("\nReverse list")
# for i in reversed(["emma", "jessa", "kelly"]):
#     print(i, end = " ")


# 15
# def addition(a, b):
#     c = a + b
#     print(c)
# def addition(a, b, c):
#     d = a + b + c
#     print(d)
# print("addition using a and b")
# addition(3, 7, 5)
# print("addition using a, b and c")
# addition(3, 7)


# 16
# for i in range(5): print(i, end = ", ")
# print()
# for i in range(5, 10): print(i, end = ", ")
# print()
# for i in range(2, 12, 2): print(i, end =", ")


# 17
# class shape:
#     def area(self, a, b = 0):
#         if b > 0:
#             print("Area of rectange is : ", a * b)
#         else:
#             print("Area of spuare is : ", a ** 2)
# square = shape()
# square.area(5)
# rectangle = shape()
# rectangle.area(5,3)


# # 18
# print(100 + 200)
# print("jessa" + "roy")
# print([10, 20, 30] + ["jessa", "emma", "kelly"])


# 19
# class book:
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self, other):
#         return self.pages + other.pages
# b1 = book(400)
# b2 = book(300)
# print("total number of pages :", b1 + b2)


# 20
# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def __mul__(self, timesheet):
#         print("worked for", timesheet.days, "days")
#         return self.salary * timesheet.days
# class Timesheet:
#     def __init__(self, name, days):
#         self.name = name
#         self.days = days
# emp = employee("jessa", 800)
# timesheet = Timesheet("jessa", 50)
# print("salary is :", emp * timesheet)