# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZEGAQUa-sgDFAVs&probBoxId=AZTP3wYKXqXHBIRD&type=USER&problemBoxTitle=%2802.07%29+List2-1&problemBoxCnt=8

'''
N, K = int(input().split())

'''
N = 3
K = 6

set = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

for i in range(2):    # 각 원소의 포함 여부 할당
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l

                for m in range(4):
                    if bit[m] == 1:
                        print(set[m], end = "")