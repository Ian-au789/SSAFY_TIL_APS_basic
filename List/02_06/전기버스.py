# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZTP8TUaX0jHBIRD&probBoxId=AZTP3wYKXqTHBIRD&type=USER&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

# 제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    station = list(map(int, input().split()))

    def how_many_charge(K, N, M, charge):

        distance_charge = [0]*(M+1)           # 출발점, 종착역, 그리고 충전소 사이의 거리 

        charge.append(N)
        distance_charge[0] = charge[0]

        for i in range(1, M+1):
            distance_charge[i] = charge[i] - charge[i-1]

        drive = 0                             # 버스가 운전한 거리
        charge_time = 0                       # 버스가 충전한 횟수 

        for distance in distance_charge:
            if distance > K:                  # 충전소 사이의 거리가 운전 가능 거리보다 멀면 도착 불가
                return 0

            else :
                drive += distance             # 충전소 사이의 거리 버스가 운전한 거리에 합산
                if drive > K:                 # 운전 가능 거리를 초과하면 
                    charge_time += 1          # 충전 횟수 1 증가 
                    drive = distance          # 운전한 거리가 초과하기 직전에 drive 초기화   

                elif drive == K:
                    if distance != distance_charge[M]:    # 종착역에 도달하면 충전할 필요가 없음 
                        charge_time += 1                  
                        drive = 0  

        return charge_time
	
    print(f"#{test_case} {how_many_charge(a, b, c, station)}")
'''

K, N, M  = 5, 20, 5
charge = [4, 7, 9, 14, 17]

def how_many_charge(K, N, M, charge):

    distance_charge = [0]*(M+1)           # 출발점, 종착역, 그리고 충전소 사이의 거리 

    charge.append(N)
    distance_charge[0] = charge[0]

    for i in range(1, M+1):
        distance_charge[i] = charge[i] - charge[i-1]

    drive = 0                             # 버스가 운전한 거리
    charge_time = 0                       # 버스가 충전한 횟수 

    for distance in distance_charge:
        if distance > K:                  # 충전소 사이의 거리가 운전 가능 거리보다 멀면 도착 불가
            return 0
        
        else :
            drive += distance             # 충전소 사이의 거리 버스가 운전한 거리에 합산
            if drive > K:                 # 운전 가능 거리를 초과하면 
                charge_time += 1          # 충전 횟수 1 증가 
                drive = distance          # 운전한 거리가 초과하기 직전에 drive 초기화   

            elif drive == K:
                if distance != distance_charge[M]:    # 종착역에 도달하면 충전할 필요가 없음 
                    charge_time += 1                  
                    drive = 0  
        
    return charge_time

print(how_many_charge(K, N, M, charge))