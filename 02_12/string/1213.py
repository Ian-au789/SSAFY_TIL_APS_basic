# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14P0c6AAUCFAYi&probBoxId=AZTP3wYKXqjHBIRD&type=PROBLEM&problemBoxTitle=%2802.12%29+String-2&problemBoxCnt=4

import sys
sys.stdin = open('test_input.txt', encoding='utf-8')


def boyer_moore(pattern, sentence):
    len_sen = len(sentence)
    len_pat = len(pattern)
    cnt = 0
    idx = len_pat - 1
    check_list = list(pattern)[::-1]                                  # 인덱스 계산 편하게 하기 위해 거꾸로

    while idx <= len_sen - 1:
        for i in range(len_pat):
            if sentence[idx - i] != check_list[i]:                    # 문자열의 항목이 패턴의 항목과 일치하나 확인

                if sentence[idx - i] in check_list[i:]:               # 불일치한 항목이 현 위치 앞 패턴 항목 중 있을 때
                    idx += check_list[i:].index(sentence[idx - i])    # 그 위치로 이동
                else:
                    idx += len_pat                                    # 부분 일치가 없으므로 이동
                break

            else:
                if i == len_pat - 1:                                  # 패턴이 일치하면 카운트 하고 패턴 길이 만큼 이동
                    cnt += 1
                    idx += len_pat
    return cnt


for t in range(10):
    T = int(input())
    p = input()
    str_input = input()

    print(f"#{T} {boyer_moore(p, str_input)}")
