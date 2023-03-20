import random

player = int(input("请输入你要出的拳，石头1/剪刀2/布3："))
computer = random.randint(1,3)
print("玩家出的拳为 %d,电脑出的拳为 %d" % (player,computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("电脑弱爆了！")
elif player == computer:
    print("平局，再来")
else:
    print("我不服，再来")
