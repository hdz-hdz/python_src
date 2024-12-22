# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}×{i}={i*j}", end="\t")
#     print()  # 换行



# 1到 100 求和
i = 1
sum = 0
while i<=100:
    sum = i+sum
    i+=1
print(sum)




# 猜随机数
import random
count = 0
num = random.randint(1, 100)
flag = True
while flag:
    a = int(input("输入数字"))
    if a == num:
        print("right")
        flag = False
    elif a > num:
        print("big")
    elif a < num:
        print("small")
    count += 1
print(count)

# 九九乘法表
i = 1
j = 1
while i <10:
    j = 1
    while  j <= i:
        print(f"{j}*{i} = {j*i}\t", end=" ")
        j += 1
    i +=1
    print()



