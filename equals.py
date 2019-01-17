class Words():
    def __init__(self,text):
        self.text = text
    def equals(self,word2):
        return self.text.lower() == word2.lower()
    def printl(self,word):
        print('1',self.text,word)
first = Words('what')   #实例化类的时候，init中有几个需要初始化的参数，就必须传入几个参数
print(first.equals('WHat'))