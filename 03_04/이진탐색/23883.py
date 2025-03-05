# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkIGsKB__HBINE&probBoxId=AZVjg-a6ABDHBITD&type=USER&problemBoxTitle=%2803.04%29+tree1&problemBoxCnt=4

import sys
sys.stdin = open("5176_input.txt")


class Binary_Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


T = int(input())
for t in range(1, T+1):
    N = int(input())

    print(f"#{t} {} {}")
