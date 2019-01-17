class Car():
    def exclaim(self):
        print('I,m a Car!')
    def override(self):
        print('this is override method')
class Yoga(Car): #class Yoga括号里的Car是继承的父类
    def exclaim(self): # 重写父类方法
        print('I,m a yoga !')
    def need_push(self): #子类添加父类没有的方法
        print("A little help here ?")
    def need_father_method(self):
        super().override()  # 获取父类的定义 使用super().


give_me_a_car = Car() #为类创建对象
give_me_a_yoga = Yoga() #为类创建对象

give_me_a_car.exclaim()   #调用类里面的方法
give_me_a_yoga.exclaim()    #调用类里面的方法
give_me_a_yoga.override()  #子类继承父类方法，直接调用
give_me_a_yoga.need_push()   #调用父类没有的方法
give_me_a_yoga.need_father_method()

