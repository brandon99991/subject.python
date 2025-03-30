capacity = 100
array = [None]*capacity
size = 0

# 리스트의 연산: 일반 함수
def isEmpty():
    if size == 0:
        return True  # 공백이면 True 반환
    else:
        return False  # 아니면 False 반환

def isFull():
    return size == capacity  # 비교 연산 결과를 바로 반환

def getEntry(pos):
    if 0 <= pos < size:
        return array[pos]  # 유효한 인덱스라면 해당 요소 반환
    else:
        return None  # 유효하지 않으면 None 반환

def insert(pos, e):
    global size  # size는 전역변수
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]  # 한 칸씩 뒤로 옮김
        array[pos] = e  # pos위치에 새로운 요소 추가
        size += 1  # 요소의 수가 하나 증가
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

def delete(pos):
    global size  # size는 전역변수
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size-1):
            array[i] = array[i+1]  # 한 칸씩 앞으로 당김
        size -= 1  # 요소의 수가 하나 감소
        return e
    else:
        print("리스트 underflow 또는 유효하지 않은 삭제 위치")
        exit()

if __name__ == "__main__":
    print("최초       ", array[0:size])

    insert(0, "안녕하세요")
    insert(1, "저는")
    insert(2, "AAA")
    insert(3, 1111111)
    insert(4, "홍길동입니다.")
    print("삽입x5     ", array[0:size])

    delete(0)
    print("삭제       ", array[0:size])

    delete(1)
    print("삭제       ", array[0:size])

    delete(0)
    print("삭제(0)    ", array[0:size])
