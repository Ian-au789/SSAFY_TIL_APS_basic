# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWQmA4uK8ygDFAXj&probBoxId=AZT4yWiKS8vHBIOK&type=PROBLEM&problemBoxTitle=IM+%EB%8C%80%EB%B9%84%ED%95%98%EC%9E%90%21&problemBoxCnt=8

import sys
sys.stdin = open("sample_input(1).txt")


def othello(size, matrix):
    # 보드 게임 준비
    board = [[0]*size for _ in range(size)]
    board[size // 2 - 1][size // 2 - 1] = 2
    board[size // 2 - 1][size // 2] = 1
    board[size // 2][size // 2 - 1] = 1
    board[size // 2][size // 2] = 2

    # 델타 탐색
    di = [1, 0, -1, 0, 1, 1, -1, -1]
    dj = [0, 1, 0, -1, 1, -1, 1, -1]
    scalar = 1

    for move in matrix:
        board[move[1]][move[0]] = move[2]

        if move[2] == 2:
            me = 2
            opponent = 1

        else:
            me = 1
            opponent = 2

        for m in range(8):
            if 0 <= move[1] + di[m] <size and 0 <= move[0] + dj[m] < size:                          # 인접한 칸이 보드 안에 있나 확인
                if board[move[1] + di[m]][move[0] + dj[m]] == opponent:                             # 인접한 칸이 상대의 돌이면
                    scalar = 1                                                                      # 스칼라 초기화

                    while 0 <= move[1] + scalar*di[m] <size and 0 <= move[0] + scalar*dj[m] < size: # 탐색 범위가 보드 안에 있을 때
                        if board[move[1] + scalar*di[m]][move[0] + scalar*dj[m]] == opponent:       # 한 칸씩 전진하면서 확인
                            scalar += 1

                        elif board[move[1] + scalar*di[m]][move[0] + scalar*dj[m]] == me:           # 내 돌을 찾으면 그 사이 모든 돌 색 바꾸기
                            for n in range(1, scalar):
                                board[move[1] + n * di[m]][move[0] + n * dj[m]] = me
                            break

                        else:
                            break

    # 흑돌 백돌 개수 세기
    cnt_black = 0
    cnt_white = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                cnt_black += 1
            elif board[i][j] == 2:
                cnt_white += 1

    result = [cnt_black, cnt_white]
    return " ".join(map(str, result))


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    input_matrix = []
    for _ in range(M):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    for a in range(M):
        for b in range(2):
            input_matrix[a][b] -= 1

    print(f"#{t} {othello(N, input_matrix)}")
