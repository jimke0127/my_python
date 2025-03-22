# 类名 遵循大驼峰命名法
# 类的三要素：类名 属性 方法

class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()
print(tom)
addr = id(tom)
print("%x" % addr)
print("=" * 50)
# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
addr = id(lazy_cat)
print("%x" % addr)
print("*" * 50)

# dir内置函数，可以查看对象(在Python中，变量、数据、函数都是对象)内所有的属性和方法
print(dir(Cat))
