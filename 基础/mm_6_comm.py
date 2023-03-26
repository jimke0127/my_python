# 格式化快捷键 ctrl+alt+l
# 未开发或带后续再开发的地方，用# TODO 注释
# 对代码中的同一个变量改名时，建议先双击该变量，再使用右键Refactor->Rename
# 如果需要在系统终端执行某文件，执行以下操作
# 1、在该文件头部加入python3的位置(which python3)
# 2、该文件增加执行的操作(sudo chmod +x 文件名)

# 变量只能由字母、下划线和数字组成，且不能以数字开头、不能与关键字重名
# 变量命名规则：
# 使用小写字母，单词与单词之间使用_连接，如first_name
# 或者使用驼峰命名法（又分大驼峰FirstName，小驼峰firstname，不推荐）
# 变量和数据是分开存储的，数据保存在内存中的一个位置，变量保存着数据在内存中的地址
# 变量中记录数据的地址，就叫做引用，使用id() 可以查询变量中保存数据的地址

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

# 类型转换，input输入的都是字符串
# 转成浮点数
price = float(input("请输入苹果价格："))
# 转成整数
num = int(input("请输入苹果个数："))
# 转成字符串
price_str = str(price)
print(type(price))
print(type(num))
print(type(price_str))

# 格式化：
# %s-字符串，
# %d-有符号十进制，%06d表示输出的整数显示位数，不足的地方使用0不全
# %f-浮点数，%.02f,小数后面只显示两位
# %%-会输出%
money = price * num
print("%d%%" % num)
print("苹果每个 %.2f 元，购买了 %d 个，需要支付 %.4f 元" % (price, num, money))
