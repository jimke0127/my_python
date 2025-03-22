# 在属性或方法前增加两个下划线，就是私有的属性或方法
# 私有属性或方法在类的外部不能访问

class Women:

    def __init__(self, name):

        self.name = name
        # 女人的年龄，设置为私有的属性
        self.__age = 18

    def __secret(self):
        """
        女人都有自己的秘密，类的外部不能访问
        """
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))

    def test(self):
        """
        类的内部可以访问私有的属性或方法
        """
        print(self.__age)
        self.__secret()


class Xiaohong(Women):

    def work(self):
        print("热爱工作")

xiaofang = Women("小芳")
# 私有属性，在外界不能够被直接访问
# print(xiaofang.__age)
# 私有方法，同样不允许在外界直接访问
# xiaofang.__secret()

# 类的内部可以访问私有的属性或方法
xiaofang.test()

xh = Xiaohong("小红")
xh.test()
