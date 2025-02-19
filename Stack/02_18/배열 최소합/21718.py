# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZE0RVAKwUMDFAVs&probBoxId=AZTP3wYKXqzHBIRD&type=USER&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("4881_input.txt")


def find_min_sum(level, size, mid_sum):
    global min_sum

    if level == size:                                        # 마지막 레벨에 도달했을 때
        if mid_sum < min_sum:                                # 현재 최소합보다 작으면 갱신
            min_sum = mid_sum
        return

    if mid_sum > min_sum:                                    # 중간합이 이미 현재 최소합을 넘어버리면 탐색 중단 (가지치기)
        return

    else:
        for i in range(size):
            if not visited[i]:                               # 아직 방문하지 않은 열
                visited[i] = 1                               # 방문 기록
                mid_sum += matrix[level][i]                  # 현재 주소의 항목 더하기
                find_min_sum(level + 1, size, mid_sum)       # 그 다음 행으로 넘어가서 재귀 호출
                mid_sum -= matrix[level][i]                  # 돌아 왔으면 더했던 값 제거
                visited[i] = 0                               # 방문 기록 초기화


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        input_list = list(map(int, input().split()))
        matrix.append(input_list)

    visited = [0] * N
    min_sum = sum([matrix[i][i] for i in range(N)])            # 최소 합 초기값 설정

    find_min_sum(0, N, 0)

    print(f"#{t} {min_sum}")
