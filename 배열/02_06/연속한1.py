# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AXALDUIq97oDFASI&probBoxId=AZTP3wYKXqTHBIRD&type=USER&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

'''
N = int(input())
bin = input()

~~~

print(f"#{test_case} {ones_in_a_row(N, bin)}")
'''

n = 10
bin = "0000100001"

def ones_in_a_row(length, binary):

    max_count = 0
    count = 0

    binary = binary + '0'                         # 마지막 항목까지 확인하기 위해 맨 뒤에 0 추가 

    for i in range(length):

        if binary[i] == '1' :                     # 1을 찾으면 카운팅 시작 
            count += 1

            if max_count < count:                 # 카운팅 최댓값 갱신 
                    max_count = count

            if binary[i+1] == '0':                # 바로 다음 항목이 0이면 카운팅 초기화 
                count = 0

    return max_count

print(ones_in_a_row(n, bin))
