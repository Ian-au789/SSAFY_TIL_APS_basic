# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEF_UA6-pADFAVs&probBoxId=AZTP3wYKXqXHBIRD&type=USER&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("sample_input.txt", "r")


def find_purple(color_matrix):
    paper = [[0]*10 for _ in range(10)]                           # 빈 모눈종이 준비
    cnt = 0                                                       # 보라색 칸 세기

    for color in color_matrix:
        for i in range(color[0], color[2]+1):                     # 색칠 영역의 행 좌표 전부
            for j in range(color[1], color[3]+1):                 # 색칠 영역의 열 좌표 전부
                if paper[i][j] != color[4] and paper[i][j] < 3:   # 이미 칠한 색 중복 색칠 방지, 보라색에 또 칠하기 방지
                    paper[i][j] += color[4]                       # 색칠하기

                if paper[i][j] == 3:                              # 보라색 칸 하나당 카운트
                    cnt += 1

    return cnt


T = int(input())
for t in range(1, T+1):
    input_matrix = []

    N = int(input())
    for n in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{t} {find_purple(input_matrix)}")