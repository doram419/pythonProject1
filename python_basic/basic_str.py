def define_str() : 
    """
    함수 정의 연습
    """
    # 문자열의 정의
    # 한 줄 문자열: 쌍따옴표("), 홑따옴표(') 모두 가능하다
    s1 = "Hello Python" # 리터럴로 생성 가능
    s2 = str("Hello Type String")  # 타입 함수 사용
    s3 = str(3.14159) # 다른 타입을 변환 생성
    print("s1 : ", s1)
    print("s1의 type :", type(s1))
    print("s2 : ", s2)
    print("s2의 type :", type(s2))
    print("s3 : ", s3)
    print("s3의 type :", type(s3))

    print("s1은 str? ", isinstance(s1, str))

    # 여러 줄 문자열: """, '''
    s4 = """Life could be dream, Life coulde be dream
        do lat lat do lat do
        파이썬은 데이터 처리가 중요한 시대에서
        가장 널리 사용 되는 언어입니다
        """
    
    print(s4)

    # 여러 줄 문자열은 한 줄 주석만 있는 파이썬에서
    # 여러 줄 주석을 사용하고자 할 때도 사용 할 수 있다.
    """여러 줄 문자열을 사용한 여러 줄 주석
    메서드 정의 바로 아래 여러 줄 주석을 추가하면
    문서화할 때 이용될 수 있고
    help 명령어로 해당 메서드의 주석을 볼 수 있다
    이런 걸 docstring 이라고 한다"""

    # f-string : 문자열 포맷팅 방식 중 하나
    name, age = "홍길동", 28
    message = f"안녕하세요, {name}님. 당신은 {age}살입니까?"
    print(message)

    width, height = 10, 5
    message = f"사각형의 면적은 {width * height}입니다"
    print(message)

def string_open():
    """
    문자열 연산
    """
    str1 = "First String"
    str2 = "Second String"
    # len(), 인덱싱 가능, 슬라이싱 가능, 포함 여부 판별
    # immutable, 치환 불가능
    print("문자열 " + str1 + "의 길이 : ", len(str1))
    print("문자열 " + str2 + "의 길이 : ", len(str2))
     # 길이

    # 인덱싱
    print(str1[0], str1[1], str1[2], "...", str1[9], str1[10], str1[11])
    print(str1[-12], str1[-11], str1[-10], "...", str1[-3], str1[-2], str1[-1])

    # 문자열은 immutable -> 치환 불가
    # str1[0] = "f" # 변경 불가

    # 슬라이싱 
    # [시작경계:끝경계:간격]
    print(str1)
    print(str1[6:9]) # 정방향 인덱스 활용
    print(str1[-6:-3]) # 역방향 인덱스 활용

    print(str1[0:5])
    print(str1[:5]) # 시작부터 -> 생략 가능

    print(str1[6:len(str1)])
    print(str1[6:]) # 끝까지 -> 생략 가능

    print(str1[::2]) # 처음부터 끝까지 간격 2
    print(str1[::-1]) # 간격 값이 음수 -> 역방향
    
def transform_methods() :
    """
    대소문자 변환 관련 연습
    """
    s = "i like python"

    print("UPPER: ", s.upper()) # 모두 대문자
    print("LOWER: ", s.lower()) # 모두 소문자로
    print("CAPITALIZE: ", s.capitalize())   # 첫 글자만 대문자로
    print("TITLE: ", s.title())   # 각 단어의 첫 글자만 대문자로

    print("SWAPCASE: ", s.title().swapcase())   #대 <-> 소

    # 불변 자료 -> 원본은 바뀌지 않는다
    print("원본 : ", s)

