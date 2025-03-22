# open 函数默认以只读方式打开文件
# r--只读
# w--只写
# a--追加

# 1. 打开文件
file = open("readme")

# 2. 读取文件内容
text = file.read()
print(text)
print(len(text))
# 读取文件后，文件指针会指到最末尾
print("-" * 50)

# 再次读取，内容就是空的了
text = file.read()
print(text)
print(len(text))

# 3. 关闭文件
file.close()
