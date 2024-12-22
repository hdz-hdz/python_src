# def 函数名(传入参数):
#     函数体
#     return 函数返回值



# def add(a,b):
#     """
#     :param a: 形参x表示相乘的一个数字
#     :param b: 形参y表示相乘的一个数字
#     :return: 两束相乘的结果
#     """
#     result = a*b
#     print(f"{a}*{b}={a*b}")
# add(99,99)


# def add(a):
#     if a > 37:
#         print(f"体温为{a}°C，属于高危人群")
#     else:
#         print(f"体温为{a}°C，属于低危人群")
# add(39)


# 函数嵌套调用
# 简单省略


# 局部变量和全局变量
# 在函数外局部变量无法使用
# global 关键字
# global 关键字可以在函数中将局部变量修改成全局变量
# num = 200
# def testa():
#     print(f"testa:{num}")
#
# def testb():
#     global  num
#     num = 500
#     print(f"testb:{num}")
#
# testa()
# testb()
# print(num)

# 综合案例
money = 5000000
name = input("请输入姓名")
def check():
    print(f"{name}的余额为{money}")

def get():
    global money
    x = int(input("请输入取款金额"))
    money -= x
    return money


def put():
    global money
    y = int(input("请输入存款金额"))
    money += y
    return money


while True:
    num = input("查询money输入1\n存款按2\n取款按3\n退出按4\n")
    if num == "1":
        check()
        continue
    elif num =="2":
        put()
        print(f"存款成功\n还有{money}元")
        continue
    elif num =="3":
        get()
        print(f"取款成功\n还有{money}元")
        continue
    else:
        break
