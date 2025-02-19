# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14_DEKAJcCFAYD&probBoxId=AZTP3wYKXqnHBIRD&type=PROBLEM&problemBoxTitle=%2802.13%29+Stack1-1&problemBoxCnt=5

import sys
sys.stdin = open('input.txt')


def password(size, numbers):
    top = -1
    stack = [""]*size

    for i in range(size):
        if stack[top] != numbers[i]:
            top += 1
            if top == size:
                return -1
            else:
                stack[top] = numbers[i]

        else:
            if top == -1:
                return -1
            else:
                top -= 1

    return "".join(map(str, stack[:top+1]))


for t in range(1, 11):
    N, M = input().split()
    print(f"#{t} {password(int(N), list(map(int, M)))}")
