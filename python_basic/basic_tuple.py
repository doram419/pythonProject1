def define_tuple():
    """
    튜플의 정의
    tuple: 리스트와 거의 동일, 변경 불가 자료형(immutable)
        len, 인덱싱, 슬라이싱, 연결, 반복, 포함 여부 확인 가능
        내부 요소 변경 불가
    """
    tp1 = () # 공튜플
    print("tp1 : ", tp1)
    print("tp1 type?? ", type(tp1))
    tp2 = tuple()   # 타입으로 형성한 공튜플, 다른 자료형에서 변환할 때 사용됨
                    # 데이터가 변경되지 않아야 하는 경우에 자주 사용
    print("tp2 : ", tp2)
    print("tp2 type?? ", type(tp2))
    tp3 = (1)   # 이건 튜플이 아니다
    print("tp3 : ", tp3)
    print("tp3 type?? ", type(tp3))
    tp4 = (1,)  # 이건 튜플이다. 요소가 1개일 경우 요소 뒤에 , 기입
    print("tp4 : ", tp4)
    print("tp4 type?? ", type(tp4))

def tuple_oper():
    """
    튜플 연산
    """
    tp = (1, 2, 3, 4, 5)
    # 튜플은 길이를 구할 수 있다
    print(tp, "LENGTH : ", len(tp))
    
    # 역방향 인덱싱 가능 
    print("tp[-1] : ", tp[-3])
    print("tp[-2] : ", tp[-2])
    print("tp[-3] : ", tp[-1])
    
    # 정방향 인덱싱 가능 
    print("tp[0] : ", tp[0])
    print("tp[1] : ", tp[1])
    print("tp[2] : ", tp[2])

    # 슬라이싱 : [시작경계:끝경계:[:간격]]
    slice = tp[1:4]
    print("slice : ", slice, "slice type?? : ", type(slice))
    slice = tp[:]   # 처음부터 생략 가능, 끝까지도 생략 가능 -> [:] -> 처음부터 끝까지라는 뜻
    print("slice = tp[:] >> ", slice)

    # 반복 *
    print("tp * 3 >> ", tp * 3)

    # 연결 +
    print("tp + (6,7,8,9,10) >> ", tp + (6,7,8,9,10))

    # 포함 여부 in, not in
    print("6 in tp? >> ", 6 in tp)
    print("61 not in tp? >> ", 61 not in tp)

def tuple_assign():
    """
    튜플의 할당
    """
    # 튜플을 이용, 좌우변의 여러 값을 동시 할당
    x, y, z = 10, 20, 30    # 튜플 
    fmt = "x : %d, y : %d, z : %d"
    print(fmt % (x, y, z))

    #튜플을 이용한 swap(값 교환)
    x, y = 10, 20
    print(x, y)
    x,y = y, x # 튜플을 이용한 교환
    print(x, y)

def tuple_method():
    """
    튜플의 메서드들
    """
    tp = (20, 30, 10, 20)
    print("count:", tp.count(20))   # 요소 갯수
    print("index:", tp.index(20))   # 요소의 인덱스
    print("index:", tp.index(20, 1))   # 요소의 인덱스, 범위 제한

def packing_unpacking():
    """
    튜플 패킹과 언패킹
    """
    tp = (10, 20, 30, "Python") # 기본적으로 튜플 생성법
    print(tp, type(tp))
    tp = 10, 20, 30, "Python"   # 값만 나열해도 자동으로 튜플로 인식
    print(tp, type(tp))

    # 기본 unpacking
    a, b, c, d = tp
    print(a, b, c, d)

    # a, b, c = tp  # 좌변의 개수가 튜플의 개수보다 적으면 -> ValueError
    # a, b, c, d, e = tp                        # 많으면.. -> ValueError

    # 확장 언패킹
    a, *b = tp  # a 한 개 할당, 나머지는 b에 할당한다는 뜻 * 
    print(a, type(a))
    print(b, type(b))

    *a, b = tp
    print(a, type(a))
    print(b, type(b))

    a, *b, c = tp
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))

if __name__ == "__main__" :
    # define_tuple()
    # tuple_oper()
    # tuple_assign()
    # tuple_method()
    packing_unpacking()