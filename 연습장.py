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


def f(i, N):  # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    if i == N:  #
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i + 1, N)  # i+1자리 결정
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
N = 3
f(0, N)