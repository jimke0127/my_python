# 目的--让类创建的对象只有唯一的一个对象
# 即--每一次执行 类名() 返回的对象，内存地址是相同的
# 使用类名创建对象时，会先调用 __new__ 方法为对象分配空间，
# 然后返回对象的引用

# 所以，要实现单例，就要重写__new__方法，
# 特别注意：重写__new__ 一定要 return super().__new__(cls)，
# 否则，python解释器就得不到分配了空间的对象引用，就不会初始化__init__
class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 1. 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

        # 2. 如果没有执行过，在执行初始化动作
        print("初始化播放器")

        # 3. 修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象,应该是返回相同的内存地址
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)


