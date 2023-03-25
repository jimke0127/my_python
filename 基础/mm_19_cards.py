import mm_19_cards_tools as tool

while True:
    tool.mark()
    c = input("请输入您的选择：")
    print("您选择的操作是【%s】" % c)
    if c == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    elif c == "1":
        tool.add_cards()
    elif c == "2":
        tool.show_cards()
    elif c == "3":
        tool.search_cards()
    else:
        print("您输入的不正确，请重新选择")


