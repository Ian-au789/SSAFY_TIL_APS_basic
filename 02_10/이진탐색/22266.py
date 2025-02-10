# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGv4_VapOEDFAXd&probBoxId=AZTP3wYKXqbHBIRD&type=USER&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("sample_input(1).txt", "r")


def search_game(pages, page1, page2):
    pass


T = int(input())
for t in range(1, T+1):
    L, M, N = map(int, input().split())

    print(f"#{t} {search_game(L, M, N)}")
