# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZE0RVAKwUMDFAVs&probBoxId=AZTP3wYKXqzHBIRD&type=USER&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("4881_input.txt")


def f(i, size):
    if i == size:
        result = 0
        idx = 0
        for n in perm:
            result += input_matrix[idx][n]
            idx += 1
        all_sum.append(result)

    else:
        for j in range(i, N):
            perm[i], perm[j] = perm[j], perm[i]
            f(i + 1, N)
            perm[i], perm[j] = perm[j], perm[i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_matrix = []
    for _ in range(N):
        input_list = list(map(int, input().split()))
        input_matrix.append(input_list)

    perm = [i for i in range(N)]
    all_sum = []

    f(0, N)
    print(f"#{t} {min(all_sum)}")
