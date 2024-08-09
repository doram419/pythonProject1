def if_statement():
    """
    if ~ elif ~ else
    """

    """
    금액을 입력 받고
        금액이 10,000원 이상이면 by taxi
        금액이 2,000원 이상이면 by bus
        그 미만이면 on foot
    """
    money = int(input("얼마 가지고 있어? "))

    message = ""
    if(money >= 10000):
        message += "by taxi"
    elif(money >= 2000):
        message += "by bus"
    else:
        message += "on foot"

    print(message)

def cond_expr():
    """
    조건 표현식
    """
    money = int(input("얼마 가지고 있어? "))

    message = "by taxi" if money >= 10000 else "by bus" if money >= 2000 else "on foot"

    print(message)

def for_ex():
    """
    반복문 활용 패턴
    """
    # 기본적인 순회 : for 타겟변수 in 순차자료형
    for animal in ['cat', 'cow', 'dog', 'tiger']:   # 순차형의 length 만큼 순회
        print(animal, end=' ') 
    else:
        print()

    # 인덱스와 요소를 함께 받아올 경우 : enumrate 함수
    for index, color in enumerate(['red', 'blue', 'green', 'yellow', 'black', 'white']):
        print(index, color)

    # continue : 남아 있는 코드 실행 중단 -> 다음 번 루프
    # break : 반복 자체를 종료하고 바깥으로 이동

    # continue를 이용한 1 ~ 10까지 loop -> 짝수만 출력
    print("====== continue")
    for i in range(1, 11):
        if i % 2 != 0:
            continue
        print(i, end=' ')
    else:
        print()

    print("====== break")

    r1 = list(range(1, 12, 2))
    print("r1:", r1)
    r2 = r1 + [12, 13, 15]
    print("r2:", r2)

    # 리스트 내부에서 짝수를 찾으면 "찾았습니다" -> 루프 종료
    #                      못 찾으면 "짝수는 없습니다" 출력
    for i in r1:
        if(i % 2 == 0):
            print("짝수(%d)를 찾았습니다" % i)
            break # 루프 탈출
    else:
        print("짝수는 없습니다")

    for i in r2:
        if(i % 2 == 0):
            print("짝수(%d)를 찾았습니다" % i)
            break # 루프 탈출
    else:
        print("짝수는 없습니다")

    """
    while 반복 조건 : 
        반복 코드
        - 반복 조건 잘 제어해서 무한 루프에 빠지지 않도록 제어
    """

    # 연습 문제 1
    # 2단 ~ 9단까지
    # 2 x 2 = 4
    # 2 x 3 = 6
    # ...
    print("===== 연습 문제 1 : 구구단 출력하기")
    for i in range(2, 10):
        gugu = ["%d x %d = %2d" % (i, num, i*num) for num in range(1, 10)]
        print(gugu)
    else:
        print()

    # 연습문제 2
    # *
    # **
    # ***
    # ****
    # *****
    print("===== 연습 문제 2 : 별 만들기")
    star = str()
    for i in range(1,6):
        star += "*"
        print(star)
    else:
        print()

def list_comprehension():
    """
    리스트 내포
    Syntax: [표현식 for 타겟 in 순차자료형]
    """
    data = [1,2,3,4,5,6,7,8,9,10]
    # 내부 요소들을 2배한 새 리스트를 생성

    result = []
    for num in data:
        result.append(num * 2)

    print(data)
    print(result)

    result = [num * 2 for num in data]
    print(result)

    strings = ["a", "as", "bat", "cart", "dove", "python"]
    # 문자열 리스트에서 문자열의 길이 3 이상인 문자열 목록 만들기
    result = [word.upper() for word in strings if len(word) >= 3]
    print(result)

    # 1 ~ 100 정수 중 3의 배수만 뽑아서 새 리스트 생성
    hundredList = [num for num in range(1, 101) if num % 3 == 0]
    print(hundredList)


def set_comprehension():
    """
    세트 내포
    Syntax: {표현식 for 타겟 in 순차자료형}
    """
    strings = ["a", "as", "bat", "cart", "dove", "python"]

    # strings 리스트에서 각 단어의 길이를 set만들기
    lenStrings = {len(word) for word in strings}
    print(lenStrings)

def dict_comprehension():
    """
    딕셔너리 내포
    Syntax: {키표현식:값표현식 for 타겟변수 in 순차자료형}
    """
    strings = ["a", "as", "bat", "cart", "dove", "python"]
    #{"a":1, "as":2, ... ,"python":6}
    len_dict = {s:len(s) for s in strings}
    print(len_dict)


if __name__ == "__main__":
    # if_statement()
    # cond_expr()
    # for_ex()
    # set_comprehension()
    dict_comprehension()

