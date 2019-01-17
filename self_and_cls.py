class A():
    count = 0
    def __init__(self):
        A.count += 1        #使用类变量 是A.count
    def exp(self):          #self 作为第一个参数的方法是实例方法
        print("I,m A!")
    @classmethod  #类方法标示
    def kids(cls):         #类方法的第一个参数一般是cls
        print("A has ",cls.count,"little objects.")     #cls.count 等同于 A.count
        return ''       #如果没有return 方法被调用则默认输出none
    @staticmethod       #静态类方法
    def static_method():
        print("我不需要实例化直接调用就好")

count_1 = A()       #实例化类
A.static_method()       #不需要实例即不用创建类对象就可以调用，print是打印方法的返回值；
A.count      #类中的全局变量也可以直接调用
A.kids()   #类方法可以不用实例 直接调用
count_1.exp()        #调用实例化方法exp
count_1.kids()       #调用类方法kids

count_2 = A()       #实例化类

print(A.kids())     #类方法可以不用实例 直接调用
