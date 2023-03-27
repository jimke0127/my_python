# 递归函数两个条件
# 1、带有参数，根据参数不同，处理结果不同
# 2、要有一个出口，即当满足某个条件时函数返回，否则会出现死循环

def sum_numbers(num, sum=0):
    # 1. 出口
    if num == 1:
        return sum + 1

    else:
        sum += num
        return sum_numbers(num - 1, sum)


s = sum_numbers(100)
print(s)
