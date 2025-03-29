capacity = 5 # 전역 변수
array = [None] * capacity # 전역 변수
size = 0 # 전역 변수 

def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환 

def insert(pos, e):
    global size  # size는 전역변수
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]  # 한 칸씩 뒤로 옮김
        array[pos] = e
        size += 1  # 요소의 수가 하나 증가
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

if __name__ == "__main__":
    print("초기 size 변수의 값은", size)
    print("초기 capacity 변수의 값은", capacity) 
    print("=======================================") 

    # insert함수 호출 1
    insert(0, 10)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity])
    print("=======================================") 

    # insert함수 호출 2
    insert(0, 20)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity])
    print("=======================================") 

    # insert함수 호출 3
    insert(1, 30)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity]) 
    print("=======================================") 

    # insert함수 호출 4
    insert(2, 40)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity]) 
    print("=======================================") 

    # insert함수 호출 5
    insert(3, 50)
    print(f"현재 size변수 값은 {size}이고, size와 capcaity 비교 결과는 {isFull()} 이다.")
    print("현재 array", array[0:capacity])
    print("=======================================") 
