# https://www.acmicpc.net/problem/12927
'''
1. 1번 전구가 켜져 있으면 cnt + 1, Y <-> N 바꾸기
2. 작은 번호부터 탐색하면서 번호가 켜져 있으면 해당 번호의 배수만큼의 전구 전부 바꾸기
3. 리스트 한 번 순회하면 끝
'''


def how_many_switch(bulbs):
    cnt = 0
    for i in range(len(bulbs)):
        if bulbs[i] == "Y":                         # Y 찾으면 스위치 누르기
            cnt += 1
            for j in range(i, len(bulbs)):
                if (j + 1) % (i + 1) == 0:          # 번호(인덱스 + 1)가 배수인지 확인 (자기자신 포함)
                    if bulbs[j] == "Y":             # Y는 N으로, N은 Y로 바꾸기
                        bulbs[j] = "N"
                    else:
                        bulbs[j] = "Y"
    return cnt


arr = list(input())
print(how_many_switch(arr))
