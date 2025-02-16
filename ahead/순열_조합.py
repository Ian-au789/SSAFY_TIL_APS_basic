# itertools 라이브러리로 함수 활용 가능

# 순열 출력
def three_permutation(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                for k in range(1, n+1):
                    if i != k and j != k:
                        print(f"{i} {j} {k}")
    return "fin"


# 순열 재귀
def permute(arr, chosen, used, length):
    if len(chosen) == length:
        print(chosen)
        return

    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            chosen.append(arr[i])
            permute(arr, chosen, used, length)
            chosen.pop()
            used[i] = False


# Define the set of 5 elements
# items = [1, 2, 3, 4, 5]
# used = [False] * len(items)
# permute(items, [], used, 3)


# 조합 출력
def three_combination(n):
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                print(f"{i} {j} {k}")

# three_combination(5)

def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i + 1:], n-1):
            result.append([elem]+rest)
    return result

print(comb([1, 2, 3, 4, 5], 3))