# 函数的命名跟变量一样
# 函数要先定义，才能调用，不能反过来
# 注意：函数后面需要空两行

def say_hello():
    """打招呼"""
    print("hello 1")


def sum_num(num1, num2):
    """
    对两个数字的求和
    :param num1: 数字1
    :param num2: 数字2
    :return:
    """
    return num1 + num2


say_hello()
s = sum_num(1, 5)
print(s)
