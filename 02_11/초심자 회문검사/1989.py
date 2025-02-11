# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5PyTLqAf4DFAUq&probBoxId=AZTP3wYKXqfHBIRD&type=PROBLEM&problemBoxTitle=%2802.11%29+String-1&problemBoxCnt=7&&&&&&

import sys
sys.stdin = open("input.txt", "r")


# def palindrome(word):
#     word_invert = list(word)
#     for i in range(len(word)//2):
#         word_invert[i], word_invert[len(word)-1-i] = word_invert[len(word)-1-i], word_invert[i]
#
#     if word_invert == list(word):
#         return 1
#     else:
#         return 0

def palindrome_recursive(length, word):              # 종료 조건을 위해 문자열의 길이 input

    if word[length-1] == word[len(word) - length]:   # 서로 반대편에 있는 문자열 항목 비교
        if length == len(word)//2+1:                 # 종료 조건 (문자열 절반 검사하면 종료)
            return 1
        return palindrome_recursive(length-1, word)  # 비교 결과 일치하면 그 다음 항목 비교

    else:
        return 0                                     # 하나라도 불일치하면 종료


T = int(input())
for t in range(1, T+1):
    W = list(input())
    N = len(W)
    print(f"#{t} {palindrome_recursive(N, W)}")
