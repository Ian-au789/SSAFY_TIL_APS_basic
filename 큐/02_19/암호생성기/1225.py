# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV14uWl6AF0CFAYD&probBoxId=AZTP3wYKXq3HBIRD&type=PROBLEM&problemBoxTitle=%2802.19%29+Queue-1&problemBoxCnt=6

import sys
sys.stdin = open("input.txt")


def encrypting(num_list):
    while 1:
        for i in range(1, 6):
            n = num_list.pop(0)                      # 맨 앞의 숫자 pop
            n -= i                                   # 암호화

            if n <= 0:                               # 0 이하로 내려가면 맨 뒤에 넣고 암호화 종료
                n = 0
                num_list.append(n)
                return " ".join(map(str, num_list))
            else:
                num_list.append(n)



for _ in range(10):
    t = int(input())
    numbers = list(map(int, input().split()))

    print(f"#{t} {encrypting(numbers)}")
