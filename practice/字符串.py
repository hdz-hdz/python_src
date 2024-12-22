name = "hdz"
message = " %s是帅哥 " % name
print(message)

age = 20
name2 = "hdz"
print( "我叫%s今年%d岁" % (name2,age))
"""
%s 为字符串拼接
%d 为整数型拼接
%f 为浮点型拼接

字符串格式化-数字精度控制
我们可以使用辅助符号"m.n”来控制数据的宽度和精度
· m，控制宽度，要求是数字(很少使用)，设置的宽度小于数字自身，不生效
•.n，控制小数点精度，要求是数字，会进行小数的四舍五入
示例：
%5d：表示将整数的宽度控制在5位，如数字11，被设置为5d，就会变成：[空格][空格][空格]11，用三个空格补足宽度。

%5.2f：表示将宽度控制为5，将小数点精度设置为2

  小数点和小数部分也算入宽度计算。
如，对11.345设置了%7.2f后，结果是：[空格][空格]111.35。2个空格补足宽度，小数部分限制2位精度后，四舍五入为.35

%.2f：表示不限制宽度，只设置小数点精度为2，如11.345设置%.2f后，结果是11.35
11.345设置 %.2f之后结果为11.35
"""
name = "hdz"
age = 20
# f：format 占位使用{变量}来占位
print(f"我是{name} 今年{age}")
#占位前必须有f


#表达式的格式化
print("1*1")
print("1*2")


