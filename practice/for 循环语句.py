# text = "abcabcabc"
# count = 0
# for x in text:
#     if x == "a":
#         count +=1
# print(count)
#


# range 语句
# 语法1. ramge(5) 为01234
# 语法2. range(1,5)为1234
# 语法3. range(num1,num2,step) 如range(5,10,2) 为 5 7 9 加二输出且不包含num2

# count = 0
# for x in range(1,100):
#     if x % 2 ==0:
#         count +=1
# print(count)

#  for循环九九乘法表
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f"{y}*{x}={y*x}\t",end="")
#     print()


# money = 10000
# a = 0
# count = 0
# for x in range(1,21):
#     import random
#     num = random.randint(1, 10)
#     if num >=5:
#         a += 1000
#         count +=1
#         money -= 1000
#         print(f"员工{x}绩效分{num}工资1000还剩{money}元")
#     else:
#         print(f"员工{x}绩效分{num}不发工资")
#         continue
#     if count*1000 >=10000:
#         print("工资发完")
#         break
#

