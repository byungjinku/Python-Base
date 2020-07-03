# 클래스를 가지고 만든 객체를 인스턴스라고 부르기도 한다.
# 객체를 생성해야지만 사용할 수 있는 맴버를 인스턴스 맴버라고 부른다.
# 객체를 생성하지 않아도 사용할 수 있는 맴버를 클래스 맴버라고 부른다.

class TestClass1 :

    # 클래스 변수
    # 객체를 생성하지 않고 사용하는 변수
    class_v1 = 100
    class_v2 = 200
    
    def __init__(self, v1, v2):
        # 인스턴스 변수
        self.a1 = v1
        self.a2 = v2
        
    # 인스턴스 메서드
    def f1(self):
        print(f'a1 : {self.a1}')
        print(f'a2 : {self.a2}')

    # 클래스 메서드
    @staticmethod
    def f2():
        print(f'클래스 메서드 호출')
        print(f'TestClass1.class_v1 : {TestClass1.class_v1}')
        print(f'TestClass1.class_v2 : {TestClass1.class_v2}')


t1 = TestClass1(10, 20)
t2 = TestClass1(100, 200)
t1.f1()
t2.f1()

print('-------------------------')
# 인스턴스 변수는 객체를 통해 접근
print(f't1.a1 : {t1.a1}')
print(f't2.a1 : {t2.a1}')
# 클래스 변수는 클래스를 통해 접근
print(f'TestClass1.class_v1 : {TestClass1.class_v1}')
print(f'TestClass1.class_v2 : {TestClass1.class_v2}')
# 객체를 가지고 변수를 사용하면 객체 자신에 변수가 있는지 확인해보고
# 없으면 객체를 만들 때 사용한 클래스에 접근해서 클래스 변수에 있는지
# 확인한다. 객체를 통해 클래스 변수에 접근이 가능하지만 클래스 변수는
# 클래스를 통해 접근해서 사용하는 것을 권장한다.
print(f't1.class_v1 : {t1.class_v1}')
print(f't1.class_v2 : {t1.class_v2}')
# 파이썬은 객체를 통해 클래스 맴버 접근이 가능한기 때문에
# 클래스에 변수를 추가하면 생성된 객체 모두에 변수가 추가된것과
# 같은 효과를 볼 수 있다.
TestClass1.class_v3 = 300
print(f'TestClass1.class_v3 : {TestClass1.class_v3}')
print(f't1.class_v3 : {t1.class_v3}')
print(f't2.class_v3 : {t2.class_v3}')

TestClass1.class_v3 = 3000
print(f'TestClass1.class_v3 : {TestClass1.class_v3}')
print(f't1.class_v3 : {t1.class_v3}')
print(f't2.class_v3 : {t2.class_v3}')

t1.class_v3 = 30000
print(f'TestClass1.class_v3 : {TestClass1.class_v3}')
print(f't1.class_v3 : {t1.class_v3}')
print(f't2.class_v3 : {t2.class_v3}')

# 클래스 메서드 호출
TestClass1.f2()
t1.f2()
t2.f2()






