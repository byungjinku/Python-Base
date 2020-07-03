# 사이트 주소 : https://pjt3591oo.github.io/

# 페이지 소스보기 해서 나오는 소스에 필요한 데이터가 있는 경우.

# pip install requests
# pip install bs4
# pip install lxml

import requests
import bs4
import time

# 주소
url = 'https://pjt3591oo.github.io/'

# 페이지 번호
page = 1

while True :
    # 딜레이타임을 준다(초단위)
    time.sleep(1)
    # 요청한다.
    response = requests.get(url)
    # print(response.text)
    # bs4 객체를 생성한다.
    # bs4 객체를 생성하면 지정한 HTML 코드를 모두 분석해서 가지고 있다.
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())

    # class가 p인 div 태그 모두를 가져온다
    div1 = soup.select('div.p')
    for obj in div1 :
        # a 태그를 가져온다.
        a1 = obj.select_one('a')
        print(a1.text.strip())

        # h4 태그를 가져온다.
        a2 = obj.select_one('h4')
        print(a2.text.strip())

        # span 태그를 가져온다.
        a3 = obj.select_one('span.date')
        a3_list = a3.text.split('|')
        print(a3_list[0].strip())
        print(a3_list[1].strip())

        # 파일에 저장한다.
        with open('case1.csv', 'at', encoding='UTF-8') as fp :
            b1 = a1.text.strip()
            b2 = a2.text.strip()
            b3 = a3_list[0].strip()
            b4 = a3_list[1].strip()
            fp.write(f'{b1},{b2},{b3},{b4}\n')

        print('-----------------------------')

    # 다음 페이지로 이동할 것인지 검사한다.

    ul1 = soup.select_one('ul.pager')
    span1 = ul1.select_one('span')
    if span1 != None and span1.text.strip() == 'Next' :
        break
    else :
        # 다음 페이지의 주소
        page = page + 1
        url = f'https://pjt3591oo.github.io/page{page}/'








