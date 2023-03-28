# python3 中默认使用UTF-8编码格式
# python2 中默认使用的是ASCII 编码格式
# 所以在python2文件的第一行增加# *-* coding:utf8 *-*，解释器会以utf-8编码来处理文件

# *-* coding:utf8 *-*

# 引号前面的u告诉解释器这是一个utf8编码格式的字符串
hello_str = u"hello世界"

print(hello_str)

for c in hello_str:
    print(c)
    