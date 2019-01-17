class Quote():
    def __init__(self,person,words):
        self.person = person
        self.words =words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote): #Quote 的子类
    def says(self):     #多态类似于重写  但是区别于重写
        return self.words +'?'
class ExclamationQuote(Quote):  #Quote 的子类
    def says(self):
        return self.words + '!'

hunter = Quote('Tang','Im hunting animals')
print(hunter.who(),'says:',hunter.says())

hunter1 = QuestionQuote('Tbag','Are you kidding')
print(hunter1.who(),'says:',hunter1.says())

hunter2 = ExclamationQuote('Tom','I,m hungry')
print(hunter2.who(),'says:',hunter2.says())