# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZGv4enKpNkDFAXd&probBoxId=AZTP3wYKXqfHBIRD&type=USER&problemBoxTitle=%2802.11%29+String-1&problemBoxCnt=7

import sys
sys.stdin = open("sample_input.txt", "r")


def included_word(str1, str2):
    check = 0
    for i in range(len(str2) - len(str1)+1):         # str2 내부에 str1 길이만큼 슬라이싱한 문자열 순회
        if str2[i:i+len(str1)] == str1:
            check = 1

    if check == 1:                                   # 내부에 문자열 존재하면 1, 없으면 0 반환
        return 1
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    A = input()
    B = input()
    print(f"#{t} {included_word(A, B)}")
