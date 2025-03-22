# 返回多个值

def measure():
    """
    测量温度和湿度
    @return:
    """
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元组-可以包含多个数据，因此可以使用元组让函数一次返回多个值
    # 如果函数返回的类型是元组，小括号可以省略
    # return (temp, wetness)
    return temp, wetness


gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)
