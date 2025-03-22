# 在函数内部，针对参数使用赋值语句，不会修改到外部的实参变量

def test(str1):
    str1 = "我改变了"
    print(str1)


def test_list1(str_list1):
    # 使用列表内部方法改变列表，外部列表(可变类型的数据列表、字典)也会改变
    str_list1.append("hello")

    # 列表变量使用 += 本质上是在调用列表的 extend 方法
    str_list1 += str_list1
    # str_list1.extend(str_list1)


def test_list2(str_list2):
    # 对列表重新赋值，外部列表(可变类型的数据列表、字典)不会改变
    str_list2 = ["1", "2", "3"]
    return str_list2


a = "你好"
test(a)
# a的值没有改变
print(a)

str_list = ["a", "b", "c"]
print("调用函数前列表的值：", end="")
print(str_list)
test_list1(str_list)
print("调用函数后列表的值变了：", end="")
print(str_list)

str_list2 = ["a", "b", "c"]
print("调用函数前列表的值：", end="")
print(str_list2)
test_list2(str_list2)
print("调用函数后列表的值不变：", end="")
print(str_list2)
