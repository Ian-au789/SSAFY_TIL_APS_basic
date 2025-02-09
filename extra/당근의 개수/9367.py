# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AW_nY2m6OLADFARY&probBoxId=AZTQE57aYKnHBIRD&type=USER&problemBoxTitle=연습문제%28안풀어도됨%2C+말+그대로+더+하고+싶은+사람만%29&problemBoxCnt=4

import sys
sys.stdin = open("carrot_sample_in.txt", "r")


def increasing_carrot(number, carrot_list):
    cnt = 1                               # 최소 길이 1
    inc = 1
    carrot_list.append(0)                 # 맨 뒤에 0 추가해서 인덱스 에러 방지, 0보다 작은 항목 없으므로 영향 x

    for i in range(number):
        this_carrot = carrot_list[i]
        next_carrot = carrot_list[i+1]

        if this_carrot < next_carrot:     # 다음 당근이 지금 당근보다 크면 카운트
            cnt += 1

            if cnt > inc:                 # 연속해서 커진 횟수 중 최댓값 저장
                inc = cnt

        else:                             # 증가가 멈추면 카운트 초기화
            cnt = 1

    return inc


T = int(input())
for t in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    print(f"#{t} {increasing_carrot(N, carrots)}")