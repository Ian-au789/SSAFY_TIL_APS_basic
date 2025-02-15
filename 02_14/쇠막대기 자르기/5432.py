# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWVl47b6DGMDFAXm&probBoxId=AZTP3wYKXqrHBIRD&type=PROBLEM&problemBoxTitle=%2802.14%29+Stack1-2&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def cut_stick(brackets):
    pass


T = int(input())
for t in range(1, T+1):
    string = input()
    print(f"#{t} {cut_stick(string)}")