def search_methods() :
    """
    문자열 검색 관련 예제
    """
    s = "I Like Python, I Like Java Also"
    print("COUNT:", s.count("Like"))    # 문자열 내부의 Like 함수

    # Like을 찾아봅시다
    index = s.find("Like") # 문자열 내부에서 첫번째 Like
    print("1st find : ", index)
    index = s.find("Like", 6) # 인덱스 6부터 검색
    print("2nd find : ", index)
    index = s.find("Like", 21) # 인덱스 6부터 검색
    print("3rd find : ", index)

    # Like을 찾아봅시다 : index
    print("1st Index:", s.index("Like"))
    print("2nd Index:", s.index("Like", 6))
    # print("2nd Index:", s.index("Like", 21))
    # 방법 1: 예외 처리
    # 방법 2: 먼저 검색어 포함 여부를 확인 후 검색
    if "Like" in s[21:]:
        # 포함 여부
        print("3rd Index: ", s.index("Like", 21))
    else:
        print("21번 인덱스 이후에는 Like 없음")
        
    # 역방향 검색 : find
    print("RFIND ", s.rfind("Like"))
    print("RFIND ", s.rfind("Like", 0, 17))

    # 문자열이 특정 문자열로 시작되는가?
    url = "http://www.naver.com"
    surl = "http://www.google.com"
    ftp = "ftp://ftp.naver.com"

    print("url STARTSWITH(http): ", url.startswith("http"))
    print("surl STARTSWITH(http): ", surl.startswith("http"))
    print("ftp STARTSWITH(http://, https://): ", ftp.startswith(("http://", "https://"))) # 검색 대상이 여러 개이면 튜플로 적기

    # 문자열이 특정 문자열로 끝나는가?
    print("url ENDSWITH(naver.com)", url.endswith("naver.com"))
    print("surl ENDSWITH(naver.com)", surl.endswith("naver.com"))
 
    # startswith, endswith에서 검색 범위를 제한
    # 기본적으로 우리 프로그래밍의 변수 값이 어떤 값인지 모른다를 가정으로 만들어야한다
    print("startswith(ftp, 6, len(ftp)): ", ftp.startswith("ftp.", 6, len(ftp)))

def modify_replace_methods():
    """
    문자열 수정. 치환 관련 메서드 연습
    """
    s = "               Alice and the Heart Queen                     "
    print("s : ", s)
    print("s STRIP: [", s.strip(), "]" , sep="")
    # python은 separator와 ender 존재, 명시하지 않으면 sep=" ", end="\n"
    print("s LSTRIP: [", s.lstrip(), "]" , sep="")
    print("s RSTRIP: [", s.rstrip(), "]" , sep="")

    s = "------------------------Alice and the Heart Queen----------------------------------"
    print("-s- : ", s)
    print("-s- STRIP: [", s.strip("-"), "]" , sep="")

    s = "I Like Java"
    print("s : ", s)
    print("Java to Python with REPLACE : ", s.replace("Java", "Python"))
    print("원본:", s) # str은 immutable -> 변경되지 않는다

def align_methods():
    """
    문자열 정렬 관련 메서드
    """
    s = "Alice and the Heart Queen"

    print("s : ", s)
    print("s CENTER : [", s.center(60), "]", sep="")
    print("s CENTER place * : [", s.center(60, "*"), "]", sep="")
    print("s RJUST place * : [", s.rjust(60, "*"), "]", sep="")
    print("s LJUST place * : [", s.ljust(60, "*"), "]", sep="")
    print("ZFILL 1234 : ", "1234".zfill(5))  # 5자리 확보, 내용을 채운 후 빈 공간에 0으로 채움
    print("ZFILL 123456 : ", "123456".zfill(5))  # 확보한 5자리는 최소 공간, 넘쳐도 잘리지는 않는다

def programmers1():
    num1 = 100
    num2 = 20
    result1 = num1 / num2
    result2 = num1 // num2
    result3 = num1 % num2
    result4 = divmod(num1, num2)
    print("num1 / num2 : ", result1)
    print("num1 // num2 : ", result2)
    print("num1 % num2 : ", result3)
    print("divmod(num1, num2) : ", result4)
    print("divmod[0] : ", result4[0])
    print("divmod[0:] : ", result4[0:])
    print("divmod[1] : ", result4[1])
    print("divmod[1:2] : ", result4[1:2])

