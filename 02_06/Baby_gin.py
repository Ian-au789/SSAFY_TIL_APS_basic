# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AYZS3UfKuQgDFARc&probBoxId=AZTP3wYKXqTHBIRD&type=USER&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

# 제출용 정답
'''
card = int(input())


print(f"{test_case} {Baby_gin(random_6)})
'''

# Greedy Method 
random_6 = "532235"

def Baby_gin(card):
    card_list = []

    for i in range(6):
        div = card // 10**(5-i)
        card_list.append(div)
        card %= 10**(5-i)
    
    M = max(card_list)
    counts = [0]*(M+1)

    for number in card_list:
        counts[number] += 1

    run = 0
    triplet = 0

    for i in range(M-1):
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            while counts[i] != 0 and counts[i+1] != 0 and counts[i+2] != 0:
                run += 1
                counts[i] -= 1
                counts[i+1] -= 1
                counts[i+2] -= 1
        
    for i in range(M+1):
        if counts[i] >= 3:
            while counts[i] >= 3:
                triplet += 1
                counts[i] -= 3

    if run + triplet == 2:
        return True

    else :
        return False

print(Baby_gin(int(random_6)))