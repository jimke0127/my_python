# 面相对象三大特性：封装、继承、多态
# 继承：
# 1、子类拥有父类的所有公有的方法和属性

class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


# 继承自Animal
class Dog(Animal):
    def bark(self):
        print("汪汪叫")


# 继承自Dog
class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

# 创建一个对象 - 狗对象
wangcai = Dog()
wangcai.eat()
wangcai.bark()

# 创建一个哮天犬的对象
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()
