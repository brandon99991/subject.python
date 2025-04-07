from ArrayStack import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)  # 용량이 100인 스택 객체 생성
    for ch in statement:     # statement의 각 문자를 순서대로 ch에 대입
        # if ch in ('{', '[', '('):
        # if ch in '{{[(':
        if ch == '{' or ch == '[' or ch == '(':
            stack.push(ch)  # ch가 열리는 괄호이면 스택에 삽입
        # elif ch in ('}', ']', ')'):
        # elif ch in '}]':
        elif ch == '}' or ch == ']' or ch == ')':  # 닫히는 괄호인지 검사
            if stack.isEmpty():    # 스택이 공백이면 조건 2 위반반
                return False
            else:
                left = stack.pop()  # 스택에서 괄호를 꺼내 ch와 짝이 맞는지 비교
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "("):
                    return False

    return stack.isEmpty()  # 스택이 공백이 아니면 조건 1 위반

# 괄호 검사를 할 대상 파일
filename = "kjmtest.py"

with open(filename, "r", encoding="utf-8") as infile:
    str = infile.read()
    print("소스파일", filename, " ---> ", checkBrackets(str))
