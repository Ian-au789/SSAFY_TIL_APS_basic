# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGv4_VapOEDFAXd&probBoxId=AZTP3wYKXqbHBIRD&type=USER&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("sample_input(1).txt", "r")

# 오늘 배운 이진 탐색
def search_game(end, key):
    start = 1
    middle = (end + start) // 2
    cnt = 0

    while middle != key:
        if key > middle:
            start = middle
        else:
            end = middle

        middle = (end + start) // 2
        cnt += 1

    return cnt

T = int(input())
for t in range(1, T+1):
    L, M, N = map(int, input().split())

    # 횟수가 적은 쪽이 승리, 횟수가 동일하면 무승부
    if search_game(L, M) < search_game(L, N):
        result = "A"

    elif search_game(L, M) == search_game(L, N):
        result = 0

    else :
        result = "B"

    print(f"#{t} {result}")
