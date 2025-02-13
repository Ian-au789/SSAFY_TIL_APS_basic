# https://swexpertacademy.com/main/talk/solvingClub/problemBoxDetail.do?solveclubId=AZTP1QzqXnbHBIRD&probBoxId=AZTP3wYKXqnHBIRD&leftPage=1

import sys
sys.stdin = open('input.txt')


def pascal_triangle(number):
    if number == 1:                                       # 종료조건
        start = [1]                                       # 1 반환 및 출력
        print(1)
        return start

    else:
        up = pascal_triangle(number - 1)                  # 재귀호출
        size = len(up)+1
        result = [0]*size

        for i in range(size):                             # 파스칼의 삼각형 원리
            if i == 0:
                result[i] = up[i]
                print(result[i], end=" ")

            elif i == size-1:
                result[i] = up[i-1]
                print(result[i])

            else:
                result[i] = up[i-1] + up[i]
                print(result[i], end=" ")

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f"#{t}")
    pascal_triangle(N)
