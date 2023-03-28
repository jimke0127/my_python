# eval 可以将字符串当成 有效的表达式 来求值，并返回计算结果

a = eval("1 + 1")
print(a)

# s1是一个字符串
s1 = "[1,2,3,4,5]"
print(type(s1))
# s2 使用了eval后，变成了list
s2 = eval(s1)
print(type(s2))
