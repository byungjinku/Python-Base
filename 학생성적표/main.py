#실습 평가 1) 학생의 정보를 입력 받아 출력하는 프로그램을 작성하시오
#학생 정보는 이름, 나이, 국어점수, 수학점수, 영어점수로 구성된다.

# 학생 정보
# --------------------
# 이름 : 홍길동
# 나의 : 30세
# 국어 점수 : 80점
# 영어 점수 : 70점
# 수학 점수 : 60점
# 총점 : 260점
# 평균 : 70점

# --------------------

# 이름 : 최길동
# 나의 : 28세
# 국어 점수 : 90점
# 영어 점수 : 90점
# 수학 점수 : 80점
# 총점 : 200점
# 평균 : 60점

# 전체 총점 : 1000
# 전체 평균 : 80
#----------------------------

import pickle

class Student:

    def __init__(self, name, age, kor, mat, eng):
        self.name = name
        self.age = age
        self.kor = kor
        self.mat = mat
        self.eng = eng

    def showInfo(self):

        exam_total = int(self.kor) + int(self.mat) + int(self.eng)
        exam_avg = round(float(exam_total / 3), 2)

        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}세')
        print(f'국어점수 : {self.kor}점')
        print(f'수학점수 : {self.mat}점')
        print(f'영어점수 : {self.eng}점')
        print(f'총점 : {exam_total}점')
        print(f'평균 : {exam_avg}점')

def showMenu():
    print('----메뉴----')
    print('1. 정보입력')
    print('2. 정보출력')
    print('3. 종료')
    a1 = input('메뉴를 선택해주세요 : ')
    return float(a1)

def input_info():
    print('----- 정보 입력 -----')
    name = input('이름 : ')
    age = input('나이 : ')
    kor = input('국어점수 : ')
    mat = input('수학점수 : ')
    eng = input('영어점수 : ')

    student = Student(name, age, kor, mat, eng)
    with open('student.dat', 'ab') as fp:
        pickle.dump(student, fp)

def showAllStudent():
    with open('student.dat', 'rb') as fp:

        student_list = []
        try:
            while True:
                a1 = pickle.load(fp)
                student_list.append(a1)
        except:
            pass

    test_total = 0

    for obj in student_list:
        print('----------------------')

        obj.showInfo()

        test_total = test_total + float(obj.kor) + float(obj.eng) + float(obj.mat)


    print('----------------------')
    print(f'전체 총점 : {test_total}점')
    print(f'전체 평균 : {test_total // len(student_list) // 3}점')


if __name__ == '__main__':
    while True:
        menu = showMenu()
        if menu == 1 :
            input_info()
        elif menu == 2 :
            showAllStudent()
        elif menu == 3 :
            break
        else:
            print('잘못 입력하셨습니다.')


