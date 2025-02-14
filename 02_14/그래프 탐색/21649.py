# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEqAeLavKIDFAVs&probBoxId=AZTP3wYKXqrHBIRD&type=USER&problemBoxTitle=%2802.14%29+Stack1-2&problemBoxCnt=5

import sys
sys.stdin = open("graph_input.txt")


def search_graph(num_v, num_e, edge_list):

    top = -1
    stack = [""]*num_v
    visited = [False]*num_v
    idx = 0

    while False in visited:                            # 모든 정점을 방문하면 loop 종료
        # 탐색 시작 (visited 안에 아무것도 없음)
        if visited[0] is False:
            for m in range(2):
                top += 1                               # 첫번째 간선의 시작점 도착점 저장
                stack[top] = edge_list[0][m]
                visited[idx] = edge_list[0][m]
                idx += 1

        # 방문하지 않은 지역 확인
        for n in range(num_e):
            if stack[top] in edge_list[n]:            # 현재 정점과 이어진 간선 탐색
                for e in edge_list[n]:
                    if e not in visited and e != stack[top]:   # 해당 간선이 아직 방문 안한 정점과 연결됐는지 확인
                        top += 1
                        stack[top] = e
                        visited[idx] = e
                        idx += 1
                        break

            if n == num_e - 1:                         # 더 이상 방문 못한 지역이 없으면 후퇴
                top -= 1

    return "-".join(map(str, visited))


V, E = map(int, input().split())
input_list = list(map(int, input().split()))
edges = []

for i in range(E):
    edges.append([input_list[2*i], input_list[2*i+1]])

print(f"#1 {search_graph(V, E, edges)}")
