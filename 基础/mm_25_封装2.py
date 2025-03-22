# 需求：
# 房子(House)有户型、总面积、家具名称列表
# 家具(HouseItem) 有名字、占地面积
# 将家具添加到房子中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.rest_area = area
        self.item_list = []

    def __str__(self):
        return "户型为%s\n总面积为%.2f\n剩余面积为%.2f\n家具为：%s" % (
            self.house_type, self.area, self.rest_area, self.item_list)

    def add_item(self, item):
        """
        添加家具
        @param item: 家具对象
        @return:
        """
        if item.area > self.rest_area:
            print("%s 的面积太大了，无法添加" % item.name)
            return

        self.item_list.append(item.name)
        self.rest_area -= item.area


# 1. 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 200)
table = HouseItem("餐桌", 1.5)
# 2、创建房子对象
my_house = House("三房一厅", 160)
# 3、添加家具
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)
