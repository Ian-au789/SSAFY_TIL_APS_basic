# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWNcJ2sapZMDFAV8&probBoxId=AZTP3wYKXqzHBIRD&type=PROBLEM&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def back_to_room(size, matrix):
    visited = [0]*200                                      # 누가 한 번이라도 지나간 복도

    # 모든 학생들이 방에 돌아갔으면 0 반환 후 재귀 종료
    if size == 0:
        return 0

    else:
        failed = []      # 방에 돌아가는 데 실패한 학생들

        for m in range(size):
            route = []                                     # 각 학생이 이동한 복도 구간 저장
            for n in range(matrix[m][0], matrix[m][1]+1):
                if visited[n]:                             # 이미 누군가 지나간 적 있는 구간과 겹치면 이동 불가
                    break
                else:                                      # 아무도 해당 구간을 지나간 적 없으면 route에 추가
                    route.append(n)

            else:
                for r in route:                            # 해당 이동 구간을 아무도 지나간 적이 없으면 전부 visited에 표시
                    visited[r] = 1
                continue

            failed.append(matrix[m])                       # 못 지나간 학생은 그 다음 재귀 함수로 넘기기

    return back_to_room(len(failed), failed) + 1           # 재귀 호출마다 1회 시도 추가


T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = []

    for _ in range(N):
        input_list = list(map(int, input().split()))
        # 방 호수 정렬하고 해당 방 번호의 인덱스 위치 할당
        room_info = [min(input_list), max(input_list)]

        for k in range(2):
            room_info[k] = (room_info[k] - 1) // 2

        rooms.append([room_info[0], room_info[1]])

    print(f"#{t} {back_to_room(N, rooms)}")
