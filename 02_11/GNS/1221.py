# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14jJh6ACYCFAYD&probBoxId=AZTP3wYKXqfHBIRD&type=PROBLEM&problemBoxTitle=%2802.11%29+String-1&problemBoxCnt=7

import sys
sys.stdin = open("input.txt", "r")


def sort_number(numbers):
    sort_list = []
    order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for number in order:
        for i in range(len(numbers)):
            if numbers[i] == number:
                sort_list.append(numbers[i])

    return " ".join(sort_list)


T = int(input())
for t in range(1, T+1):
    n, N = map(str, input().split())
    input_list = list(map(str, input().split()))

    print(f"#{t} {sort_number(input_list)}")
