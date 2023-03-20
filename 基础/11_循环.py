i = 1
result = 0
while i <= 10:
    print("Hello python" + str(i))
    result += i
    i += 1

print(i)
print(result)

# 循环嵌套
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    row += 1
    # 这一行的目的是添加换行
    print("")

# #九九乘法
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d\t" % (j, i, i * j), end=" ")
        j += 1
    i += 1
    print("")
