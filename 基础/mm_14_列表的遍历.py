name_list = ["张三", "李四", "王五", "王小二", "张三"]

for name in name_list:
    print("我的名字叫　%s" % name)

# enumerate可以获取到列表的下标索引
for k, v in enumerate(name_list):
    print("%s : %s" % (k, v))

# zip 使用技巧（常用）
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
dt = {}
for k, v in zip(questions, answers):
    dt[k] = v
print(dt)

# 列表推导式
td_list = [x ** 2 for x in [2, 4, 6]]
print(td_list)
# 元组似乎不能使用推导式
td_tuple = (x ** 2 for x in [2, 4, 6])
print(td_tuple)
# 字典推导式
td_dict = {x: x ** 2 for x in (2, 4, 6)}
print(td_dict)
