# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWVl47b6DGMDFAXm&probBoxId=AZTP3wYKXqrHBIRD&type=PROBLEM&problemBoxTitle=%2802.14%29+Stack1-2&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def cut_stick(brackets):
    size = len(brackets)
    top = -1
    idx = 0
    cnt = 0

    while idx < size:
        if brackets[idx] == "(" and brackets[idx+1] == ")":        # 레이저 () 탐색
            cnt += top+1                                           # 레이저가 현재 위치를 지나가는 막대기들을 자르면서 그 개수만큼 막대기 추가
            idx += 2                                               # 2칸 이동

        else:
            if brackets[idx] == "(":                               # 쇠막대 왼쪽 끝 탐색
                top += 1
                idx += 1
                cnt += 1                                           # 막대기 카운트

            else:                                                  # 쇠막대 오른쪽 끝 탐색
                top -= 1
                idx += 1

    return cnt


T = int(input())
for t in range(1, T+1):
    input_list = list(map(str, input()))
    print(f"#{t} {cut_stick(input_list)}")
