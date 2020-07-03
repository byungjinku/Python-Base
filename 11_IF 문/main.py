# if 문 : 특정 조건에 만족할 경우 수행되는 조건문
a1 = 10

# if : 만약 ~ 한다면...
if a1 > 5 :
    print('a1은 5보다 큽니다')

if a1 < 5 :
    print('a1은 5보다 작습니다')

if a1 < 5 :
    print('들여쓰기 테스트')
    print('이 부분이 수행될까요? 1')

if a1 < 5 :
    print('들여쓰기 테스트')
print('이 부분이 수행될까요? 2')

# else : 조건에 만족하지 않을 경우 수행될 부분
# if ~ else : 만약 ~ 한다면... 하고 그렇지 않으면 ... 해라
if a1 > 5 :
    print('a1은 5보다 큽니다')
else :
    print('a1은 5보다 크지 않습니다')
    
if a1 > 10 :
    print('a1은 10보다 큽니다')
else :
    print('a1은 10보다 크지 않습니다')

# 조건이 다수인 경우. 다수의 조건 중에 한군데만
# 수행된다.
if a1 == 1 :
    print('a1은 1입니다')
elif a1 == 3 :
    print('a1은 3입니다')
elif a1 == 10 :
    print('a1은 10입니다')
elif a1 == 20 :
    print('a1은 20입니다')
else :
    print('a1은 1, 3, 10, 20이 아닙니다다')


# 중첩
a1 = 10
a2 = 20

if a1 == 3 :
    if a2 == 5 :
        print('a1은 3, a2는 5')
    else :
        print('a1은 3, a2는 5가 이닙니다')
elif a1 == 10 :
    if a2 == 5 :
        print('a1은 10, a2는 5')
    elif a2 == 20 :
        print('a1은 10, a2는 20')











