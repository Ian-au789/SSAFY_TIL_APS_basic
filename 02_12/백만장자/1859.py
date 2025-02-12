# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5LrsUaDxcDFAXc&probBoxId=AZTP3wYKXqjHBIRD&type=PROBLEM&problemBoxTitle=%2802.12%29+String-2&problemBoxCnt=4

import sys
sys.stdin = open("input.txt", "r")


def max_profit(future, prices):
    size = len(prices)
    profit = 0

    now_max = max(prices[1:future])                     # 탐색 전 최댓값 확인

    for i in range(size-1):
        if i <= size-future:                            # 탐색하는 범위가 리스트의 마지막에 도달할 때 까지
            now_max = max(now_max, prices[i+future-1])  # 새로 탐색 범위에 들어오는 항목과 현재의 최댓값 비교해서 갱신
            if prices[i] < now_max:
                profit += now_max - prices[i]           # 오늘의 가격과 미래의 최대 가격의 차이 만큼 이윤 발생

            elif prices[i] == now_max:
                now_max = max(prices[i+1:i+future])     # 최댓값이 갱신되지 않고 탐색 범위를 벗어나면 최댓값 다시 구하기

        else:
            if prices[i] < now_max:                     # 탐색할 항목이 더 늘어나지 않음
                profit += now_max - prices[i]
            elif prices[i] == now_max:                  # 최댓값이 탐색 범위를 떠날 때만 고려
                now_max = max(prices[i+1:size])

    return profit


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_list = list(map(int, input().split()))

    print(f"#{t} {max_profit(N, input_list)}")
