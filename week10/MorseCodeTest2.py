# 과제 : 모스 부호를 입력하여 자신의 이름름을 출력하기 

# 모스코드 테스트 프로그램2
# 설명 : 모스 부호를 입력하여 자신의 이름을 출력하기 (문자사이의 공백은 / 로 구분)
# 실행시 입력값 : -.- .. --  /  .--- .- . / -- .. -. 

from MorseCode import *
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()
    str = input("모스 부호 입력 (문자사이의 공백은 / 로 구분): ")
    words = str.strip().split(" / ") 

    print("Decoding (Tree): ", end='')
    for word in words:
        mlist = word.split()  
        for code in mlist:
            ch = decode(morseCodeTree, code)
            print(ch, end='')
        print(' ', end='')  
    print()