def split_join_method():
    """
    문자열 분할과 합치기 관련 메서드
    """
    s = "Ham and Cheese and Breads and Ketchup"
    print("s : ", s)
    print("split() : ", s.split())    # split은 공백을 기준으로 리스트로 분리한다
    
    ingr = s.split(" and ")
    print("split( and ) : ", ingr) 
    print("JOIN:", ", ".join(ingr))  #ingr리스트를 , 를 중심으로 합침

    print("s.split(2) : " ,s.split(" and ", 2))  # 앞에서 2개만 분리
    print("s.rsplit(2) : " ,s.rsplit(" and ", 2))  # 뒤에서 2개만 분리

    # 줄 단위 구분 : split("\n")과 동일
    # \ (역슬래시의 기능?) : \n을 무시하게 해줌
    lines = """\
    Java Programming
    Python Programming
    HTML Coding
    """
    print("split : ", lines.split())
    print("split(n) : ", lines.split("\n"))

    print("splitlines(True) : ", lines.splitlines(True))  # 개행문자 유지
    print("splitlines(False) : ", lines.splitlines(False))  # 개행문자를 유지하지 않음
    
def programmers2():
    a = 100
    b = 99
    c = 100
    print("a : ", a, " b : ", b, " c : ", c)
    print("a is b : ", a is b)
    print("a is c : ", a is c)
    print("b is c : ", b is c)
    print("a == b : ", a == b)
    print("a == c : ", a == c)
    print("b == c : ", b == c)

def check_methods():
    """
    str 데이터의 형태 판별
    """
    print("1234.isdigit? : " , "1234".isdigit()) # 숫자 형태인가?
    print("abcd.isalpha? : " , "abcd".isalpha()) # 알파벳 형태인가?
    print("python3.isalnum? : " , "python3".isalnum()) # 알파벳 + 숫자 형태인가?
    print("Python 3.isalnum? : " , "Python 3".isalnum()) # 알파벳 + 숫자 형태인가?
    print("\\r\\n\\t.isspace? : " , "\r\n\t".isspace()) # 공백 문자 형태? 스페이스, 개행문자, 탭 등 모두 공백 문자
    print(".isspace? : " ,"".isspace())

    print("PYTHON.isupper? : " ,"PYTHON".isupper())
    print("python.islower? : " ,"python".islower())
    print("Python Programming.istitle? : " ,"Python Programming".istitle())

def string_format():
    """
    문자열 포맷팅 연습
    """
    # c 스타일 문자열 포맷
    # %s, %c, %d, %f, %x, %o, %%
    fmt = "%d개의 %s 중에서 %d 개를 먹었다"
    print("fmt : ", fmt)
    print(fmt % (10, "사과", 3))

    print("현재 이자율은 %f%%입니다." % 3.4)
    print("현재 이자율은 %.2f%%입니다." % 3.4)

    # named formatting
    fmt = "%(total)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다"
    print("fmt : ", fmt)
    print("fmt : ", fmt % {"total":10, "fruit":"사과", "eat":5})
    print("fmt : ", fmt % {"fruit":"배", "eat":7, "total":20})

    # format 메서드
    fmt = "{}개의 {}중에서 {}개를 먹었다"
    print("fmt : ", fmt)
    print("placeholder fmt : ", fmt.format(77, "파인애플", 4))
    fmt = "{0}개의 {1}중에서 {2}개를 먹었다"
    print("placeholder with index : ", fmt.format(90, "망고", 44))

    # placeholder의 named parameter를 이용하는 방법
    fmt = "{total}개의 {fruit}중에서 {eat}개를 먹었다"
    print("placeholder with name : ", fmt.format(eat=3, total=9, fruit="라즈베리"))
    
    # dict로 작성된 데이터가 있을 경우
    data = {"total":10, "eat":8, "fruit":"멜론"}
    print("placeholder with format_map : ", fmt.format_map(data))

    # f-string
    # 포맷팅 문자열 앞에 f
    # {} 내부에 데이터, 변수명, 표현식 -> 해당 결과 바인딩 -> 최종 출력물
    total, fruit, eat = 10, "사과", 3
    print(f"{total}개의 {fruit} 중에서 {eat} 개를 먹었다")
    # 플레이스 홀더 내부에 연산식 활용 가능
    total, fruit, eat = 10, "apple", 3
    print(f"{total}개의 {fruit.upper()} 중에서 {eat} 개를 먹어서 {total - eat}개가 남았다")
 
if __name__ == "__main__":
    # define_str()
    # string_open()
    # transform_methods()
    # search_methods()
    # modify_replace_methods()
    # programmers1()
    # align_methods()
    # split_join_method()
    # check_methods()
    string_format()
    
