def write_file():
    """
    파일을 열어서 파일에 텍스트 저장
    : 문장 1개 -> ./sample/test.txt 기록
    : open(파일명, 파일모드, encoding)
    : 액션모드 : r(read: default) w(write), a(append)
    : 형식모드 : t(text: default) b(binary)
    """
    f = open("./sample/test.txt", "w", encoding="UTF-8")  # ("./sample/test.txt", "wt", "UTF-8")인데 디폴트라서 생략 가능
    write_size = f.write("Life is too short, you need Python")   # 기록한 콘텐츠의 길이 반환
    print("기록된 컨텐츠 길이 : ", write_size)
    f.close()

def write_file2():
    """
    여러 줄의 ./sample/multilines.txt
    """
    f = open("./sample/multiLine.txt", "w" , encoding="UTF-8")
    for i in range(1, 11):
        f.write(f"Line {i}\n")
    f.close()

def read_file():
    """
    ./sample/multiLine.txt" 읽어오기 
    """
    f = open("./sample/multiLine.txt", encoding="UTF-8")
    text = f.read() # 컨텐츠 전체 -> 내용이 많을 때 부하가 걸릴 수 있음
    print(text)
    f.close()

def read_file_by_line():
    """
    줄 단위로 읽어와서 메모리에 부하 줄이기
    """
    f = open("./sample/multiLine.txt", encoding="UTF-8")
    while True:
        line = f.readline() # 한 줄 읽기
        if not line: # 더 읽어올 것이 있는가?
            break
        print(line)

    f.close()

# def read_file_readline():
#     with open("./sample/multiLine.txt", "rt", encoding="UTF-8") as f:
#         #print(lines)
#         for line in lines:
#             print(line.strip())

def copy_binary_file():
    """
    이전 파일을 읽거나 쓰기 위해서는 모드를 b로 설정
    : ./sample/rose-flower.jpeg - ./sample/rose-flower-copy.jpeg로 복사
    """
    # 읽어들이기
    with open("./sample/rose-flower.jpeg", "rb") as f:
        data = f.read()
        print(type(data), "LENGTH:", len(data))

    # 저장하기
    with open("./sample/rose-flower-copy.jpeg", "wb") as f:
        f.write(data)

import pickle
def serialize():    # 직렬화
    """
    pickle 모듈의 dump 메소드 직렬화
    """

    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball", 9}, f, 1) # dump(객체, 파일포인터, 프로토콜 버전
        pickle.dump({"basketball", 5}, f, pickle.HIGHEST_PROTOCOL) # 최신 파일 버전
        pickle.dump({"soccer", 11}, f)
    print("직렬화 완성")

def deserialize():  # 역직렬화
    """
    피클 역직렬화 load, 프로토콜 버전은 명시하지 않아도 됨
    """

    data_list = list()

    with open("./sample/players.bin", "rb") as f:
        # print(pickle.load(f))
        # print(pickle.load(f))
        # print(pickle.load(f))
        while True: # 몇 개인지 모르기 때문에 루프
            try:
                data = pickle.load(f)
                data_list.append(data)
            except EOFError:    # 피클이 없음
                break
        

    print("역직렬화 결과 ", data_list)

"""
연습문제
- sangbuk.csv -> 읽어서
- ,를 기준으로 분할
- 한 개의 레코드를 딕셔너리로 만들기
    예: {"name":채치수, "backNo":4, "height":197, "position":센터}
- sanbuk-players.bin -> pickle로 dump
"""
import csv

def pickle_practice():
    save_list = list()
    with open("./sample/sangbuk.csv", "r", encoding="UTF-8") as f:
        try:
            reader = csv.reader(f)

            for line in reader:
                cucumber = {"name":line[0], "backNo":line[1], "height":line[2],"position":line[3]}
                save_list.append(cucumber)
        except Exception as e:
            print(e)

    with open("./sample/sanbuk-players.bin", "wb") as f:
        try:
            for cucum in save_list:
                pickle.dump(cucum, f, 1)
            else:
                print("쓰기 완료")
        except Exception as e:
            print(e)

def check_pickle_practice():
    with open("./sample/sanbuk-players.bin", "rb") as f:

        while True: # 몇 개인지 모르기 때문에 루프
            try:
                data = pickle.load(f)
                print(data)
            except EOFError:    # 피클이 없음
                break

                    
if __name__ == "__main__":
    # write_file()
    # write_file2()
    # read_file()
    # read_file_by_line()
    # copy_binary_file()
    # serialize()
    # deserialize()
    # pickle_practice()
    check_pickle_practice()
