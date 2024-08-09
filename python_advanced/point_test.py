from point import Point

def bound_instance_method():
    """
    bound instance method: 인스턴스에 직접 바인딩 된 메서드
    """
    p = Point() # Point 인스턴스 생성
    p.setX(10)
    p.setY(20)

    print(p.getX(), p.getY(), sep=",")

def unbound_instance_method():
    """
    Unbound method:
    클래스 메서드에 인스턴스 참조주소를 전달 우회 접근법
    """

if __name__ == "__main__":
    bound_instance_method()