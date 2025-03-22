# 当类创建对象时，会自动进行以下操作
# 1、为对象在内存中分配空间(使用 __new__方法)
# 2、为对象的属性设置初始值(有__init__方法会先执行这个方法)

class Cat:
    # __init__ 方法是专门用来定义一个类具有那些属性的方法
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    # 当一个对象被从内存中销毁前，会自动调用__del__
    def __del__(self):
        print("%s 我去了" % self.name)

    # 必须返回一个字符串
    def __str__(self):
        return "我是小猫：%s" % self.name


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
print(tom)
print(tom.name)
