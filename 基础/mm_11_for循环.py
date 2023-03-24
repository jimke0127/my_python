for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break退出了循环
    # else 下方的代码就不会被执行
    print("for循环用使用break退出，这里就不会执行")

print("循环结束")
