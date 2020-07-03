# 다음과 같이 출력되도록 만드세요~
# 단 for문을 사용한다.

# 1 2 3
# 4 5 6
# 7 8 9
# print('1 2 3')
# print('4 5 6')
# print('7 8 9')
for idx in range(3) :
    # a1 = 1 + (idx * 3)
    # a2 = 2 + (idx * 3)
    # a3 = 3 + (idx * 3)
    # print(a1, a2, a3)
    for idx2 in range(3) :
        b1 = 1 + idx2
        a1 = b1 + (idx * 3)
        print(a1, end=' ')

    print()

print('----------------------')



# 3 2 1
# 6 5 4
# 9 8 7

# 1 4 7
# 2 5 8
# 3 6 9

# 0
# 0 0
# 0 0 0

#     0
#   0 0
# 0 0 0

# 0   0
#   0
# 0   0







