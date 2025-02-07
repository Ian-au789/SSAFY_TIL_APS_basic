# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV139KOaABgCFAYh&probBoxId=AZTP3wYKXqTHBIRD&type=PROBLEM&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

'''
for test_case in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    ~~~

    print(f"#{test_case} {flatten(N, boxes)}")
'''

N = 834
boxes = [42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 
  92, 5, 3, 54, 93, 83, 22, 17, 19, 96, 48, 27, 72, 39, 70, 13, 68, 100, 36, 95, 
  4, 12, 23, 34, 74, 65, 42, 12, 54, 69, 48, 45, 63, 58, 38, 60, 24, 42, 30, 79, 
  17, 36, 91, 43, 89, 7, 41, 43, 65, 49, 47, 6, 91, 30, 71, 51, 7, 2, 94, 49, 30, 
  24, 85, 55, 57, 41, 67, 77, 32, 9, 45, 40, 27, 24, 38, 39, 19, 83, 30, 42]


def flatten(max_dump, box_list):

    dumps = 0
    length = len(box_list)

    if sum(box_list) % length == 0:                    # 박스의 총합이 리스트 길이에 나누어 떨어지면 평탄화가 완료됐을 떄 고저차가 0
        flat = 0  

    else :                                             # 그렇지 않으면 1 
        flat = 1

    while dumps < max_dump:                            # 덤프 횟수가 최대횟수에 도달할 때 까지 

        '''
        min_box = min(box_list)                        # 가장 높은 박스와 가장 낮은 박스 갱신 
        max_box = max(box_list)


        if max_box - min_box == flat:                  # 최대 횟수에 도달하기 전에 평탄화 완료되면 중단 
            return flat

        for i in range(0, length):                     # 제일 먼저 찾은 최솟값에 1 더하고 break 
            if box_list[i] == min_box:
                box_list[i] += 1
                break

        for i in range(0, length):                     # 제일 먼저 찾은 최댓값에 1 빼고 break 
            if box_list[i] == max_box:
                box_list[i] -= 1
                break
        '''                                            # max, min 함수 남발은 시간복잡도 증가 초래 

        max_box, min_box = box_list[0], box_list[0]
        max_idx, min_idx = 0, 0

        for i in range(length):                        # 최대, 최소, 인덱스 동시에 반환 

            if box_list[i] > max_box:
                max_idx, max_box = i, box_list[i]

            if box_list[i] < min_box:
                min_idx, min_box = i, box_list[i]
        
        if max_box - min_box == flat:                  # 최대 횟수에 도달하기 전에 평탄화 완료되면 중단 
            return flat

        box_list[max_idx] -= 1
        box_list[min_idx] += 1

        dumps += 1                                     # while loop 1회마다 덤프 + 1 


    return max_box - min_box           # 평탄화 완료 못했을 시 최대 고저차 반환 
    
print(flatten(N, boxes))
