name_list = ["张三", "李四", "王五", "王小二", "张三"]

# 判断列表是否包含某个元素
if "李四" in name_list:
    print("数组包含李四")
else:
    print("数组不包含李四")

list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

count = name_list.count("张三")
print("张三出现了 %d 次" % count)

# 从列表中删除第一次出现的数据，如果数据不存在，程序会报错
name_list.remove("张三")
print(name_list)

# 排序
name_list = ["zhangsan", "lisi", "wangwu", "aly"]
num_list = [6, 8, 4, 1, 10]
print(num_list)
# 升序，从小到大
name_list.sort()
print(name_list)
# 升序，从小到大
num_list.sort()
print(num_list)
# 降序，从大到小
num_list.sort(reverse=True)
# 翻转
num_list = [6, 8, 4, 1, 10]
num_list.reverse()
print(num_list)
