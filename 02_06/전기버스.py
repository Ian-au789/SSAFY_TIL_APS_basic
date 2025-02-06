# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZTP8TUaX0jHBIRD&probBoxId=AZTP3wYKXqTHBIRD&type=USER&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

# 제출용 답안
'''
K, N, M = map(int, input().split())
charge = list(map(int, input().split()))

print(f"#{test_case} {charge_time}")
'''

K, N, M  = 3, 10, 5
charge = [1, 3, 5, 7, 9]

station = [0]*(N+1)

for location in charge:
    station[location] = 1

