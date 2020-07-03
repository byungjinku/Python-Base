# 텅 비어있는 컨테이너 타입을 생성한다.
tuple1 = tuple()
list1 = list()
dic1 = dict()
set1 = set()
print('tuple1 type :', type(tuple1))
print('list1 type :', type(list1))
print('dic1 type :', type(dic1))
print('set1 type :', type(set1))

print('tuple1 :', tuple1)
print('list1 :', list1)
print('dic1 :', dic1)
print('set1 :', set1)

#################################
list10 = [10, 10, 20, 20, 30]
tuple10 = 10, 10, 20, 20, 30
set10 = {10, 20, 30}
dict10 = {'a1' : 10, 'a2' : 20}

# 리스트로 만들기
list11 = list(tuple10)
list12 = list(set10)
# 딕셔너리는 이름을 가지고 리스트를 만든다.
list13 = list(dict10)
# 이름을 가지고 리스트를 만든다.
list14 = list(dict10.keys())
# 값을 가지고 리스트를 만든다.
list15 = list(dict10.values())
# (이름, 값)의 튜플이 생성되고 이 튜플들이
# 들어 있는 리스트를 만든다.
list16 = list(dict10.items())
print('list11 :', list11)
print('list12 :', list12)
print('list13 :', list13)
print('list14 :', list14)
print('list15 :', list15)
print('list16 :', list16)

print('---------------------------')
# 튜플 만들기
tuple11 = tuple(list10)
tuple12 = tuple(set10)
print('tuple11 :', tuple11)
print('tuple12 :', tuple12)

print('----------------------------')
# set 만들기
set11 = set(list10)
set12 = set(tuple10)
print('set11 :', set11)
print('set12 :', set12)

print('-----------------------------')

# 딕셔너리 만들기
# 이름과 값의 쌍으로 이루어진 데이터를
# 가지고 만든다.
dict10 = dict([
    ('a1', 100), ('a2', 200),
    ('a3', 300), ('a4', 400)
])
print(dict10)

# 데이터를 저장할 때 사용할 이름 리스트
key_list = 'a1', 'a2', 'a3', 'a4', 'a5'
zip1 = zip(key_list, tuple10)
print(list(zip1))
dict11 = dict(zip(key_list, tuple10))
print(dict11)

########################################
print('---------------------------------')
# 리스트나 튜플에 담긴 값을 변수에 담는다.
list20 = [10, 20, 30, 40, 50]
tuple20 = 10, 20, 30, 40, 50

# 각각의 값을 변수에 담는다.
a1 = list20[0]
a2 = list20[1]
a3 = list20[2]
a4 = list20[3]
a5 = list20[4]
print(a1, a2, a3, a4, a5)

# 리스트나 튜플에 담긴 값과 동일한 개수의 변수를 나열한다.
a6, a7, a8, a9, a10 = list20
a11, a12, a13, a14, a15 = tuple20
print(a6, a7, a8, a9, a10)
print(a11, a12, a13, a14, a15)


a16, a17, a18, a19, a20 = 10, 20, 30, 40, 50
print(a16, a17, a18, a19, a20)











