#https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AYcllbDqUVgDFASR&probBoxId=AZTQE57aYKnHBIRD&type=PROBLEM&problemBoxTitle=연습문제%28안풀어도됨%2C+말+그대로+더+하고+싶은+사람만%29&problemBoxCnt=4

import sys
sys.stdin = open("sample_input.txt", "r")


def dots_in_circle(radius):
    origin = 1                  # 원점
    cnt = 0

    # 원은 상하좌우 대칭이므로 y > 1, x >= 0 일 떄만 구하고 4배
    for y in range(1, radius+1):
        for x in range(radius):
            if x**2 + y**2 <= radius**2:
                cnt += 1
            else :                         # 원의 범위를 벗어나는 순간 더 탐색은 비효율
                break

    return 4*cnt + origin


T = int(input())
for t in range(1, T+1):
    r = int(input())
    print(f"#{t} {dots_in_circle(r)}")
