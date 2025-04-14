from PriorityQueue import PriorityQueue
# 원형 덱: 테스트 프로그램
if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue(34)
    q.enqueue(18)
    q.enqueue(27)
    q.enqueue(45)
    q.enqueue(15)

    print("PQueue:", q)
    while not q.isEmpty():
        #print("Max Priority =", q.dequeue())  # FindMaxIndex로 가장 큰 값의 인덱스를 찾아
        print("Min Priority =", q.dequeue())  # FindMaxIndex로 가장 큰 값의 인덱스를 찾아        
        print("PQueue:", q)
                                              # 그 값을 꺼내고 현재 큐 내 마지막 요소와 바꾸고 사이즈 감소
