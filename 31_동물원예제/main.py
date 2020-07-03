# 동물원 예제
# 동물은 이름, 나이, 하루 식사량 정보를 갖게 한다.
# 입력받은 데이터는 파일로 저장한다.
# 출력시 파일에서 데이터를 읽어와 출력을 한다.
# 출력은 다음과 같이 한다.
# 이름 : 동물1
# 나이 : 5
# 하루 식사량 : 1kg
# ---------------------------
# 이름 : 동물1
# 나이 : 5
# 하루 식사량 : 1kg
# -----------------------
# 전체 동물 수 : 100,000,000마리
# 전체 식사량 : 13,223,424kg
# 평균 식사량 : 34kg

import pickle


# 동물 정보를 담을 클래스
class Animal:

    def __init__(self, name, age, eat):
        self.name = name
        self.age = age
        self.eat = eat

    # 동물 정보를 출력하는 함수
    def showInfo(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'식사량 : {self.eat}')


# 메뉴를 출력하는 함수
def showMenu():
    print('----메뉴----')
    print('1. 정보입력')
    print('2. 정보출력')
    print('3. 종료')
    a1 = input('메뉴를 선택해주세요 : ')
    return int(a1)


# 정보를 입력받는다.
def input_info():
    print('----- 정보 입력 -----')
    name = input('이름 : ')
    age = input('나이 : ')
    eat = input('식사량 : ')

    
    # 객체 생성
    animal = Animal(name, age, eat)
    # 파일에 저장한다
    with open('animal.dat', 'ab') as fp:
        pickle.dump(animal, fp)


# dumps는 쓰는거, loads는 읽어오는거
# 정보 출력
def showAllAnimal():
    # 파일에서 객체들을 가져온다.
    with open('animal.dat', 'rb') as fp:
        # try ~ except - try 부분에서 오류가 발생하면
        # 프록램을 중단시키지 않고 except부분을 수행해준다.
        animal_list = []
        try:
            while True:
                a1 = pickle.load(fp)
                animal_list.append(a1)
        except:
            pass

    eat_total = 0

    for obj in animal_list:
        print('----------------------')
        print(f'이름 : {obj.name}')
        print(f'나이 : {obj.age}살')
        print(f'식사량 : {obj.eat}kg')
        # 식사량을 누적한다.
        eat_total = eat_total + int(obj.eat)

    print('------------------------')
    print(f'동물 수 : {len(animal_list)}')
    print(f'전체 식사량 : {eat_total}')
    print(f'식사량 평균 : {eat_total // len(animal_list)}')


if __name__ == '__main__':
    while True:
        # 메뉴 처리
        menu = showMenu()
        if menu == 1:
            input_info()
        elif menu == 2:
            showAllAnimal()
        elif menu == 3:
            break
        else:
            print('잘못 입력하셨습니다.')

