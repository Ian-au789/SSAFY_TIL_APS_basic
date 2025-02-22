# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWNcJ2sapZMDFAV8&probBoxId=AZTP3wYKXqzHBIRD&type=PROBLEM&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def back_to_room(matrix):
    # 모든 학생들이 방에 돌아갔으면 종료
    if len(matrix) == 0:
        return 0

    else:
        visited = [0] * 200                                # 복도 (0~199) 매 회차 초기화
        failed = []                                        # 방에 돌아가는 데 실패한 학생들

        for room in matrix:
            route = []                                     # 각 학생이 이동한 복도 구간 저장
            for n in range(room[0], room[1]+1):
                if visited[n]:                             # 이미 누군가 지나간 적 있는 구간과 겹치면 이동 불가
                    failed.append(room)                    # 못 지나간 학생은 다음 기회에 시도
                    break
                else:                                      # 아무도 해당 구간을 지나간 적 없으면 route에 추가
                    route.append(n)

            else:
                for n in route:                            # 아무와도 겹치지 않는 이동 루트 visited에 표시
                    visited[n] = 1

    return back_to_room(failed) + 1           # 1회차 시도 종료


T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = []

    for _ in range(N):
        start, end = map(int, input().split())
        # 방 호수 정렬하고 해당 방 번호의 인덱스 위치 할당
        room_info = [min((start - 1) // 2, (end - 1) // 2), max((start - 1) // 2, (end - 1) // 2)]

        rooms.append(room_info)

    print(f"#{t} {back_to_room(rooms)}")
