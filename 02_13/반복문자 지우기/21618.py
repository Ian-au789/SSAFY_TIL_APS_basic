# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEk4KA69-gDFAVs&probBoxId=AZTP3wYKXqnHBIRD&type=USER&problemBoxTitle=%2802.13%29+Stack1-1&problemBoxCnt=5

import sys
sys.stdin = open('sample_input.txt')


def erase_same_letter(line):
    pass


T = int(input())
for t in range(1, T+1):
    input_line = list(input())
    print(f"#{t} {erase_same_letter(input_line)}")