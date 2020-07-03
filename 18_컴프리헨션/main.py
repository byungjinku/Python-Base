
# 튜플
t1 = 10, 20, 30, 40, 50
# 튜플, 리스트 등에 담긴 값을 가지고 와서 연산을 수행한다음
# 그 결과를 가지고 있는 리스트를 만드는 경우
list1 = []
for value in t1 :
    a1 = value * 2
    list1.append(a1)

print('list1 :', list1)

list2 = [value * 2 for value in t1]
print('list2 :', list2)

# t2에서 짝수만 연산을 하고 담는다.
t2 = 1, 2, 3, 4, 5
list3 = []
for value in t2 :
    if value % 2 == 0 :
        list3.append(value * 2)

print('list3 :', list3)

list4 = [value * 2 for value in t2 if value % 2 == 0]
print('list4 :', list4)




