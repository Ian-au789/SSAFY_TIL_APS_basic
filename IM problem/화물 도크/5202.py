# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZT4zs56TIvHBIOK&probBoxId=AZT4yWiKS8vHBIOK&type=USER&problemBoxTitle=IM+대비하자%21&problemBoxCnt=6

import sys
sys.stdin = open("input.txt", "r")


def max_truck(schedule):
    size = len(schedule)
    working_time = []

    for work in schedule:
        working_time.append(work[1] - work[0])

    for i in range(size):
        min_idx = i
        for j in range(i+1, size):
            if working_time[min_idx] > working_time[j]:
                min_idx = j

        working_time[i], working_time[min_idx] = working_time[min_idx], working_time[i]
        schedule[i], schedule[min_idx] = schedule[min_idx], schedule[i]

    max_work = [schedule[0]]
    idx = 1

    while idx < size:
        for work in max_work:
            if schedule[idx][0] < work[0] < schedule[idx][1] or \
                    schedule[idx][0] < work[1] < schedule[idx][1] or\
                    work == schedule[idx]:
                check = 0
                break

            for m in range(2):
                if work[0] < schedule[idx][m] < work[1]:
                    check = 0
                    break
                else:
                    check = 1

            if check == 1:
                continue
            else:
                break

        if check == 1:
            max_work.append(schedule[idx])

        idx += 1

    return len(max_work)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        operation = list(map(int, input().split()))
        arr.append(operation)

    print(f"#{t} {max_truck(arr)}")
