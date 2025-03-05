# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkJECaCGfHBINE&probBoxId=AZVjg-a6ABHHBITD&type=USER&problemBoxTitle=%2803.05%29+tree2&problemBoxCnt=3

import sys
sys.stdin = open("5177_input.txt")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_heap = [-1]
    idx = 0
    for n in numbers:
        min_heap.append(n)
        idx += 1

        if min_heap[idx // 2] <= min_heap[idx]:
            continue

        else:
            check = idx
            while min_heap[check // 2] > min_heap[check]:
                min_heap[check // 2], min_heap[check] = min_heap[check], min_heap[check // 2]
                check //= 2

    result = 0
    while idx > 1:
        idx //= 2
        result += min_heap[idx]

    print(f"#{t} {result}")
