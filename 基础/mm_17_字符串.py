str1 = "hello python"
str2 = '我的外号是"大西瓜"'
print(str2)
# 索引为6的字母
print(str1[6])
for char in str2:
    print(char)

hello_str = "Hello tom,hello dog!"
# 统计长度
print(len(hello_str))
# 统计出现的次数
print(hello_str.count("ll"))
print(hello_str.count("dog"))
# 出现的位置
print(hello_str.index("o"))
print(hello_str.rindex("o"))
# 注意：如果使用index方法传递的子字符串不存在，程序会报错！
# print(hello_str.index("abc"))

# 1. 判断空白字符
space_str = "      \t\n\r"
print(space_str.isspace())

# 2. 判断字符串中是否只包含数字
# 1> 都不能判断小数
# num_str = "1.1"
# 2> unicode 字符串
# num_str = "\u00b2"
# 3> 中文数字
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

hello_str = "hello world"
# 1. 判断是否以指定字符串开始
print("是否以he开头：%s" % hello_str.startswith("he"))

# 2. 判断是否以指定字符串结束
print("是否以world开头：%s" % hello_str.endswith("world"))

# 3. 查找指定字符串
# index同样可以查找指定的字符串在大字符串中的索引
print("是否包含字符串llo：%s" % hello_str.find("llo"))
# index如果指定的字符串不存在，会报错
# find如果指定的字符串不存在，会返回-1
print(hello_str.find("abc"))

# 4. 替换字符串
# replace方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容
print(hello_str.replace("world", "python"))
print(hello_str)

# 5、去除前后空白
poem = "\t 白日依山尽   "
print(poem)
print(poem.strip())

# 假设：以下内容是从网络上抓取的
# 要求：
# 1. 将字符串中的空白字符全部去掉
# 2. 再使用 " " 作为分隔符，拼接成一个整齐的字符串
poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n更上一层楼"
print(poem_str)

# 1. 拆分字符串，默认以空白字符(\t \n \r 空格)为分隔符
poem_list = poem_str.split()
print(poem_list)

# 2. 合并字符串
result = " ".join(poem_list)
print(result)

# 3、字符串的截取(切片)
num_str = "0123456789"
print(num_str[2:6])
print(num_str[2:])
print(num_str[0:6])
print(num_str[:6])
# 截取步长为2
print(num_str[::2])
# 取最后的字符
print(num_str[-1:])
print(num_str[-1])
# 取最后两个字符
print(num_str[-2:])
# 翻转
print(num_str[::-1])
