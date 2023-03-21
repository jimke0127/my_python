# 元组(Tuple)和列表相似，不同在于元组的元素不能修改
# 格式字符串后面的()，本质上就是一个元组
# 函数返回多个值时，本质上也是元组

# 创建空元祖
tp = ()
print(tp)

# 元组只有一个元素时，需要在元素后面添加逗号
tp = ("name",)
print(tp)

info_tuple = ("zhangsan", 18, 1.75, "zhangsan")
# 1. 取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangsan"))

# 2. 统计计数
print(info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print(len(info_tuple))

info_tuple = ("小明", 21, 1.85)
# 格式化字符串后面的 `()` 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)

# 元组和列表的转换
print("####元组和列表的转换####")
list1 = list(info_tuple)
print(list1)
print(type(list))

tuple1 = tuple(list1)
print(tuple1)
print(type(tuple1))
