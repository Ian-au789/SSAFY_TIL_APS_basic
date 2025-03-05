numbers = [7, 2, 5, 3, 4, 6, 1]

min_heap = [-1]
idx = 0
for n in numbers:
    min_heap.append(n)
    idx += 1

    if min_heap[idx // 2] <= min_heap[idx]:
        continue

    else:
        check = idx
        while min_heap[check // 2] > min_heap[check]:
            min_heap[check // 2], min_heap[check] = min_heap[check], min_heap[check // 2]
            check //= 2

print(min_heap)

result = 0
while idx > 1:
    idx //= 2
    result += min_heap[idx]
