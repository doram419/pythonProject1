def define_dict():
    """
    dict 정의
    """
    dct = dict()    # 빈 dict
    print(dct, type(dct))
    dct = {}        # 빈 dict
    print(dct, type(dct))

    # 키워드 인수로 생성
    dct = dict(one=1, two=2)
    print(dct, type(dct))

    #키, 값 쌍 튜플의 목록으로 생성
    dct = dict([("one", 1), ("two", 2), ("three", 3)])
    print(dct, type(dct))

    # 키 목록과 값 목록이 별도로 있을 때 두 목록을 합쳐서 dict 생성
    keys = ('one', 'two', 'three', 'four')
    values = (1, 2, 3)
    dct = dict(zip(keys, values))   # 키 목록과 값 목록을 합쳐서 dict에 전달, 그러나 쌍이 없으면 패스
    print(dct, type(dct))

def dict_oper():
    """
    dict의 연산
    키를 통한 접근, 가변 자료형
        len, in, not in
        기본적 연산 대상은 keySet
    """

    dct = {"baseball":9, "basketball":5}
    # 키를 통한 접근
    dct['soccer'] = 11

    print(dct, type[dct])

    # 순서가 없음 : 인덱싱, 슬라이싱 불가
    # 길이, 포함 여부 확인 가능
    print(dct, "LENGTH:", len(dct))
    print("baseball" in dct)
    print("soccer" in dct)
    print("volleyball" in dct)

    # 포함 여부를 값 목록에서 확인할 경우 .values()
    print(9 in dct.values())

    # .keys() : key set을 받아 올 수 있음
    # .values() : value 목록을 받아올 수 있음
    # .items() : (키, 가방) 목록을 받아올 수 있음

def loop():
    """
    사전의 순회(loop) : keySet 대상
    """
    phones = {
        "둘리":"010-1234-5678",
        "도우너":"010-9876-5432",
        "또치":"010-2222-3333"
    }

    # 기본적인 루프
    for key in phones:
        print(f"{key}: {phones.get(key)}")

    for key in phones.keys():
        print(f"{key}: {phones.get(key)}")

    print("items:", phones.items())
    for key, value in phones.items():
        print(f"{key}:{value}")

if __name__ == "__main__":
    # define_dict()
    # dict_oper()
    loop()