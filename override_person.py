class Person():
    def __init__(self,name):
        self.name = name
class MDPerson():
    def __init__(self,name):
        self.name = "Doctor" + name
class JDPerson():
    def __init__(self,name):
        self.name = name + ", Esquire"

person = Person(1)
person.name = 10
print(person.name)
# doctor = MDPerson('Tom')
# lawyer = JDPerson('Jack')
#
# print(person.name)
# print(doctor.name)
# print(lawyer.name)