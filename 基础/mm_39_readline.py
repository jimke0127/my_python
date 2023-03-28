# read 方法默认会把文件的所有内容一次性读取到内存
# 如果文件太大，对内存的占用会非常挺严重

# readline 方法可以一次读取一行内容
# 方法执行后，会把文件指针移动到下一行开头

file = open("readme")

while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    print(text)

file.close()
