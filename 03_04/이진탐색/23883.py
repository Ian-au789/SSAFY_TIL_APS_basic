# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkIGsKB__HBINE&probBoxId=AZVjg-a6ABDHBITD&type=USER&problemBoxTitle=%2803.04%29+tree1&problemBoxCnt=4

import sys
sys.stdin = open("5176_input.txt")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    n = N//2
    numbers = [n for n in range(1, N+1)]
    root = numbers[n]

    queue = [[root, numbers]]
    n = N
    n -= 1
    while n > 0:
        queue.append([queue[0][1][len(queue[0][1][:len(queue[0][1]) // 2 - 1]) // 2], queue[0][1][:len(queue[0][1]) // 2]])
        n -= 1
        if n == 0:
            break
        queue.append([queue[0][1][queue[0][0] + len(queue[0][1][queue[0][0]:]) // 2], queue[0][1][queue[0][0]:]])
        n -= 1
        queue.pop(0)

    result = queue.pop()

    print(f"#{t} {root} {result[0]}")
