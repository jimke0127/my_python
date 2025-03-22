# 该文件不能直接在这里执行，必须要到系统终端对应的目录下执行：
# 1、python3 setup.py build 构建模块，会生成build/lib/message,里面就是包的文件
# 2、python3 setup.py sdist 生成压缩包，会产生一个dist目录，里面有压缩包hm_message-1.0.tar.gz
# 3、把这个压缩包分享给别人
# 4、别人拿到这个压缩包后：tar -zxvf hm_message-1.0.tar.gz,会产生目录hm_message-1.0
# 5、cd hm_message-1.0
# 6、安装模块：sudo python3 setup.py install (大概被安装在/usr/local/lib/python3.5/dist-packages这个目录下)
# 7、然后就可以直接导入包来使用了：import hm_message
# 8、如何使用，参考mm_36_包.py

# 卸载模块
# 1、hm_message.__file__ 可以查看模块的位置，(假设为/usr/local/lib/python3.5/dist-packages)
# 2、cd /usr/local/lib/python3.5/dist-packages
# 3、sudo rm -r hm_message*


from distutils.core import setup

setup(name="hm_message",  # 包名
      version="1.0",  # 版本
      description="发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="小明",  # 作者
      author_email="xxx@xxx.com",  # 作者邮箱
      url="",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
