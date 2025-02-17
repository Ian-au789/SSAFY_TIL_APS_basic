cnt = 0
num_list = [1, 1, 1, 1, 1]
target = 3
negative = [0, 0, 0, 0, 0]

size = len(num_list)

for i in range(1 << size):
    for j in range(size):
        if i & (1 << j):
            negative[j] = 1
        else:
            negative[j] = 0

    num_list = [1, 1, 1, 1, 1]
    for k in range(size):
        if negative[k] == 1:
            num_list[k] *= -1

    if sum(num_list) == target:
        cnt += 1

print(cnt)


def solution(numbers, target):
    cnt = 0
    size = len(numbers)
    negative = [0] * size

    for i in range(1 << size):
        for j in range(size):
            if i & (1 << j):
                negative[j] = 1
            else:
                negative[j] = 0

        numbers = list(map(abs, numbers))

        for k in range(size):
            if negative[k] == 1:
                numbers[k] *= -1

        if sum(numbers) == target:
            cnt += 1

    return cnt
