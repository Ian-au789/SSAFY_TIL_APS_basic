# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV134DPqAA8CFAYh&probBoxId=AZTP1QzqXnfHBIRD&type=PROBLEM&problemBoxTitle=%2802.05%29+List1-1&problemBoxCnt=4

# 제출용 정답
'''
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    def open_sight(building, N):
        count = 0

        for idx in range(2, N-2):                                                 # 양쪽 2칸 씩 제외 (탐색 불가)
            my_building = building[idx]                                         # 현재 건물의 높이 
            left_building = max(building[idx-1], building[idx-2])           # 왼쪽 2칸 내 건물 중 가장 높은 건물의 높이
            right_building = max(building[idx+1], building[idx+2])        # 오른쪽 2칸 내 건물 중 가장 높은 건물의 높이

            left_sight = 0                                                            # 조망권이 확보된 층 (왼쪽, 오른쪽)
            right_sight = 0

            if left_building < my_building:                                  # 왼쪽, 오른쪽 2칸 중 가장 높은 건물이 현재 건물보다 작으면
                left_sight = my_building - left_building                   # 그 차이만큼의 층 수는 한 쪽 조망권이 확보 

            if right_building < my_building:
                right_sight = my_building - right_building

            count += min(left_sight, right_sight)                         # 조망권은 높은 층 부터 확보되므로 왼쪽 오른쪽 중 적은 층 수가 양쪽 조망권 다 확보 

        return count                              
    
    print(f"#{test_case} {open_sight(arr, N)}")
'''
N = 11
building = [0, 0, 118, 90, 243, 178, 99, 100, 200, 0, 0]

def open_sight(building, N):
    count = 0

    for idx in range(2, N-2):                                         # 양쪽 2칸 씩 제외 (탐색 불가)
        my_building = building[idx]                                   # 현재 건물의 높이 
        left_building = max(building[idx-1], building[idx-2])         # 왼쪽 2칸 내 건물 중 가장 높은 건물의 높이
        right_building = max(building[idx+1], building[idx+2])        # 오른쪽 2칸 내 건물 중 가장 높은 건물의 높이

        left_sight = 0                                                # 조망권이 확보된 층 (왼쪽, 오른쪽)
        right_sight = 0

        if left_building < my_building:                               # 왼쪽, 오른쪽 2칸 중 가장 높은 건물이 현재 건물보다 작으면
            left_sight = my_building - left_building                  # 그 차이만큼의 층 수는 한 쪽 조망권이 확보 

        if right_building < my_building:
            right_sight = my_building - right_building

        count += min(left_sight, right_sight)                         # 조망권은 높은 층 부터 확보되므로 왼쪽 오른쪽 중 적은 층 수가 양쪽 조망권 다 확보 

    return count                                                      # 탐색하면서 전부 저장 

print(open_sight(building, N))

