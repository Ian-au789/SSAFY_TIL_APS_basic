# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZTP5XoqXuDHBIRD&probBoxId=AZTP1QzqXnfHBIRD&type=USER&problemBoxTitle=%2802.05%29+List1-1&problemBoxCnt=4 

#제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    
    def difference_max_min_section(length, section, list_of_numbers):
        max_section = sum(list_of_numbers[0:section])
        min_section = sum(list_of_numbers[0:section])

        for i in range(0, length-section+1):
            temp = sum(list_of_numbers[i:i+section]) 

            if temp < min_section:
                min_section = temp

            if temp > max_section:
                max_section = temp

        return max_section - min_section
	
    result = difference_max_min_section(N, M, num_list)
    print(f"#{test_case} {result}")
'''
N, M = 10, 5
num_list = [6262, 6004, 1801, 7660, 7919, 1280, 525, 9798, 5134, 1821] 

def difference_max_min_section(length, section, list_of_numbers):
    max_section = sum(list_of_numbers[0:section])
    min_section = sum(list_of_numbers[0:section])

    for i in range(0, length-section+1):
        temp = sum(list_of_numbers[i:i+section]) 

        if temp < min_section:
            min_section = temp

        if temp > max_section:
            max_section = temp

    return max_section - min_section

print(difference_max_min_section(N, M, num_list))
