def dummy():
    # 함수 구현부가 없어도 비워두면 안 되다
    pass

def times(a, b):
    return a * b

# 매개변수의 유무, 출력의 유무
# return 문
#   기본적으로 함수를 종료하고 함수 호출 지점으로 돌아감
#   돌려줄 출력이 있을 때도 return 뒤에 데이터를 명시

def none():
    return # 출력 없이 return 문만 썻었을 떄는 None

print(none())
#함수도 객체
# 다른 객체들과 동등한 권한를 갖는다.
# - 변수에 할당 될 수 있고
# - 다른 함수의 매개변수로 전달 될 수 있고
# - 함수의 결과를 반환 될 수 있음

fun = times #변수에 할당
print(fun, type(fun))
#실행 가능 객체인지를 확인 -> Callable
print(callable, 20)
if callable(fun):
    print(fun(10, 10))

if __name__ == "__main__":
    dummy()
    times()
