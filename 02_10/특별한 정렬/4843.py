# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZTP-exKX8PHBIRD&probBoxId=AZTP3wYKXqbHBIRD&type=USER&problemBoxTitle=%2802.10%29+List2-2&problemBoxCnt=6

import sys
sys.stdin = open("4843_input.txt", "r")


def special_sort(length, numbers):

    for i in range(length-1):
        min_idx = i
        max_idx = i
        for j in range(i+1, length):
            if i % 2 == 0:                                             # i가 짝수일 때 최댓값 맨앞으로, i가 홀수일 때 최솟값 맨앞으로
                if numbers[max_idx] < numbers[j]:                      # 최댓값 갱신
                    max_idx = j

            else:
                if numbers[min_idx] > numbers[j]:                      # 최솟값 갱신
                    min_idx = j

        if i % 2 == 0:
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
        else:
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

        if i == 9:                                                     # 원소 10개 정렬하면 함수 중단
            break

    return numbers[:10]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_list = list(map(int, input().split()))

    print(f"#{t} {' '.join(map(str, special_sort(N, input_list)))}")
