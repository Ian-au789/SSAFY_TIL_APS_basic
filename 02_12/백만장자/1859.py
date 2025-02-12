# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5LrsUaDxcDFAXc&probBoxId=AZTP3wYKXqjHBIRD&type=PROBLEM&problemBoxTitle=%2802.12%29+String-2&problemBoxCnt=4

import sys
sys.stdin = open("input.txt", "r")


def max_profit(future, prices):
    profit = 0

    for _ in range(future):
        prices.append(0)

    first_max = max(prices[1:future])

    for i in range(len(prices)-future):
        now_max = max(first_max, prices[i+future-1])
        if prices[i] < now_max:
            profit += now_max - prices[i]

    return profit


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_list = list(map(int, input().split()))

    print(f"#{t} {max_profit(N, input_list)}")
