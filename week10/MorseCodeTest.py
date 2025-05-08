# 과제 : 모스 부호를 입력하여 자신의 이름을 출력하기 

# 모스코드 테스트 프로그램
# 설명 : 모스 부호를 입력하여 자신의 이름을 출력하기
# 실행시 입력값 : -.- .. -- .--- .- . -- .. -. 

from MorseCode import *
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()
    str = input("모스 부호 입력 (공백으로 구분): ")
    mlist = str.strip().split()    # 공백 기준 분할

    print("Decoding (Tree): ", end='')
    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end='')
    print()
