# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZTP6dSqXwrHBIRD&probBoxId=AZTP1QzqXnfHBIRD&type=USER&problemBoxTitle=%2802.05%29+List1-1&problemBoxCnt=4

# 제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    def highest_drop(N, box_list):
        max_fall = 0

        for i in range(0, len(box_list)-1):
            count = 1  

            for j in range(i+1, len(box_list)):     

                if box_list[i] <= box_list[j]: 
                    count += 1


            fall = N-(i+count)

            if max_fall < fall:
                max_fall = fall

        return max_fall
    
    print(f"#{test_case} {highest_drop(n, arr)}")
'''

N = 9
box_list = [7, 4, 2, 0, 0, 6, 0, 7, 0]

def highest_drop(N, box_list):
    
    max_fall = 0

    for i in range(0, len(box_list)-1):
        count = 1  

        for j in range(i+1, len(box_list)):     

            if box_list[i] <= box_list[j]: 
                count += 1
            

        fall = N-(i+count)

        if max_fall < fall:
            max_fall = fall
        
    return max_fall

print(highest_drop(N, box_list))