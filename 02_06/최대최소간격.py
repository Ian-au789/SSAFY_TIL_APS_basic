# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXYEGnBq6h0DFAST&probBoxId=AZTP3wYKXqTHBIRD&type=USER&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

# 제출용 정답
'''
N = int(input())
input_list = list(map(int, input().split()))

'''
length = 20
numbers = [4, 1, 6, 7, 9, 4, 1, 4, 8, 4, 1, 6, 5, 3, 1, 4, 3, 1, 10, 10]

def distance_min_max(lng, num_list):

    min_num = min(num_list)                 # 최솟값 
    max_num = max(num_list)                 # 최댓값 

    min_idx = 0
    max_idx = lng-1

    for i in range(lng):                   # 앞에서부터 탐색하면 동일한 값이 있어도 인덱스 최소치 반환 
        if num_list[i] == min_num:
            min_idx = i
            break

    for i in range(lng-1, -1, -1):         # 뒤에서부터 탐색하면 동일한 값이 있어도 인덱스 최대치 반환 
        if num_list[i] == max_num:
            max_idx = i
            break

    return abs(max_idx - min_idx)          # 인덱스 차의 절댓값 반환 


print(distance_min_max(length, numbers))

