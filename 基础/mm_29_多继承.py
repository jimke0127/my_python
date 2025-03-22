# 多继承不要让父类有相同的方法

class A:

    def test(self):
        print("test 方法")


class B:

    def demo(self):
        print("demo 方法")


class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()
