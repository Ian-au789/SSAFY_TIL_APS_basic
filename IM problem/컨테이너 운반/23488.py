# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZT4zC2qTCrHBIOK&probBoxId=AZT4yWiKS8vHBIOK&type=USER&problemBoxTitle=IM+%EB%8C%80%EB%B9%84%ED%95%98%EC%9E%90%21&problemBoxCnt=6

import sys
sys.stdin = open("sample_input(3).txt", "r")


def shipping(length_c, length_t, cargo_list, truck_list):
    max_weight = 0

    cargo_list.sort(reverse=1)            # 내림차순으로 정렬
    truck_list.sort(reverse=1)

    for i in range(length_t):
        for j in range(length_c):
            if truck_list[i] >= cargo_list[j]:         # 트럭이 운반할 수 있는 화물의 무게 탐색
                max_weight += cargo_list[j]            # 최대 무게에 더하기
                cargo_list.remove(cargo_list[j])       # 적재한 화물은 리스트에서 제거
                length_c -= 1                          # 탐색 범위 조정
                break

    return max_weight


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    list_M = list(map(int, input().split()))

    print(f"#{t} {shipping(N, M, list_N, list_M)}")
