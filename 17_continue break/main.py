# break : 반복문을 중단 시킨다.

for idx in range(10):
    # idx가 5보다 커지면 반복문을 중단한다.
    if idx > 5:
        break

    print('break :', idx)

# continue : 다음 반복으로 넘어간다.
for idx in range(10):

    if (idx % 2 == 0):
        continue

    print('continue :', idx)
