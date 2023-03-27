# 面相对象三大特性：封装、继承、多态
# 封装：
# 1、将属性和方法封装到一个类中
# 2、外界使用类创建对象，然后让对象调用属性或方法
# 3、对象方法的细节都被封装在类的内部

class Person:

    def __init__(self, name, weight):

        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        """
        封装一个跑步的方法
        """
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        """
        封装一个吃的方法
        """
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

# 小美爱跑步
xiaomei = Person("小美", 45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
print(xiaoming)
