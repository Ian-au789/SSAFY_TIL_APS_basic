# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZFI7O-a8asDFAVs&probBoxId=AZTP3wYKXq3HBIRD&type=USER&problemBoxTitle=%2802.19%29+Queue-1&problemBoxCnt=6&&&&&&

import sys
sys.stdin = open("5099_input.txt")


def last_pizza(size, pizzas):
    roast = [0]*size                            # 화구 준비
    idx = -1

    while len(pizzas) > 0:                      # 모든 피자를 집어 넣을 때 까지
        idx = (idx + 1) % size                  # 인덱스 번호 순환
        if roast[idx] == 0:                     # 화구가 비어있으면 피자 집어 넣기
            roast[idx] = pizzas.pop()

        else:
            roast[idx][1] //= 2                 # 한 바퀴 돌때마다 치즈 절반 녹음
            if roast[idx][1] == 0:
                roast[idx] = pizzas.pop()       # 치즈가 다 녹으면 피자 꺼내고 다음 피자 집어 넣기


    while len(roast) > 1:
        idx = (idx + 1) % size
        roast[idx][1] //= 2

        if roast[idx][1] == 0:
            roast.pop(idx)
            idx -= 1
            size -= 1

    return roast[0][0]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_matrix = []
    for k in range(M):
        input_matrix.append([k+1, input_list[k]])

    print(f"#{t} {last_pizza(N, input_matrix[::-1])}")
