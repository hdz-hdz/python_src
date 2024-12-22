# list列表
# 可存储不同类型的数据 支持嵌套

# # index
# list1 = [1,2,3,4,5]
# index = list1.index(2)
# print(index)
#
# # 语法：列表[下标] = 值
# # list1[2] = 2
# # print(list1)
#
# # insert方法
# # 语法: 列表.insert（下标，值）————在指定位置后面插入到指定位置
# list1.insert(1,6)
# print(list1)
#
# # 追加元素：列表.append(元素)————将指定元素追加到列表的尾部
# list1.append(7)
# print(list1)
#
# # extend  列表.extend()其他数据容器————将列表中的元素追加到列表的尾部
# list1.extend([8,9]) #也可放list
# print(list1)
#
# # 删除元素 ———— 语法1：del列表[下标]  语法2：列表.pop(下标)
# del list1[1]
# print(list1)
# list1.pop(2)
# print(list1)
#
# # 语法：列表.remove(元素) 删除某元素在列表中的第一个匹配项
# list1 = [1,1,2,3,4,5]
# list1.remove(1)
# print(list1)
#
# # # 清空列表 ————语法 ：列表.clear()
# # list1.clear()
# # print(list1)
#
# # 统计某元素在列表内的数量————语法：列表.count(元素)
# list1 = [1,1,2,3,4,5]
# print(list1.count(1))
#
# # 统计列表中全部的元素数量————语法：len(列表)
# list1 = [1,1,2,3,4,5]
# print(len(list1))

# 遍历：将容器内的元素依次取出并处理
# 列表的遍历——while循环(可无限循环)
# def list_while_fun():
#     list1 = [1,2,3,4,5]
#     index = 0
#     while index < len(list1):
#         element = list1[index]
#         print(f"列表的元素：{element}")
#         index +=1
#
# # 列表的遍历——for循环(不可无限循环)
# def list_for_fun():
#     list1 = [1,2,3,4,5]
#     for element in list1:
#         print(f"列表的元素：{element}")
#
# list_while_fun()
# list_for_fun()


# 案例：
list_1 = [1,2,3,4,5,6,7,8,9,10]
"""
遍历list_1中的元素，将偶数添加到新的列表double_list中，并打印出来。
"""# 初始化一个空列表，用于后续存储偶数元素
double_list = []

def list_for_fun():
    """
    遍历list_1中的每个元素，将偶数元素添加到double_list中。
    该函数不接受参数，也没有返回值。它通过全局变量double_list来存储找到的偶数元素，
    并在完成遍历后打印出这些偶数元素。
    """
    for element in list_1:
        # 检查元素是否为偶数
        if element % 2 == 0:
            # 如果是偶数，则添加到double_list中
            double_list.append(element)
    # 打印收集到的偶数列表
    print(f"偶数：{double_list}")
def list_while_fun():
    """
    遍历list_1中的元素，将偶数添加到新的列表double_list中，并打印出来。
    """
    # 初始化一个空列表，用于存储偶数
    double_list = []
    # 初始化索引变量，用于遍历list_1
    index = 0
    # 使用while循环遍历list_1
    while index < len(list_1):
        # 获取当前索引对应的元素
        element = list_1[index]
        # 检查元素是否为偶数
        if element % 2 == 0:
            # 如果是偶数，则添加到double_list中
            double_list.append(element)
        # 索引递增，以继续遍历下一个元素
        index += 1
    # 打印出所有偶数
    print(f"偶数：{double_list}")



list_for_fun()
list_while_fun()