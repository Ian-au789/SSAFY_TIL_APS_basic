# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AV5Pl0Q6ANQDFAUq&probBoxId=AZTP3wYKXqTHBIRD&type=PROBLEM&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    ~~~

    print(f"#{test_case} {result[0]} {result[1]} {result[2]} {result[3]} {result[4]}")
'''

n = 6791400

def factorization(number):

    exp = [0]*5

    factors = [2, 3, 5, 7, 11]

    for i in range(5):
        while number % factors[i] == 0:
            number /= factors[i]
            exp[i] += 1

    return exp

print(factorization(n))
