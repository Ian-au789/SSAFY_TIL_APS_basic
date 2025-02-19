# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEk2yzq99ADFAVs&probBoxId=AZTP3wYKXqnHBIRD&type=USER&problemBoxTitle=%2802.13%29+Stack1-1&problemBoxCnt=5

import sys
sys.stdin = open('sample_input.txt')


def check_bracket(line):
    top = -1
    size = len(line)
    stack = [0]*size

    for i in range(size):
        if line[i] == "{" or line[i] == "(":           # push 구현
            top += 1
            if top == size:
                return 0
            else:
                stack[top] = line[i]

        elif line[i] == "}" or line[i] == ")":
            if top == -1:
                return 0

            if line[i] == "}":                        # 대괄호 소괄호 종류가 일치할 때만 pop
                if stack[top] == "{":
                    top -= 1
                else:
                    return 0

            else:
                if stack[top] == "(":
                    top -= 1
                else:
                    return 0

    if top == -1:
        return 1
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    input_line = list(input())
    print(f"#{t} {check_bracket(input_line)}")
