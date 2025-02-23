# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEGAQUa-sgDFAVs&probBoxId=AZTP3wYKXqXHBIRD&type=USER&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

import sys
sys.stdin = open("sample_input.txt", "r")


def count_subset(num_element, sum_element):
    my_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt = 0

    for i in range(1 << 12):                 # 2^12가지 부분집합 전부 탐색
        bits = [0] * 12                      # 반복할 때 마다 비트 초기화
        sum_sub = 0                          # 부분집합 원소의 합 초기화

        for j in range(12):
            if i & (1 << j):
                bits[j] += 1                 # 부분집합의 비트 기록

        if sum(bits) == num_element:         # 비트 개수가 입력과 일치하는 경우
            for k in range(12):
                if bits[k] == 1:             # 비트가 1인 인덱스 찾기
                    sum_sub += my_set[k]     # 동일한 인덱스를 가지는 집합의 원소 누적합

        if sum_sub == sum_element:           # 부분집합의 원소의 합이 입력과 일치하면 카운트
            cnt += 1

    return cnt


T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    print(f"#{t} {count_subset(N, K)}")
