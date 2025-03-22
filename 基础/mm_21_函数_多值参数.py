#  一般给多值参数命名时，习惯使用以下两个名字,也叫拆包
# *args -- 存放元组参数
# **kwargs -- 存放字典参数

def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, 6, name="小明", age=12)


def sum_numbers1(*args):
    """
    多值参数，和sum_numbers2比较一下哪个传参更简单
    @param args:
    @return:
    """
    num = 0
    print(args)
    # 循环遍历
    for n in args:
        num += n
    return num


def sum_numbers2(args):
    num = 0
    print(args)
    # 循环遍历
    for n in args:
        num += n
    return num


# 直接传多个参数
result = sum_numbers1(1, 2, 3, 4, 5)
print(result)
# 必须是传元组
args_tuple = (1, 2, 3, 4, 5)
result = sum_numbers2(args_tuple)
print(result)


def demo1(*args, **kwargs):
    """
    拆包例子
    @param args:
    @param kwargs:
    """
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# 这个会传入(gl_nums, gl_dict),{}这两个参数
demo1(gl_nums, gl_dict)

# 拆包语法，简化元组变量/字典变量的传递
demo1(*gl_nums, **gl_dict)

demo1(1, 2, 3, name="小明", age=18)
