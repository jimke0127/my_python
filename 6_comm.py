# 数字型之间可以直接计算
# 计算时布尔类型True=1 False=0
a = 8
b = 7
c = True
d = False
money = a + b + c + d
print(money)

# 字符串之间用 + 连接
first_name = "zhang"
last_name = "san"
full_name = first_name + last_name
print(full_name)

# 字符串变量可以和整数使用*重复拼接相同的字符串
face = "-_-"
# 输出10个笑脸
print(face * 10)

# 特别注意，字符串不能和数字类型做相加运算，
# 以下操作会出错
# print(first_name + a)
print(first_name + str(a))


