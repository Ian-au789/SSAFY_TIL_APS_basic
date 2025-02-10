# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXAerAPaVXMDFARP&probBoxId=AZTP3wYKXqbHBIRD&type=USER&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("input1.txt", "r")


def max_powder(row, column, matrix):
    max_cnt = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]                          # 델타 탐색 (상하좌우)

    for i in range(row):
        for j in range(column):
            cnt = matrix[i][j]                  # 터뜨릴 풍선 안에 있는 꽃가루

            for m in range(1, matrix[i][j]+1):                   # 해당 풍선의 꽃가루 개수 만큼 상하좌우로 추가로 터짐
                for n in range(4):
                    if 0 <= i + m*di[n] < row and 0 <= j + m*dj[n] < column:  # 추가로 터지는 풍선이 배열 안에 있는 경우에만
                        cnt += matrix[i + m*di[n]][j + m*dj[n]]               # 추가로 터지는 풍선 안의 꽃가루 카운트

            if max_cnt < cnt:                   # 최댓값 갱신
                max_cnt = cnt

    return max_cnt


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    input_matrix = []
    for r in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    print(f"#{t} {max_powder(N, M, input_matrix)}")
