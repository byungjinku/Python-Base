# 학생 정보를 관리한다.
# 학생의 이름, 국어점수, 영어점수, 수학점수를 입력 받는다.
# 출력은 다음과 같이 한다.
# --------------------
# 이름 : 홍길동
# 국어 점수 : 100점
# 영어 점수 : 90점
# 수학 점수 : 70점
# 총점 : 260점
# 평균 : 86점
# 등급 : A
# --------------------
# 전체 총점 : 몇점~
# 전체 평균 : 몇점~

# 학생정보를 입력 받을 때 더 입력을 받을 것인지를 물어본다.
# 계속 입력?(1. YES, 2. NO) :

# 점수 등급
# 100 ~ 80 : A
# 79 ~ 60 : B
# 59 ~ : F


# 입력
# 학생 정보를 담을 딕셔너리들이 담길 리스트
student_list = []
# 전체 총점과 평균을 담을 변수
total = 0
avg = 0
# 계속 입력 여부값을 가지고 있는 변수
a1 = 1

# 입력받는다.
while a1 == 1 :
    # 학생 정보를 입력 받는다.
    name1 = input('이름 :')
    kor1 = input('국어 점수 :')
    eng1 = input('영어 점수 :')
    mat1 = input('수학 점수 :')
    # 입력 받은 정보를 딕셔너리에 담는다.
    dict1 = {}
    dict1['name'] = name1
    dict1['kor'] = int(kor1)
    dict1['eng'] = int(eng1)
    dict1['mat'] = int(mat1)
    dict1['total'] = int(kor1) + int(eng1) + int(mat1)
    dict1['avg'] = dict1['total'] // 3

    # 리스트에 담는다.
    student_list.append(dict1)
    print(student_list)

    chk = input('계속 입력?(1. YES, 2. NO) :')
    a1 = int(chk)

# 출력
# 학생 개개인의 정보를 출력
for student in student_list :
    print('----------------------')
    print('이름 :', student['name'])
    print('국어점수 :', student['kor'])
    print('영어점수 :', student['eng'])
    print('수학점수 :', student['mat'])
    print('총점 :', student['total'])
    print('평균 :', student['avg'])

# 전체 정보를 출력
for student in student_list :
    total = total + student['total']

avg = total // len(student_list) // 3

print('---------------------------')
print('전체 총점 :', total)
print('전체 평균 :', avg)








