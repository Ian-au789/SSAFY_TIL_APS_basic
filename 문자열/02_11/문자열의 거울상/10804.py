# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXTC0x16D8EDFASe&probBoxId=AZTP3wYKXqfHBIRD&type=PROBLEM&problemBoxTitle=%2802.11%29+String-1&problemBoxCnt=7

import sys
sys.stdin = open("input.txt", "r")


def mirror(string):
    result = list(string[::-1])                               # list로 변환하고 순서 거꾸로

    invert = {"b": "d", "d": "b", "p": "q", "q": "p"}         # 거울에 비추면서 바뀌기 전과 후

    for i in range(len(result)):
        for key in invert:                                    # 현재 글자가 key와 일치하면 거울에 반사된 글자로 바꿈
            if result[i] == key:
                result[i] = invert[key]
                break

    return "".join(result)


T = int(input())
for t in range(1, T+1):
    letters = input()
    print(f"#{t} {mirror(letters)}")
