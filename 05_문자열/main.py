# 문자열.

str1 = "안녕하세요"
str2 = '안녕하세요'

print('str1 :', str1)
print('str2 :', str2)

# 삼중 따옴표
str3 = '''안녕하세요'''
str4 = """안녕하세요"""
print('str3 :', str3)
print('str4 :', str4)

str5 = '''이름은 '홍길동' 이고 나이는 "100"살 입니다'''
print('str5 :', str5)

str6 = '''동해물과 백두산이
          마르고 닳도록
          하느님이 보우하사
          우리나라 만세'''
print('str6 :', str6)

# 원하는 글자 가져오기
str7 = '동해물과 백두산이'

# 3번째 글자를 가져온다(인덱스번호는 0부터 시작)
print("str7의 3번째 :", str7[2])

# 3번째 ~ 6번째 글자를 가져온다.
# 인덱스 2 ~ 6 - 1 까지
print("str7의 3 ~ 6번째 :", str7[2:6])

# 처음부터 6번째까지..
print('str7의 처음부터 6번째 :', str7[0:6])
print('str7의 처음부터 6번째 :', str7[:6])

# 6번째 ~ 끝까지
print('str7의 6번째부터 끝까지 :', str7[5:])

# 처음부터 끝까지
# 처음부터 끝까지의 글자를 가지고 새로운 문자열을 만든다.
print('str7 :', str7[:])
# str7이 가지고 있는 문자열을 사용한다.
print('str7 :', str7)

# 문자열 연산
str8 = '안녕하세요'

# 문자열 + 연산 : 문자열과 문자열을 더해주면 합쳐진 새로운 문자열이
# 만들어진다.
str9 = str8 + '반갑습니다'
print('str9 :', str9)
print('str9 : ' + str9)

# 문자열과 문자열 아닌 것을 더한다.(오류)
# str10 = str8 + 100
# str 함수를 사용하면 문자열로 변환할 수 있다.
str10 = str8 + str(100)
print('str10 :', str10)

# 문자열을 곱하기 연산하면 곱하는 만큼 합쳐진 문자열이 만들어진다.
str11 = '안녕하세요'
str12 = str11 * 3
print('str12 :', str12)
















