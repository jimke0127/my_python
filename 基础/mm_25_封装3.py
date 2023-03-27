# 需求：
# 1、士兵许三多有一个AK47
# 2、许三多能开枪
# 3、枪可以填充以及发射子弹

class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        """
        装子弹
        @param count: 装弹数量
        """
        self.bullet_count += count

    def shoot(self):
        """
        发射子弹，每次3发
        @return:
        """
        if self.bullet_count <= 0:
            print("没有子弹了。。")
            return

        self.bullet_count -= 3
        print("[%s]突突突...[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        """
        士兵开火
        @return:
        """
        if self.gun is None:
            print("[%s] 还没有枪 。。。" % self.name)
            return

        self.gun.add_bullet(50)
        self.gun.shoot()


gun = Gun("AK47")
xsd = Soldier("许三多")
xsd.gun = gun
xsd.fire()
print(xsd.gun)
