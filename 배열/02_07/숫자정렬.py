# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PrmyKAWEDFAUq&probBoxId=AZTP3wYKXqXHBIRD&type=PROBLEM&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("input.txt", "r")


def sort_number(length, num_list):
    sort_list = []
    idx = 0

    while idx < length:                       # idx가 입력 리스트 길이에 도달할 때 까지
        for num in num_list:
            if num == min(num_list):          # 리스트 내 최솟값 탐색
                sort_list.append(num)         # 순서 정렬 리스트에 투입
                num_list.remove(num)          # 기존 리스트에서는 제거
        idx += 1

    return sort_list


T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = " ".join(map(str, sort_number(N, numbers)))
    print(f"#{t} {result}")
