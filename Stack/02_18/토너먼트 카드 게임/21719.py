# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZE0RvcKwVUDFAVs&probBoxId=AZTP3wYKXqzHBIRD&type=USER&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("4880_input.txt")


def group_competition(size, rsp):

    if size == 2:
        return rock_scissor_paper(rsp[0], rsp[1])

    elif size == 1:
        return rsp[0]

    else:
        return rock_scissor_paper(group_competition((size+1)//2, rsp[:(size+1)//2]),
                                  group_competition(size - (size+1) // 2, rsp[(size+1)//2:]))


# 가위바위보 승자를 정하는 함수
def rock_scissor_paper(m, n):
    if m[1] == 1 and n[1] == 3:
        return m

    elif m[1] == 3 and n[1] == 1:
        return n

    elif m[1] == n[1]:
        if m[0] < n[0]:
            return m
        else:
            return n

    else:
        if m[1] < n[1]:
            return n
        else:
            return m


T = int(input())
for t in range(1, T+1):
    N = int(input())
    input_list = list(map(int, input().split()))

    cards = []
    for i in range(N):
        cards.append([i+1, input_list[i]])

    result = group_competition(N, cards)
    print(f"#{t} {result[0]}")

