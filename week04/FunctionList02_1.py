capacity = 5                        # 전역 변수
array = [None]*capacity              # 전역 변수
size = 0                             # 전역 변수

# 리스트의 연산: 일반 함수
def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환

def insert(pos, e):
    global size  # size는 전역변수
    if not isFull():
        array[pos] = e
        size += 1  # size변수의 값에 +1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

# 프로그램의 시작
if __name__ == "__main__":
    print("(초기값) 현재 size 변수의 값은 ? ", size)   
    print("(초기값) 현재 capacity 변수의 값은 ? ", capacity)   
    print("----------------------------------------------------")   

    # insert함수 호출 1
    insert(0, 10)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 2
    insert(1, 20)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 3
    insert(2, 30)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 4
    insert(3, 40)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   

    # insert함수 호출 5
    insert(0, 50)
    print("현재 array", array[0:capacity])
    print("----------------------------------------------------")   
