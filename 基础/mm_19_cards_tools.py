card_list = []


def mark():
    print("*" * 50)
    print("")
    print("1、新建名片")
    print("2、显示全部")
    print("3、查询名片")
    print("")
    print("0、退出系统")
    print("*" * 50)


def add_cards():
    name = input("请输入您的姓名：")
    phone = input("请输入您的电话：")
    address = input("请输入您的地址：")
    qq = input("请输入您的QQ：")
    card_dict = {
        "name": name,
        "phone": phone,
        "address": address,
        "qq": qq
    }
    card_list.append(card_dict)
    print(card_dict)
    # 4. 提示用户添加成功
    print("添加 %s 的名片成功！" % name)


def show_cards():
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片！")
        return

    print("姓名\t\t电话\t\tQQ\t\t地址")
    for d in card_list:
        print(d["name"] + "\t\t" + d["phone"] + "\t\t" + d["qq"] + "\t\t" + d["address"])


def search_cards():
    find_word = input("请输入你要查询的姓名或手机号码：")
    print("姓名\t\t电话\t\tQQ\t\t地址")
    for d in card_list:
        if d["name"] == find_word or d["phone"] == find_word:
            print(d["name"] + "\t\t" + d["phone"] + "\t\t" + d["qq"] + "\t\t" + d["address"])
            deal_card(d)
            break
    else:
        print("不存在的名片：" + find_word)


def deal_card(card_dict):
    c = input("请输入你的选择 1-编辑 2-删除 0-回到上级")
    if c == "1":
        card_dict["name"] = input_card_info(input("请输入您的姓名："), card_dict["name"])
        card_dict["phone"] = input_card_info(input("请输入您的电话："), card_dict["phone"])
        card_dict["address"] = input_card_info(input("请输入您的地址："), card_dict["address"])
        card_dict["qq"] = input_card_info(input("请输入您的QQ："), card_dict["qq"])
    elif c == "2":
        card_list.remove(card_dict)
        print("删除名片成功")


def input_card_info(input_name, old_name):

    if len(input_name) > 0:
        return input_name
    else:
        return old_name
