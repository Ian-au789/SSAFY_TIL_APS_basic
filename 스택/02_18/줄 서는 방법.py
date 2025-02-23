# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZE0RIBqwTsDFAVs&probBoxId=AZTP3wYKXqzHBIRD&type=USER&problemBoxTitle=%2802.18%29+Stack2-2&problemBoxCnt=5

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def permutation(n, k):
    numbers = list(range(1, n + 1))  # 1부터 n까지 숫자 리스트
    answer = []
    k -= 1  # 인덱스 보정 (0부터 시작)

    for i in range(n, 0, -1):
        fact = factorial(i - 1)  # 직접 구현한 팩토리얼 함수 사용
        index = k // fact  # 현재 위치에서 사용할 숫자의 인덱스
        answer.append(numbers.pop(index))  # 해당 숫자 선택 후 리스트에서 제거
        k %= fact  # 다음 선택을 위해 k 업데이트

    return answer


# Math 라이브러리 사용 방법
from math import factorial


def permutation_math(n, k):
    numbers = list(range(1, n + 1))  # 1부터 n까지 숫자 리스트
    answer = []
    k -= 1  # 인덱스 보정 (0부터 시작)

    for i in range(n, 0, -1):
        fact = factorial(i - 1)  # (i-1)! 값
        index = k // fact  # 현재 위치에서 사용할 숫자의 인덱스
        answer.append(numbers.pop(index))  # 해당 숫자 선택 후 리스트에서 제거
        k %= fact  # 다음 선택을 위해 k 업데이트

    return answer



print(permutation_math(3, 6))  # [3, 2, 1]
print(permutation_math(4, 9))  # [2, 3, 1, 4]
print(permutation_math(5, 16)) # [3, 1, 5, 2, 4]
