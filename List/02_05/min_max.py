# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZTP6EZaXv7HBIRD&probBoxId=AZTP1QzqXnfHBIRD&type=USER&problemBoxTitle=%2802.05%29+List1-1&problemBoxCnt=4

# 제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    num_list = list(map(int, input().split()))

    def find_min(input):
        minimum = input[0]

        for i in range(0, len(input)):
            if minimum > input[i]:
                minimum = input[i]

        return minimum

    def find_max(input):
        maximum = input[0]

        for i in range(0, len(input)):
            if maximum < input[i]:
                maximum = input[i]

        return maximum

    print(f"#{test_case} {find_max(num_list) - find_min(num_list)}")

'''

N = 5
num_list = [477162, 658880, 751280, 927930, 297191]

def find_min(input):
    minimum = input[0]

    for i in range(0, len(input)):
        if minimum > input[i]:
            minimum = input[i]

    return minimum

def find_max(input):
    maximum = input[0]

    for i in range(0, len(input)):
        if maximum < input[i]:
            maximum = input[i]

    return maximum

print(find_max(num_list) - find_min(num_list))