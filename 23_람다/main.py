def test1(a1, a2, a3) :
    return a1 + a2 + a3

r1 = test1(100, 200, 300)
print(f'r1 : {r1}')

test2 = lambda a1, a2, a3 : a1 + a2 + a3
r2 = test2(100, 200, 300)
print(f'r2 : {r2}')

###############################################
# 고차함수 : 함수를 매개변수로 받거나 함수를 반환하는 함수
# 매개변수 f1은 함수를 받을 것이고 넘어온 함수를 호출해서
# 결과를 가져오고 있다.
def test3(a1, a2, f1) :
    result1 = f1(a1, a2)
    print(f'result1 : {result1}')

def k1(v1, v2) :
    return v1 + v2

test3(100, 200, k1)

def k2(v1, v2) :
    return v1 - v2

test3(100, 200, k2)

test3(100, 200, lambda v1, v2 : v1 * v2)
test3(200, 5, lambda v1, v2 : v1 // v2)







