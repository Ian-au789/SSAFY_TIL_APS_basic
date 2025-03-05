# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkGPH6BwbHBINE&probBoxId=AZVjg-a6ABDHBITD&type=USER&problemBoxTitle=%2803.04%29+tree1&problemBoxCnt=4

import sys
sys.stdin = open("tree_input.txt")


# def pre_order(n):
#     if n:
#         print(n, end = ' ')
#         pre_order(left[n])
#         pre_order(right[n])
#
#     return
#
N = int(input())
numbers = list(map(int, input().split()))
#
# left = [0]*(N+1)
# right = [0]*(N+1)
# par = [0]*(N+1)
#
# for i in range(N-1):
#     parent = numbers[i*2]
#     sibling = numbers[i*2 + 1]
#
#     if left[parent] == 0:
#         left[parent] = sibling
#     else:
#         right[parent] = sibling
#
#     par[sibling] = parent
#
# sibling = N
#
# while par[sibling] != 0:
#     sibling = par[sibling]
#
# root = sibling
# pre_order(root)


def pre_order(n):
    if n:
        print(n, end =" ")

        for k in range(len(vertex[n])):
            if vertex[n][k] == 1:
                pre_order(k)

    return


vertex = [[0]*(N+1) for _ in range(N+1)]
for i in range(len(numbers) // 2):
    vertex[numbers[i*2]][numbers[i*2 + 1]] = 1

pre_order(numbers[0])

