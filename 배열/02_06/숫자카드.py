# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AYYPdof62mIDFARc&probBoxId=AZTP3wYKXqTHBIRD&type=USER&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

# 제출용 정답
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    cards = input()
    
    ~~~
    
    print(f"#{test_case} {result[0]} {result[1]}")
'''
lng = 5

n = "49679"


def many_cards(length, card):

    card_list = []

    for i in range(length):
        card_list.append(int(card[i]))

    counts = [0]*10

    for number in card_list:
        counts[number] += 1

    for i in range(9, -1, -1):
        if counts[i] == max(counts):
            return i, max(counts)


print(many_cards(lng, n))