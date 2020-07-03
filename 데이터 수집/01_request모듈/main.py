# request 모듈
# 웹 서버 요청을 쉽게 할 수 있도록 만든 모듈
# pycharm의 하단에 terminal을 띄우고 다음과 같이 입력한다.
# pip install requests

import requests

# 접속할 페이지의 주소
url = 'https://google.com'
# 요청
response = requests.get(url)
# response를 출력했을 때 200 이라고 나오면 정상
# 500 : 서버 오류.
# 404 : 주소가 잘못된것.
print(f'response : {response}')
# 405 : 요청 방식이 잘못되었때.
# 요청방식 : get, post
response2 = requests.post(url)
print(f'response2 : {response2}')

if response.status_code == 200 :
    print('구글은 get방식을 지원합니다')

if response2.status_code == 200 :
    print('구글은 post방식을 지원합니다.')

# 서버로 부터 받아온 데이터
print(response.text)










