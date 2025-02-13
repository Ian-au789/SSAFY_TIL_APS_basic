# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZTP_-YKX_rHBIRD&probBoxId=AZTP3wYKXqfHBIRD&type=USER&problemBoxTitle=%2802.11%29+String-1&problemBoxCnt=7

import sys
sys.stdin = open("sample_input(1).txt", "r")


def many_alphabet(str1, str2):
    check = set()                   # str1에서 중복 제거한 알파벳 저장
    for letter in str1:
        check.add(letter)

    max_cnt = 0                     # 제일 많은 알파벳 개수
    for i in check:                 # check 집합 내 원소와 str2의 알파벳 일일이 비교
        cnt = 0
        for j in str2:
            if i == j:              # 일치하면 카운트
                cnt += 1
            if max_cnt < cnt:       # 최댓값 갱신
                max_cnt = cnt

    return max_cnt


T = int(input())
for t in range(1, T+1):
    A = input()
    B = input()
    print(f"#{t} {many_alphabet(A, B)}")
