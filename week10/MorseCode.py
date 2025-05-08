# 모스 코드 표와 인코딩 알고리즘
table = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'),    ('F', '..-.'), ('G', '--.'),  ('H', '....'),
    ('I', '..'),   ('J', '.---'), ('K', '-.-'),  ('L', '.-..'),
    ('M', '--'),   ('N', '-.'),   ('O', '---'),  ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..'),  
]

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

# 모스코드 디코딩(순차탐색)
def decode_slow(code):
    for e in table:
        if code == e[1]:
            return e[0]
    return None

class TNode:
    def __init__(self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right

# 모스 코드 결정 트리 만들기
def make_morse_tree():
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1]           # 모스 코드
        node = root
        for c in code:         # 모스 코드의 각 부호에 대해
            if c == '.':       # 점(.)이면 왼쪽으로 이동
                if node.left == None:      # 비었으면 빈 노드 만들기
                    node.left = TNode(None, None, None)
                node = node.left           # 노드가 있었다면 그쪽으로 이동
            elif c == '-':     # 선(-)이면 오른쪽으로 이동
                if node.right == None:     # 비었으면 빈 노드 만들기
                    node.right = TNode(None, None, None)
                node = node.right          # 노드가 있었다면 그쪽으로 이동
        node.data = tp[0]      # 코드의 알파벳
    return root

def decode(root, code):        # 결정트리를 이용한 디코딩 함수
    node = root
    for c in code:             # 맨 마지막 문자 이전까지 --> 이동
        if c == '.':           # 점(.)이면 왼쪽으로 이동
            node = node.left
        elif c == '-':         # 선(-)이면 오른쪽으로 이동
            node = node.right
    return node.data           # 문자 반환
