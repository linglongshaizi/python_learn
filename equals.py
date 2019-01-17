class Words():
    def __init__(self,text):
        self.text = text
    def equals(self,word2):
        return self.text.lower() == word2.lower()
    def printl(self,word):
        print('1',self.text,word)
first = Words('what')   #实例化类的时候，init中有几个需要初始化的参数，就必须传入几个参数
print(first.equals('WHat')) #调用实例化方法的时候，如果需要传参则要传递参数；实例化的参数是在init中实例 ，目前我的理解是全局变量；


#书中的例子用以介绍__eq__

class Word():
    def __init__(self,text):
        self.text = text
    def __eq__(self, words):
       return self.text.lower() == words.text.lower()

first = Word('NUM')
second = Word('num')

print(first == second)  #直接使用eq进行比较