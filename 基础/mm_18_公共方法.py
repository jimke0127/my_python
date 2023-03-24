t_str = "djgvbsdnv"
t_list = [9, 4, 3, 5, 6, 8, 2]
t_tuple = (2, 4, 5, 7, 3, 0)
t_dict = {
    "a": "z",
    "b": "f",
    "c": "a",
    "d": "f"
}
print(len(t_str), len(t_list), len(t_tuple), len(t_dict))
print(min(t_str), min(t_list), min(t_tuple), min(t_dict))

# 切片
print(t_str[1:3])
print(t_list[1:3])
print(t_tuple[1:3])
# 字典不能切片，以下会出错
# print(t_dict[1:2])

# 相乘|相加
t_str = "ab"
t_list = [2, 5]
t_tuple = (1, 2)
t_dict = {
    "a": "z",
    "b": "f"
}
print(t_str * 3, t_str + t_str)
print(t_list * 3, t_list + t_list)
print(t_tuple * 2)
# 字典不支持相乘|相加，以下会出错
# print(t_dict + t_dict)

# in | not in
print("a" in t_str)  # 返回 True
print("a" not in t_str)  # 返回 False
print(5 in t_list)  # 返回 True
print(5 in t_tuple)  # 返回 False
print("a" in t_dict)  # 返回 True
print("z" in t_dict)  # 返回 False

