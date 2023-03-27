# 缺省参数的默认值
# 1、有默认值的参数在末尾，以便于传参时可以缺省
# 2、当有多个可以缺省的参数时，可以指定参数名
def print_info(name, title="", gender=True):
    """
    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s" % (title, name, gender_text))


# 假设班上的同学，男生居多！
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明", "副班长")
print_info("老王")
print_info("小美", gender=False)
