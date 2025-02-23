import sys
sys.stdin = open("4871_input.txt")


def route_exist(v_start, v_end):
    pass

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        edges[v1].append(v2)                     # v1노드를 인덱스 번호로 가지는 항목에 v2 저장

    start, end = map(int, input().split())
    print(f"#{t} {route_exist(start, end)}")
