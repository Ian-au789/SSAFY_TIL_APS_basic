# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEk40hq-AcDFAVs&probBoxId=AZTP3wYKXqnHBIRD&type=USER&problemBoxTitle=%2802.13%29+Stack1-1&problemBoxCnt=5

import sys
sys.stdin = open('bracket_input.txt')


def check_bracket(brackets):
    pass


for T in range(1, 5):
    input_list = list(map(str, input()))
    print(f"#{T} {check_bracket(input_list)}")