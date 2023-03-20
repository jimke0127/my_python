age = int(input("请输入你的年龄："))
if age >= 18:
    print("欢迎光临本网吧")
else:
    print("你还没有成年，回家写作业去吧！")

is_employee = True
if not is_employee:
    print("非员工，请勿入内")
else:
    print("公司职员，请进")

holiday_name = "中秋节"
if holiday_name == "情人节":
    print("买玫瑰")
elif holiday_name == "中秋节":
    print("吃月饼")
else:
    print("开心就好")

