# 不同的子类对象调用相同的父类方法，产生不同的执行结果
# 要使用多态，必须以继承和重写父类方法 为前提

class Person(object):

    def __init__(self, name):
        self.name = name

    def work(self):
        print("%s 工作日每天都要工作..." % self.name)


class Programmer(Person):

    def work(self):
        """
        程序员的工作就是写代码
        """
        super().work()
        print("%s的工作内容就是写代码..." % self.name)


class Designer(Person):
    def work(self):
        """
        设计师的工作就是设计各种方案
        """
        super().work()
        print("%s的工作内容就是设计方案..." % self.name)


pg = Programmer("小明")
pg.work()

xh = Designer("小红")
xh.work()
