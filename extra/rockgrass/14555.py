# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYGtoa3qARcDFARC

import sys
sys.stdin = open("sample_in.txt", "r")


def least_ball(code):
    idx = 0
    cnt = 0

    while idx < len(code)-1:
        if code[idx] == "(" or code[idx+1] == ")":  # 공 절반이 보이면 무조건 공이 있음
            cnt += 1
            idx += 1

        idx += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    field = list(input())
    print(f"#{t} {least_ball(field)}")
