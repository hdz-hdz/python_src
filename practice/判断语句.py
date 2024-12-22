"""
age = int(input("请输入年龄"))
if age >= 18:
    print("已成年")
print("游戏愉快")
"""

#
# print("欢迎")
# height = int(input("请输入身高"))
# if height>=120:
#     print("买票")
# else:
#     print("免费")
# print("happy")



import random
num = random.randint(1,10)
a = int(input("输入数字"))
if a == num:
    print("right")
else :
    if a > num:
        print("big")
    else :
        print("small")

a = int(input("再次输入数字"))
if a == num:
    print("right")
else :
    if a > num:
        print("big")
    else :
        print("small")

a = int(input("第三次输入数字"))
if a == num:
    print("right")
else :
    print("人机")
