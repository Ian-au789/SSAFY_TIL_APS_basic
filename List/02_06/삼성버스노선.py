# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZTP1QzqXnbHBIRD&contestProbId=AWczm7QaACgDFAWn&probBoxId=AZTP3wYKXqTHBIRD&type=PROBLEM&problemBoxTitle=%2802.06%29+List1-2&problemBoxCnt=8

'''
N = int(input())

ab_list = []

for i in range(N):
    ab_list.append(list(map(int, input().split())))

P = int(input())

c_list = []

for i in range(P):
    c_list.append(int(input()))

    ~~~

print(f"#{test_case}", end = " ")

print(" ".join(map(str, count_c)))
'''
ab_list = [[1, 3], [2, 5]]
c_list = [1, 2, 3, 4, 5]

'''
count_bus = [0]*(max(c_list)+1)               # 각 정류장의 버스 노선 갯수 저장 

for ab in ab_list:
    for i in range(ab[0], ab[1]+1):              # Ai 이상 Bi 이하 버스 정거장을 지나는 버스 노선 1개씩 추가 
        count_bus[i] += 1

count_c = []

for c in c_list:
    count_c.append(count_bus[c])           # c 번호 정거장을 지나가는 버스 노선 개수를 따로 저장 

print(count_c)
'''
count_c = [0]*len(c_list)
idx = 0
for c in c_list:
    for ab in ab_list:
        if c >= ab[0] and c <= ab[1]:
            count_c[idx] += 1
    idx += 1

print(count_c)