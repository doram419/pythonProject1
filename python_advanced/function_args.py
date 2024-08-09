# 함수의 매개 변수
# 기본적으로 필요한만큼 선언할 수 있다

# 기본적인 형태의 함수
def sum_val(a, b):
    return a + b

def incr(a, step=1): # 두번째 인수(step은 기본 값이 있다)
    return a + step

print("sum_val(2, 3) : ", sum_val(2, 3)) #순서대로 a=2, b=3으로 전달됨
print("incr(10) : ", incr(10)) # incr()에 두번째 파라미터가 오지 않으면 기본값을 씀
print("incr(10, 20) : ", incr(10, 20)) # 기본값 무시하고 값을 부여하면 그 값이 활용됨

# 키워드 인수
def area(width, height):
    return width * height

print("area(10, 20) : ", area(10, 20)) # 설계된 매개변수 순서대로 호출
print("area(height=30, width=40) : ", area(height=30, width=40))    #혹은 매개변수 순서와 상관없이 이름으로 전달가능
print("area(width=40, height=30) : ", area(width=40, height=30))    

# 가변 인수 : 정해지지 않은 수의 매개변수 -> 매개변수 앞에 *
def get_total(*args):   # args -> 정해지지 않은 개수의 매개변수
    total = 0 
    for x in args:
        total += x
    return total

print(get_total(1,3,5,7,9))
print(get_total(3,6,9,12,15))

# 키워드 인수 : **
# 함수에 고정인수, 가변인수, 키워드 인수
# 선언부에 고정인수, 가변인수, 키워드 인수 순서로 선언

def func_args(a,b, *args, **kwargs):
    print("고정인수:", a,b)
    print("가변인수:", args, type(args))
    print("키워드인수:", kwargs, type(kwargs))

func_args(10, 20, 30, 40, 50, 60, 70, 80, 90, option1="test", option2="kwargs")

print("----------------------------")

# 함수도 객체다 -> 함수의 인수로 전달될 수 있다

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def calculator(a, b, func): # func -> 함수
    if callable(func): #넣어온 매개변수가 실행 가능 객체인지 확인
        return func(a, b)
    
print(calculator(3, 7, plus))
print(calculator(3, 7, minus))

# 1회성으로 로직 전달하고자 할 때
# 익명 함수 lambda 함수를 전달해 줄 수 있다

def clean_strings(strings, *funcs):
    results = list()
    for s in strings:
        for func in funcs:
            if callable(func) : # 넘어온 인자가 실행 가능 객체
                s = func(s)
        results.append(s)

    return results

dirty_strings = "python pRoGrAmInG, jAvA pROGraminG, lInUX, wInDoWs".split()
print(dirty_strings)
cleaned = clean_strings(dirty_strings, str.strip, str.title)
print(cleaned) 

# lambda : 익명 함수
# 익명 함수를 이용한 키 함수 정의
strings = "Life is too short, you need Python".replace(",","").lower().split()
print("strings:", strings)

# 문자열 길이 순으로 정렬
sorted_str = sorted(strings, key=lambda x: len(x))
print(sorted_str)