# 列表是有序的对象集合，类似php中的不带键的数组
# 可变类型(列表|字典) 一旦定义了列表或字典，内存地址就固定了，
# 使用自身方法改变列表或字典，地址不变，但是重新赋值会改变
# 不可变类型(数字、字符串、元组)，一旦重新赋值，地址会也变化

name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
# list index out of range - 列表索引超出范围
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.index("wangwu"))

# 2. 修改
name_list[1] = "李四"
print(name_list)
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错！
# name_list[3] = "王小二"

# 3. 增加
# append 方法可以向列表的末尾追加数据
name_list.append("王小二")
print(name_list)
# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(1, "小美眉")
print(name_list)

# extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["王小二", "孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)
print(name_list)
#去重
name_t = set(name_list) 
print(name_t)

# 4. 删除
# remove 方法可以从列表中删除指定的数据
name_list.remove("wangwu")
print(name_list)
# pop 方法默认可以把列表中最后一个元素删除
name_list.pop()
print(name_list)
# pop 方法可以指定要删除元素的索引
name_list.pop(3)
print(name_list)
# 删除第二个元素
del name_list[1]
print(name_list)
# clear 方法可以清空列表
name_list.clear()

print(name_list)
