# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZFOC3XauCcDFAVs&probBoxId=AZTP3wYKXq7HBIRD&type=USER&problemBoxTitle=%2802.20%29+Queue-2&problemBoxCnt=5

import sys
sys.stdin = open("5102_input.txt")


def how_many_node(start, end):
    global V
    this_level = 0                               # 현재 레벨의 노드 개수 카운트
    level = [1]                                  # 각 레벨의 노드 개수 저장
    next_level = 0                               # 다음 레벨의 노드 개수 카운트
    queue = [start]                              # 큐 준비
    visited[start] = 1

    while len(queue) > 0:
        for i in range(V+1):
            if matrix[queue[0]][i]:
                if not visited[i]:
                    if i == end:
                        return len(level)            # 도착 노드에 도달하면 지금까지 노드 개수 반환

                    queue.append(i)
                    visited[i] = 1
                    next_level += 1

        else:
            queue.pop(0)
            this_level += 1

            if this_level == level[len(level)-1]:  # 현재 레벨의 노드를 다 탐색했으면
                level.append(next_level)           # 다음 레벨의 노드 개수 저장
                this_level = 0                     # 카운트 초기화
                next_level = 0

    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range((V+1))]         # 출발 노드를 행번호로 가지고 도착 노드를 열번호로 가지는 항목 1로 표시

    for k in range(E):
        node1, node2 = map(int, input().split())       # 방향 없는 그래프의 간선 양방향으로 저장
        matrix[node1][node2] = 1
        matrix[node2][node1] = 1

    S, G = map(int, input().split())
    visited = [0]*(V+1)
    visited[0] = 1

    print(f"#{t} {how_many_node(S, G)}")
