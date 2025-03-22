# 字典类似关联数组，键名与键值承成对出现，键与值用：分隔
# 键值对之间用逗号,间隔

# 创建空字典
dist = {}

# 初始化字典
xm = {
    "name": "小明",
    "gender": "男",
    "height": 175
}
print(xm)

xiaoming_dict = {"name": "小明"}
# 1. 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的key不存在，程序会报错！
# print(xiaoming_dict["name123"])

# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"
print(xiaoming_dict)
# 3. 删除
xiaoming_dict.pop("name")
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
# xiaoming_dict.pop("name123")
print(xiaoming_dict)

xiaoming_dict = {"name": "小明",
                 "age": 18}
# 1. 统计键值对数量
print(len(xiaoming_dict))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
# 3. 清空字典
xiaoming_dict.clear()

print(xiaoming_dict)
