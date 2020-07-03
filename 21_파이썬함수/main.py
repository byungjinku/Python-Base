# 매개변수 지정하기
def test1(a1, a2, a3) :
    print('test1호출')
    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print(f'a3 : {a3}')

test1(100, 200, 300)
# 값을 전달할 때 값이 담길 매개변수를 지정한다.
test1(a3=300, a1=100, a2=200)
# a1에 지정될 값이 정해져 있지 않고, 3번째 값이
# 이미 값이 결정된 a3로 전달하려고 시도한다(오류)
# test1(a3=300, a2=200, 100)
test1(100, a3=300, a2=200)

# 매개변수의 기본값
# 함수를 호출할 때 값을 정해주지 않으면 기본값이 셋팅된다.
def test2(a1, a2 = 2, a3 = 3) :
    print('test2호출')
    print(f'a1 : {a1}')
    print(f'a2 : {a2}')
    print(f'a3 : {a3}')

# 첫 번째 매개변수인 a1은 기본값이 설정되어 있지 않으므로
# 반드시 값을 지정해야 한다.
# test2()
test2(100)
test2(100, 200)
test2(100, 200, 300)
test2(100, a3=300)

# 반환값
def test3(a1, a2) :
    r1 = a1 + a2
    r2 = a1 - a2
    r3 = a1 * a2
    r4 = a1 // a2
    # 값 4개를 쉼표로 구분해서 나열했으므로 값 4개를 가지고 있는
    # 튜플이 생성되고 튜플이 반환된다.
    return r1, r2, r3, r4

result1 = test3(100, 4)
print(f'result1 type : {type(result1)}')

# 반환되는 튜플이 4개의 값을 가지고 있으므로 4개의 변수를
# 정의해서 각각 값을 받게 된다.
v1, v2, v3, v4 = test3(100, 4)
print(f'v1 : {v1}')
print(f'v2 : {v2}')
print(f'v3 : {v3}')
print(f'v4 : {v4}')






