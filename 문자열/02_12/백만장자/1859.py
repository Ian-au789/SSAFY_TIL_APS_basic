# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5LrsUaDxcDFAXc&probBoxId=AZTP3wYKXqjHBIRD&type=PROBLEM&problemBoxTitle=%2802.12%29+String-2&problemBoxCnt=4

import sys
sys.stdin = open("input.txt", "r")


def max_profit(length, prices):
    idx = 0
    profit = 0

    while idx < length - 1:
        max_price = prices[idx]
        max_price_idx = idx

        for i in range(idx, length):
            if max_price < prices[i]:
                max_price = prices[i]
                max_price_idx = i

        profit += max_price * (max_price_idx - idx) - sum(prices[idx:max_price_idx])

        idx = max_price_idx + 1

    return profit


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    input_list = list(map(int, input().split()))

    print(f"#{t} {max_profit(N, input_list)}")