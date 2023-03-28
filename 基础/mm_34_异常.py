def input_password():
    pwd = input("请输入一个不小于8位数的密码:")
    if len(pwd) < 8:
        ex = Exception("密码长度不够")
        # 主动抛出异常
        raise ex
    else:
        return pwd


def input_num():
    # 尝试输入一个字母，看看抛出什么错误
    num = int(input("请输入一个整数:"))
    print("您输入的整整数为：", end="")
    return num


try:
    print(input_password())
    print(input_num())
except Exception as result:
    print(result)
