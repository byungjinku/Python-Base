# set : 중복된 데이터를 저장할 수 없다.
#       관리 기준이 없다.
#       순서가 없다.

set1 = {10, 20, 30, 40, 50}
print(type(set1))

# 비어있는 set 을 만들 때는 set 함수를
# 사용한다.
set2 = set()
print(type(set2))

# 중복된 데이터를 이용해 set을 만든다.
set3 = {50, 10, 20, 10, 20, 10, 30}
print('set3 :', set3)

# 추가
set3.add(40)
set3.add(50)
set3.add(60)
set3.add(20)
set3.add(10)
print('set3 :', set3)


