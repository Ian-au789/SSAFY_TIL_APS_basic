# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc

import sys
sys.stdin = open("input.txt")


def dfs(size, visited, idx, probability):
    global max_prob

    if idx == size:
        max_prob = max(max_prob, probability)
        return

    for i in range(size):
        if matrix[idx][i] == 0:
            continue
        else:
            if not visited[i]:
                visited[i] = 1
                dfs(size, visited, idx + 1, probability * (matrix[idx][i] / 100))
                visited[i] = 0

    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    check = [0]*N

    max_prob = 0
    dfs(N, check, 0, 1)

    print(f"#{t} {max_prob*100}")
