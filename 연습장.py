# 행렬 입력 받기
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_matrix = []
    for _ in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)


# 한 줄 입력받기

T = int(input())
for t in range(1, T+1):
    N = int(input)
    input_list = list(map(int, input().split()))
'''


def permutation(n, k):
    global cnt
    numbers = [i for i in range(1, n+1)]
    visited = [0] * n
    idx = 0

    while cnt != k:
        perm = []
        while idx < n:
            for i in range(n):
                if not visited[i]:
                    perm.append(numbers[i])
                    idx += 1
                    break
                else:
                    continue

            else:
                out = perm.pop()
                idx -= 1
                visited[out] = 0

        cnt += 1

    return perm



cnt = 0

