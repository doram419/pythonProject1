from point import Point

def bound_instance_method():
    """
    bound instance method: 인스턴스에 직접 바인딩 된 메서드
    """
    p = Point() # Point 인스턴스 생성
    p.setX(10)
    p.setY(20)

    print(p.getX(), p.getY(), sep=",")

if __name__ == "__main__":
    bound_instance_method()