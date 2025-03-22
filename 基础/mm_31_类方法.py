# 类属性就是定于在class内而又在__init__外的属性
# (定义在__init__内的属性是实例属性)
# 类方法需要用@classmethod 来标识，表明这是一个类方法
# 类方法的第一个参数应该是cls (而实例方法的第一个参数是self)
# 调用类方法不需要实例化，只需要用：类名.方法名()

class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()
