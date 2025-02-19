# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZE0RIBqwTsDFAVs&probBoxId=AZTP3wYKXqzHBIRD&type=USER&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("4881_input.txt")


def permutation(n, k):
    global cnt
    numbers = [i for i in range(1, n+1)]
    size = len(numbers)

    if n == 0:
        cnt += 1
        if cnt == k:
            return numbers

    else:
        for j in (size - k, size):
            numbers[j], numbers[size - n] = numbers[size - n], numbers[j]
            permutation(n-1, k)
            numbers[j], numbers[size - n] = numbers[size - n], numbers[j]


cnt = 0
