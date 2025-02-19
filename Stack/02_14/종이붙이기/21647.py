# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEp_DvavHMDFAVs&probBoxId=AZTP3wYKXqrHBIRD&type=USER&problemBoxTitle=%2802.14%29+Stack1-2&problemBoxCnt=5

import sys
sys.stdin = open("4869_input.txt")

def combination(m, n):
    result = 1

    for i in range(m, m-n, -1):
        result *= i

    for j in range(1, n+1):
        result //= j

    return result


def paper_puzzle(size):
    max_square = size//20
    cnt = 0

    for paper_20 in range(max_square+1):
        paper_10 = size//10 - 2*paper_20
        cnt += 2**paper_20 * combination(paper_10 + paper_20, paper_20)

    return cnt


"""
30 - 4+1 2*2+1
40 - 2*2 + 2*3 + 1
50 - 20+1 2*4+2*2*3+1
70 - 84+1 2*6+2*2*10+2*2*2*4+1
"""


T = int(input())
for t in range(1, T+1):
    row = int(input())
    print(f"#{t} {paper_puzzle(row)}")
