class PriorityQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity       # 용량 (고정)
        self.array = [None] * capacity # 요소들을 저장할 배열
        self.size = 0                  # 요소의 수

    def isEmpty(self):
        return self.size == 0          # 공백의 조건

    def isFull(self):
        return self.size == self.capacity  # 포화상태 조건

    def enqueue(self, e):
        if not self.isFull():              # 포화가 아니면 삽입 가능
            self.array[self.size] = e      # 새로운 요소는 배열 맨 뒤에 추가
            self.size += 1                 # 삽입 후 size를 증가시킴

    def findMaxIndex(self):
        if self.isEmpty(): return -1
        highest = 0
        for i in range(1, self.size):
            if self.array[i] > self.array[highest]:  # 공백이 아니면 가장 큰 요소값이 높은 우선순위를 할당받음
                highest = i
        return highest

    def findMinIndex(self):
        if self.isEmpty(): return -1
        lowest = 0
        for i in range(1, self.size):
            if self.array[i] < self.array[lowest]:  # 공백이 아니면 가장 큰 요소값이 높은 우선순위를 할당받음
                lowest = i
        return lowest

    def dequeue(self):
        #highest = self.findMaxIndex()         # 우선순위가 가장 높은 요소 삭제
        highest = self.findMinIndex()         # 우선순위가 가장 높은 요소 삭제
        if highest != -1:
            self.size -= 1
            self.array[highest], self.array[self.size] = \
                self.array[self.size], self.array[highest]  # 두 요소를 서로 교환
            return self.array[self.size]      # 실제 제거하지 않고 SIZE만 줄여 논리적으로 제거

    def peek(self):
        highest = self.findMaxIndex()         # 배열에서 가장 높은 우선순위를 찾아 꺼내지는 않고 확인만 함
        if highest != -1:
            return self.array[highest]

    def __str__(self):
        return str(self.array[0:self.size])   # 문자열 반환 연산자 중복 함수
