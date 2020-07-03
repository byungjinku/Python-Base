# 튜플 : 다수의 기억장소를 묶어서 관리하는 개념
# 리스트 : 다수의 기억장소를 묶어서 관리하는 개념
# 0 부터 1씩 증가하는 인덱스 번호로 관리한다.
# 튜플은 성능이 좋지만 수정, 삭제, 추가가 불가능하고
# 리스트는 성능이 덜 좋지만 수정, 삭제, 추가가 가능하다.

# 튜플 생성
tuple1 = (10, 20, 30, 40, 50)
print('tuple1 type :', type(tuple1))
print('tuple1 :', tuple1)

tuple2 = 10, 20, 30, 40, 50
print('tuple2 type :', type(tuple2))
print('tuple2 :', tuple2)

# 리스트 생성
list1 = [10, 20, 30, 40, 50]
print('list1 type :', type(list1))
print('list1 :', list1)

# 튜플, 리스트의 값들을 사용한다.
# 0부터 시작하는 인덱스 번호를 사용한다.
print('tuple1 0 :', tuple1[0])
print('tuple1 1 :', tuple1[1])
print('list1 2 :', list1[2])
print('list1 3 :', list1[3])

#########################################
print('--------------------------------')

tuple10 = 10, 20, 30, 40, 50
list10 = [10, 20, 30, 40, 50]
str10 = '안녕하세요'

# 인덱스
# 양수 인덱스 : 0부터 1씩 증가. 좌측부터 시작한다.
# 음수 인덱스 : -1부터 1씩 감소. 우측부터 시작한다.
print(tuple10[0], tuple10[1], tuple10[-1], tuple10[-2])
print(list10[0], list10[1], list10[-1], list10[-2])
print(str10[0], str10[1], str10[-1], str10[-2])

# 슬라이스
# 원하는 범위의 값을 추출해 새로운 것으로 생성한다.
# [n:m] : n ~ m - 1
# n을 생략하면 처음부터..
# m을 생략하면 끝까지..
print('----------------------------')
print(tuple10[1:3])
print(list10[1:3])
print(str10[1:3])

print(tuple10[-3:-1])
print(list10[-3:-1])
print(str10[-3:-1])

# 인덱스 1 ~ 끝까지
print(tuple10[1:])
print(list10[1:])
print(str10[1:])

# 처음부터 ~ 3 - 1까지
print(tuple10[:3])
print(list10[:3])
print(str10[:3])

# 연산
# + 연산을 하면 합쳐서 새롭게 만든다.
tuple20 = 60, 70, 80, 90, 100
list20 = [60, 70, 80, 90, 100]
str20 = '반갑습니다'

tuple30 = tuple10 + tuple20
list30 = list10 + list20
str30 = str10 + str20
print('tuple30 :', tuple30)
print('list30 :', list30)
print('str30 :', str30)

# 곱하기 : 곱한 만큼 합쳐서 새롭게 만든다.
tuple40 = tuple10 * 3
list40 = list10 * 3
str40 = str10 * 3
print('tuple40 :', tuple40)
print('list40 :', list40)
print('str40 :', str40)

# 관리하는 데이터의 개수
print('----------------------------------')
print('list10의 개수 :', len(list10))
print('tuple10의 개수 :', len(tuple10))
print('str10의 개수 :', len(str10))

print("----------------------------------")
list100 = []
print('list100의 개수 :', len(list100))
print('list100 :', list100)

# 추가
# 기억장소 0번이 없기 때문에 오류가 발생한다.
# list100[0] = 100
# print('list100의 개수 :', len(list100))
# print('list100 :', list100)

list100.append(100)
list100.append(200)
list100.append(300)
list100.append(400)
list100.append(500)
print('list100의 개수 :', len(list100))
print('list100 :', list100)

# 값 수정
list100[0] = 1000
print('list100의 개수 :', len(list100))
print('list100 :', list100)

# 제거
del list100[0]
print('list100의 개수 :', len(list100))
print('list100 :', list100)

# 인덱스번호 0 ~ 3-1까지 제거
del list100[0:3]
print('list100의 개수 :', len(list100))
print('list100 :', list100)

list200 = [10, 20, 30, 40, 50]
# 마지막 값을 내보내고 리스트에서 삭제한다.
a1 = list200.pop()
print('a1 :', a1)
print('list200의 개수 :', len(list200))
print('list200 :', list200)

# 인덱스 번째 값을 내보내고 리스트에서 삭제한다.
a2 = list200.pop(2)
print('a2 :', a2)
print('list200의 개수 :', len(list200))
print('list200 :', list200)

# 값을 지정해서 제거한다. 만약 같은 값이 여러개라면 제일 앞의
# 값을 제거한다.
list200.remove(20)
print('list200의 개수 :', len(list200))
print('list200 :', list200)

# 삽입
# 인덱스 번호 1번 위치에 100을 삽입한다.
list200.insert(1, 100)
print('list200의 개수 :', len(list200))
print('list200 :', list200)

# 위치반환
# 지정된 값의 인덱스 번호를 반환한다. 만약 같은 값이 여러개 라면
# 제일 앞에 있는 값의 인덱스가 반환된다.
idx1 = list200.index(100)
print('idx1 :', idx1)

# 존재 하지 않는 값을 찾으면 오류가 발생한다.
# idx2 = list200.index(500)
# print('idx2 :', idx2)

# 리트스 합치기
list300 = [10, 20, 30, 40, 50]
list400 = [60, 70, 80, 90, 100]

# 리스트, 튜플, 문자열 등을 + 로 연산하면 두 개를 합친 새로운
# 요소를 만든다.
list500 = list300 + list400
print('list500 :', list500)

# list300.append(list400)
# print('list300 :', list300)

# list300에 list400이 가지고 있는 값들을 추가해준다.
list300.extend(list400)
print('list300 :', list300)

# 리스트에 값이 존재하는지 확인한다.
chk1 = 50 in list300
print('chk1 :', chk1)

chk2 = 200 in list300
print('chk2 :', chk2)

# count : 리스트, 튜플, 문자열에서 지정된 값이 몇개가 있는지..
list600 = [10, 20, 30, 40, 50, 10, 20, 10, 20, 10]
cnt1 = list600.count(20)
print('20의 개수 :', cnt1)

# 정렬
list700 = [30, 10, 20, 80, 60, 70]
print('정렬 전 :', list700)

list700.sort()
print('오름 차순 정렬 :', list700)

list700.sort(reverse=True)
print('내림 차순 정렬 :', list700)

# 리스트를 뒤집는다.
list700.reverse()
print("뒤집기 :", list700)

# 하나의 리스트나 튜플안에 다양한 타입의 값을 담을 수 있다.
list800 = [100, 11.11, '안녕하세요', True]
print('list800 :', list800)














