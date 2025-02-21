# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWNcJ2sapZMDFAV8&probBoxId=AZTP3wYKXqzHBIRD&type=PROBLEM&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def back_to_room(size, matrix):
    go_back = [[0]*400 for _ in range(size)]          # 학생들이 방에 돌아가기 위해 지나간 구간
    visited = [0]*400                                 # 누가 한 번이라도 지나간 복도

    # 모든 학생들이 방에 돌아갔으면 0 반환 후 재귀 종료
    if size == 0:
        return 0

    else:
        # 모든 학생들이 방에 돌아가기 위해 지나가야 하는 복도의 구간 저장
        for i in range(size):
            # 출발 호수가 도착 호수보다 큰 경우, 작은 경우 나누기
            if matrix[i][0] > matrix[i][1]:
                for j in range(matrix[i][1], matrix[i][0] + 1):
                    go_back[i][j] = 1

            else:
                for j in range(matrix[i][0], matrix[i][1] + 1):
                    go_back[i][j] = 1

        new_matrix = []      # 방에 돌아가는 데 실패한 학생들
        cnt = 0              # 방에 돌아가는 데 성공항 학생 수

        for m in range(size):
            route = []
            for n in range(400):
                if go_back[m][n]:                         # 학생이 이동하는 구간
                    if visited[n]:                        # 이미 누군가 지나간 적 있는 구간과 겹치면 이동 불가
                        break
                    else:                                 # 아무도 해당 구간을 지나간 적 없으면 route에 추가
                        route.append(n)
                else:
                    continue

            else:
                for r in route:                          # 해당 이동 구간을 아무도 지나간 적이 없으면 전부 visited에 표시
                    visited[r] = 1
                cnt += 1                                 # 지나간 학생 수 + 1

            new_matrix.append(matrix[m])                 # 못 지나간 학생은 그 다음 재귀 함수로 넘기기

    return back_to_room(size - cnt, new_matrix) + 1      # 재귀 호출마다 1회 시도 추가


T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = []

    for _ in range(N):
        room_info = list(map(int, input().split()))
        # 해당 방 번호의 인덱스 위치 할당
        for k in range(2):
            if room_info[k] % 2 == 0:
                room_info[k] = room_info[k] // 2 - 1
            else:
                room_info[k] = room_info[k] // 2

        rooms.append([room_info[0], room_info[1]])

    print(f"#{t} {back_to_room(N, rooms)}")
