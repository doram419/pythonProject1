def int_ex():
        print("============ 정수형 연습")
        
        a = 2024 #리터럴 선언
        b = int(2024) #타입 함수사용

        print(a, "is", type(a))
        print(b, "is", type(b))

        #2진, 8진, 16진 정수 표현 가능
        b = 0b1101 # 0b 2진수
        o = 0o23   # 0o 8진수
        x = 0xFF   # 0x

        print(b, o, x)

        # 파이썬 3에서는 int와 long 구분 없음
        # long형 데이터의 저장 크기 64bit 초과해서 적재할 수 있음
        i = 2 ** 2048
        print(i);
        print(i.bit_length())
        
        # 진법 변환 함수
        i = 48
        print(i, bin(i), oct(i), hex(i))

def float_ex():
    print("================= 실수형 연습")
    a = 3.14159 # 리터럴로 생성
    print(a, "is", type(a))
    print(isinstance(a, float)) #a는 float인가?

    b = float(3.0) # 타입 함수
    print(b, "is", type(b))
    print(isinstance(b, float)) #b는 float인가?

    print("a(", a, ")는 integer인가요? ", a.is_integer())
    print("b(", b, ")는 integer인가요? ", b.is_integer())
    
    # 지수 표기법도 확인이 가능하다. e는 에러가 아닌 표시법이다
    c = 3e3 #3 * 10 ** 3
    d = -2E-5 # -2 * 10 ** -5
    print(c, d)
    print("-2E-5 == -0.00002? ", -2E-5 == -0.00002)

def complex_ex():
    print("============= 복소수 연습")
    # 복소수의 생김새는 실수부 + 허수부j의 형태이다
    a = 4 + 5j
    print(a, "is", type(a))
    print(isinstance(a, complex))   #a는 복소수?
    
    b = 7 -2j
    print(a + b) #복소수는 산술 연산이 가능하다
    print("b의 실수부 : ", b.real)
    print("b의 허수부 : ", b.imag) #실수부와 허수부를 뽑아낼 수 있다
    print(a, "의 켤레 복소수는 ", a.conjugate()) #켤레 복소수

if __name__ == "__main__":
    # int_ex()
    # float_ex()
    complex_ex()

