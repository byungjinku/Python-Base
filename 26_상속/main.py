# 상속 : 클래스를 만들 때 다른 클래스가 가지고 있는 맴버를 물려받는 개념
# 물려주는 쪽을 부모클래스(SuperClass)라고 부르고 물려 받는 쪽을 자식 클래스
# (SubClass)라고 부른다.
# 자식 클래스는 부모클래스로 부터 물려받은 것들을 자기것처럼 사용한다.
# 클래스를 작성할 때 각 클래스마다 중복되는 부분이 있을 경우 사용한다.

# 부모 클래스
class Animal :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(self.name)
        print(self.age)

# Animal 상속
class Dog(Animal) :
    def __init__(self, name, age, voice):
        # self.name = name
        # self.age = age
        # 부모의 init을 호출한다.
        super().__init__(name, age)
        self.voice = voice

    # def showInfo(self):
    #     print(self.name)
    #     print(self.age)

    def getVoice(self):
        print(self.voice)


class Cat(Animal) :
    def __init__(self, name, age, box):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.box = box

    # def showInfo(self):
    #     print(self.name)
    #     print(self.age)

    def showBox(self):
        print(self.box)

d1 = Dog('멍멍이', 5, '멍멍')
d2 = Dog('왈왈이', 6, '왈왈')
d1.showInfo()
d2.showInfo()
d1.getVoice()
d2.getVoice()

c1 = Cat('냐용이', 3, 5)
c2 = Cat('야옹이', 4, 3)
c1.showInfo()
c2.showInfo()
c1.showBox()
c2.showBox()





