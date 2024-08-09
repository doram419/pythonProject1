import sys

def sys_module():
    # argv 속성: 명령행에서 넘어온 인수
    # print(sys.argv) # 0번 인덱스는 스트립트명

    args = sys.argv[1:] # 스크립트를 제외한 인수
    print(sys.argv)

    # 시스템 관련 정보
    print("Platform:", sys.platform)
    print("Version:", sys.version)

    # 파이썬은 모듈 검색할 때, sys.path에 등록된 디렉토리를 대상으로 검색
    print("모듈 검색 경로: ", sys.path)
    # 찾는 모듈이 sys.path 에 없을 때
if __name__ == "__main__":
    sys_module()
