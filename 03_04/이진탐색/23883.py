# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AZVkIGsKB__HBINE&probBoxId=AZVjg-a6ABDHBITD&type=USER&problemBoxTitle=%2803.04%29+tree1&problemBoxCnt=4

import sys
sys.stdin = open("5176_input.txt")


# 이진 탐색 트리의 규칙을 지키기 위해 중위 순회 방식 이용 (L < V < R)
# 완전 이진 트리에 중위 순회 방식으로 1부터 채워넣기
def complete_binary_tree(n):
    global N
    global node

    if n <= N:
        complete_binary_tree(n * 2)        # 왼쪽 자식 노드가 존재하나 확인
        tree[n] = node                     # 중위 순회 방식이므로 L V R 순서
        node += 1
        complete_binary_tree(n * 2 + 1)    # 오른쪽 자식 노드가 존재하나 확인
    return


T = int(input())
for t in range(1, T+1):
    N = int(input())
    max_num = N
    tree = [0]*(N+1)

    node = 1
    complete_binary_tree(1)

    print(f"#{t} {tree[1]} {tree[N//2]}")
    print(tree)
