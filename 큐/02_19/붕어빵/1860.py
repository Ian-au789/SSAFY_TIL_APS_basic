# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5LsaaqDzYDFAXc&probBoxId=AZTP3wYKXq3HBIRD&type=PROBLEM&problemBoxTitle=%2802.19%29+Queue-1&problemBoxCnt=6

import sys
sys.stdin = open("input.txt")


def no_waiting(size, time, food, waiting):
    waiting.sort()                          # 내림차순 정렬
    for i in range(size):
        waiting[i] //= time                 # 손님이 도착한 해당 시각에 진기가 붕어빵 몇 번 만들었는지 재할당

    if waiting[0] == 0:                     # 첫 손님이 왔을 때 만들어놓은 붕어빵이 없으면 실패
        return "Impossible"

    stock = waiting[0] * food               # 첫 손님이 도착했을 때 만들어 놓은 붕어빵 개수
    clock = waiting[0]                      # 진기가 지금까지 붕어빵을 만든 횟수

    for wait in waiting:
        if clock < wait:
            stock += (wait - clock) * food  # 붕어빵을 만든 횟수가 늘어나면 그 만큼 stock에 만든 개수만큼 추가
            clock = wait

        stock -= 1                          # 손님 한 명당 붕어빵 하나씩 감소

        if stock < 0:                       # 붕어빵 재고가 다 떨어지면 실패
            return "Impossible"

    return "Possible"                       # 모든 손님에게 붕어빵 판매가 끝나면 성공


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    print(f"#{t} {no_waiting(N, M, K, customers)}")
