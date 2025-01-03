# 1
# class student:
#     def __init__(self, name):
#         print("inside constructor")
#         self.name = name
#         print("all variable initiallized")
#     def show(self):
#         print("hello my name is",self.name)
# s1 = student("emma")
# s1.show()


# 2
# fp = open(r'E:\Internship Practice\Python-self-practice\sample-data.txt', 'r')
# print(fp.read())
# fp.close()


# 3
# try:
#     fp = open("sample-data.txt", "r")
#     print(fp.read())
#     fp.close()
# except FileNotFoundError:
#     print("please check the path")


# 4
# text = "this is a additional text"
# fp = open("sample-data.txt", "w")
# fp.write(text)
# print("done writing")
# fp.close()


# 5
# f = open("sample-data.txt","r")
# f.seek(0)
# print(f.read())


# 6
# f = open("sample-data.txt", "r")
# f.readline()
# print(f.tell())


# 7
# import os
# old_name = r"E:\Internship Practice\Python-self-practice\sample-data.txt"
# new_name = r"E:\Internship Practice\Python-self-practice\sample_data.txt"
# os.rename(old_name, new_name)


# 8
# fp = open("sales.txt", "x")
# fp.close()


# 9
# import os
# os.remove(r"E:\Internship Practice\Python-self-practice\sales.txt")


# 10
# f = open("sample_data.txt", "r")
# for x in f:
#     print(x)


# 11
# f = open("sample_data.txt", "r")
# print(f.readline())
# f.close()


# 12
# import os
# if os.path.exists("sample_data.txt"):
#     print("file is present")
# else:
#     print("file is not present")