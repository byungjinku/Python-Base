
# 같은 모듈에 있는 함수
def main_function1() :
    print('같은 모듈의 fun1')

def main_function2() :
    print('같은 모듈의 fun2')

if __name__ == '__main__' :
    # 같은 모듈에 있는 것은 그냥 쓰면 된다.
    main_function1()
    main_function2()

    # 같은 패키지 다른 모듈
    import sub1
    sub1.sub1_function1()
    sub1.sub1_function2()

    # 모듈 이름을 생략한다.
    # 단, 같은 이름의 함수, 클래스등이 다른 모듈에는
    # 없어야 한다.
    # 지정된 모듈의 함수나 클래스 중에 일부를 생략하고
    # 사용하고 싶을 때...
    from sub2 import sub2_function1
    from sub2 import sub2_function2
    sub2_function1()
    sub2_function2()

    # 지정된 모듈의 함수나 클래스 모두를 생략하고
    # 사용하고 싶을 때
    from sub3 import *
    sub3_function1()
    sub3_function2()

    # 모듈명에 별칭을 부여한다.
    import iowjfidkshdf as iow

    iow.iow_function1()
    iow.iow_function2()

    # 다른 패키지의 모듈 사용
    # import pkg1.pkg1_sub1
    # pkg1.pkg1_sub1.pkg1_sub1_function1()
    # pkg1.pkg1_sub1.pkg1_sub1_function2()

    # 별칭 사용
    # import pkg1.pkg1_sub1 as ab
    # ab.pkg1_sub1_function2()
    # ab.pkg1_sub1_function2()

    # 패키지 생략
    # from pkg1 import pkg1_sub1
    # pkg1_sub1.pkg1_sub1_function1()
    # pkg1_sub1.pkg1_sub1_function2()

    # 패키지명, 모듈명 생략
    # from pkg1.pkg1_sub1 import pkg1_sub1_function1, pkg1_sub1_function2
    # pkg1_sub1_function1()
    # pkg1_sub1_function2()

    # 모든 요소들을 사용하겠다..
    # from pkg1.pkg1_sub1 import *
    # pkg1_sub1_function1()
    # pkg1_sub1_function2()

    # 모든 모듈을 사용하겠다..
    # __init__.py 파일에 정의한 모듈만 가능하다.
    from pkg1 import *
    pkg1_sub1.pkg1_sub1_function1()
    pkg1_sub1.pkg1_sub1_function2()







