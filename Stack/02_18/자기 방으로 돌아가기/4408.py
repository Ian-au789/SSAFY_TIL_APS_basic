# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWNcJ2sapZMDFAV8&probBoxId=AZTP3wYKXqzHBIRD&type=PROBLEM&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

import sys
sys.stdin = open("sample_input.txt")


def back_to_room(size, matrix):
    pass


T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = []

    for _ in range(N):
        room_info = list(map(int, input().split()))
        rooms.append(room_info)

    print(f"#{t} {back_to_room(N, rooms)}")