def hanoi_tower(n):
    if n == 1:
        return 1
    else:
        return hanoi_tower(n-1)*2+1


print(hanoi_tower(4))