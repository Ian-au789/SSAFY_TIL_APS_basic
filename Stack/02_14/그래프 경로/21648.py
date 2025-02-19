# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEqAGXqvIcDFAVs&probBoxId=AZTP3wYKXqrHBIRD&type=USER&problemBoxTitle=%2802.14%29+Stack1-2&problemBoxCnt=5

import sys
sys.stdin = open("4871_input.txt")


def route_exist(num_v, v_start, v_end):
    # 스택 준비
    top = -1
    stack = [0]*num_v
    visited = [0]*(num_v+1)

    # 시작 노드 저장
    top += 1
    stack[top] = v_start                          # 현재 위치하고 있는 노드
    visited[v_start] = 1                          # 방문한 적 있는 노드는 1로 체크

    while 1:
        for v_next in edges[stack[top]]:          # 해당 노드와 이어진 경로 탐색

            if visited[v_next] == 0:              # 다음 노드가 아직 방문하지 않은 곳이면

                if v_next == v_end:               # 다음 노드가 종착점과 일치하면 1 반환
                    return 1

                top += 1
                stack[top] = v_next               # 해당 노드로 이동
                visited[v_next] = 1               # 방문했다고 체크
                break

            else:
                continue

        else:
            top -= 1

            if top == -1:                         # 시작점으로 돌아오면 0 반환 (경로가 없음)
                return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        edges[v1].append(v2)                     # v1노드를 인덱스 번호로 가지는 항목에 v2 저장

    start, end = map(int, input().split())
    print(f"#{t} {route_exist(V, start, end)}")

# for-else 문 쓰면 더 쉽다.