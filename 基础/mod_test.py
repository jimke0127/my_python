name = "模块测试"


def test_mod():
    print("测试模块的函数")


# 如果这个文件被导入时，下面的代码不会被执行
if __name__ == "__main__":
    print("只有直接执行该，这里才会被执行")
    print(name)
    test_mod()
