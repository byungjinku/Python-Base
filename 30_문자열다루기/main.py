# split : 문자열 나누기
str1 = '동해물과 백두산이_마르고 닳도록'

list1 = str1.split()
list2 = str1.split('_')
print(f'list1 : {list1}')
print(f'list2 : {list2}')

# strip : 문자열 앞뒤 제거
str3 = '    안녕하세요    '
str4 = 'aaaa안녕하세요aaaa'

print(f'[{str3}]')
print(f'[{str3.rstrip()}]')
print(f'[{str3.lstrip()}]')
print(f'[{str3.strip()}]')

print(f'[{str4}]')
print(f'[{str4.rstrip("aaaa")}]')
print(f'[{str4.lstrip("aaaa")}]')
print(f'[{str4.strip("aaaa")}]')

# join : 문자열 합치기
list3 = ['aaa', 'bbb', 'ccc']
str5 = ' '.join(list3)
str6 = ','.join(list3)
print(f'str5 : {str5}')
print(f'str6 : {str6}')

# 믄자열 찾기
str7 = 'aaabbbccc'
idx1 = str7.index('bbb')
idx2 = str7.find('bbb')
print(f'idx1 : {idx1}')
print(f'idx2 : {idx2}')

# 없는 문자열 찾기
# 오류발생
# idx3 = str7.index('ddd')
idx4 = str7.find('ddd')
print(f'idx4 : {idx4}')

