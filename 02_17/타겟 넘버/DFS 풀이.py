def dfs_solution(numbers, target):
    size = len(numbers)
    global cnt

    if sum(numbers) == target:
        cnt += 1

    else:
        for i in range(size):
            if negative[i] == 0:
                negative[i] = 1
                numbers[i] += -1
                dfs_solution(numbers, target)

negative = [0, 0, 0, 0, 0]
cnt = 0
dfs_solution([1, 1, 1, 1, 1], 3)
print(cnt)