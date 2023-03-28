# 包 是一个包含多个模块的特殊目录
# 每个包下都有一个特殊的文件 __init__.py
# 包的命名和变量一致
# 好处：可以一次性导入包中的模块

# 案例
# 1、新建一个hm_message的包
# 2、在包下新建两个文件 send_message 和 receive_message
# 3、在 send_message 中定义一个 send 函数
# 4、在 receive_message 中定义一个 receive 函数
# 5、导入 hm_message 包,直接就可以实用工具 send 和 receive

import hm_message

hm_message.send_message.send("我发送的信息")
info = hm_message.receive_message.receive()
print(info)

