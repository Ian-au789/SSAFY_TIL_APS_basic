# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AYZS3UfKuQgDFARc&probBoxId=AZTP3wYKXqTHBIRD&type=USER&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

# 제출용 정답
'''
card = input()
~~~
print(f"#{test_case} {Baby_gin(int(random_6))}")
'''


random_6 = "054060"
# Greedy Method


def baby_gin(card):

    card_list = []

    for i in range(6):
        div = card // 10 ** (5 - i)
        card_list.append(div)
        card %= 10 ** (5 - i)

    m = max(card_list)
    counts = [0] * (m + 1)

    for number in card_list:
        counts[number] += 1

    run = 0
    triplet = 0

    for i in range(m - 1):
        if counts[i] >= 1 and counts[i + 1] >= 1 and counts[i + 2] >= 1:
            while counts[i] != 0 and counts[i + 1] != 0 and counts[i + 2] != 0:
                run += 1
                counts[i] -= 1
                counts[i + 1] -= 1
                counts[i + 2] -= 1

    for i in range(m + 1):
        if counts[i] >= 3:
            while counts[i] >= 3:
                triplet += 1
                counts[i] -= 3

    if run + triplet == 2:
        return True

    else:
        return False


print(baby_gin(int(random_6)))

# 완전탐색

def Baby_gin2(card):
    card_list = list(map(int, card))
    pass
    # Permutation = []
    # run = 0
    # triplet = 0

    # for a in range(0, 6):
    #     for b in range(0, 6):
    #         for c in range(0, 6):
    #             for d in range(0, 6):
    #                 for e in range(0, 6):
    #                     for f in range(0, 6):
                            


print(Baby_gin2(random_6))