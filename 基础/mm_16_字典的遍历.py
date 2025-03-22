xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print("%s - %s" % (k, xiaoming_dict[k]))

# 或者下面这种方式
for k, v in xiaoming_dict.items():
    print("%s - %s" % (k, v))

# 获取字典所有的键
print(list(xiaoming_dict.keys()))
# 获取字典所有的值并排序
print(sorted(list(xiaoming_dict.values())))

# 将 多个字典 放在 一个列表 中，再进行遍历
card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"}
]

for card_info in card_list:

    print(card_info["name"])
