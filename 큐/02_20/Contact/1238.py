# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV15B1cKAKwCFAYD&probBoxId=AZTP3wYKXq7HBIRD&type=PROBLEM&problemBoxTitle=%2802.20%29+Queue-2&problemBoxCnt=5

import sys
sys.stdin = open("input.txt")


def last_contact(start):
    this_level = 0  # 현재 레벨의 노드 개수 카운트
    level = [[1, start]]  # 각 레벨의 노드 개수 저장
    next_level = 0  # 다음 레벨의 노드 개수 카운트
    queue = [start]  # 큐 준비
    visited[start] = 1
    vertex = []

    while len(queue) > 0:
        cnt = sum(matrix[queue[0]])                   # 다음에 이동할 수 있는 정점 개수 확인
        if cnt == 0:                                  # 막다른 곳이면 넘어가기
            pass
        else:
            for n in range(1, 101):
                if matrix[queue[0]][n]:               # 다음에 이동할 수 있는 정점

                    if not visited[n]:                # 아직 방문하지 않은 곳이면 카운트
                        next_level += 1
                        visited[n] = 1                # 방문 한 곳 카운트
                        vertex.append(n)              # 다음 레벨의 방문 가능한 정점 저장
                        queue.append(n)

        queue.pop(0)
        this_level += 1

        if this_level == level[len(level) - 1][0]:
            if next_level == 0:                       # 더 이상 진행이 불가능 하면 마지막에 저장된 정점들 중 가장 큰 번호 반환
                return max(level[len(level) - 1][1])
            else:
                level.append([next_level, vertex])
                this_level = 0
                next_level = 0
                vertex = []


for t in range(1, 11):
    N, V = map(int, input().split())
    input_list = list(map(int, input().split()))

    matrix = [[0]*101 for i in range(101)]
    visited = [0] * 101

    for i in range(N // 2):
        matrix[input_list[2 * i]][input_list[2 * i + 1]] = 1

    print(f"#{t} {last_contact(V)}")
