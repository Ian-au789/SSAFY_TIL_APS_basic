# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEk4KA69-gDFAVs&probBoxId=AZTP3wYKXqnHBIRD&type=USER&problemBoxTitle=%2802.13%29+Stack1-1&problemBoxCnt=5

import sys
sys.stdin = open('sample_input.txt')


def erase_same_letter(line):
    top = -1
    size = len(line)
    stack = [0]*size

    for i in range(size):
        if stack[top] != line[i]:                   # 새로운 입력값이 직전 입력과 다르면 push
            top += 1
            if top == size:
                return -1
            else:
                stack[top] = line[i]

        else:                                      # 새로운 입력값이 직접 입력과 같으면 pull
            if top == -1:
                return -1
            else:
                top -= 1

    return top + 1


T = int(input())
for t in range(1, T+1):
    input_line = list(input())
    print(f"#{t} {erase_same_letter(input_line)}")