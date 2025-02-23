# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV_65wkqsb4DFAWS&probBoxId=AZTP3wYKXqjHBIRD&type=PROBLEM&problemBoxTitle=%2802.12%29+String-2&problemBoxCnt=4

import sys
sys.stdin = open('sample_input.txt', encoding='utf-8')


def fast_type(type_str, key_str):
    type_length = len(type_str)
    key_length = len(key_str)
    idx = 0                                               # 탐색 시작하는 위치
    typing = 0                                            # 타이핑한 횟수

    while idx <= type_length - key_length:
        for i in range(key_length):                       # 패턴의 길이만큼 선행 문자열 탐색
            if type_str[idx + i] == key_str[i]:           # 패턴과 일치한다면
                if i == key_length - 1:
                    idx += key_length                     # 패턴의 길이만큼 앞으로 이동
                    typing += 1                           # 타이핑은 한 번만

            else:                                         # 패턴과 일치하지 않으면
                idx += 1                                  # 다음으로 이동
                typing += 1
                break

    if idx < type_length:
        typing += type_length - idx

    return typing


def fast_type2(type_str, key_str):                         # 내장함수 이용 버전
    fast_key = type_str.count(key_str)

    result = len(type_str) - fast_key*len(key_str) + fast_key

    return result


T = int(input())
for t in range(1, T+1):
    A, B = map(str, input().split())

    print(f"#{t} {fast_type(A, B)}")
