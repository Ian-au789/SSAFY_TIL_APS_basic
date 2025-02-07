# 2차원 배열

: 2차원 이상의 다차원 list는 차원에 따라 index 선언

ex) arr = [[0, 1, 2, 3], [4, 5, 6, 7]] (2행 4열의 2차원 배열)

### 0으로 채워진 2차원 배열 만들기
    arr = [[0]*4 for _ in range(3)]

 **!!!** arr = [[0]*4]*3  <- 얕은 복사처럼 3번 객체 참조 (모든 행의 원소가 같이 바뀜)

### 2차원 배열에 입력값 저장하기

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]             # input 사이에 공백이 없으면 split 제거


### 2차원 배열 순회 

    # 행 우선 순회

    for i in range(n):
        for j in range(M):
            print(arr[i][j])

    # 열 우선 순회

    for j in range(m):             # 열의 index를 바깥 for문
        for i in range(n) :
            print(arr[i][j])

    # 지그재그 순회 

    for i in range(n):
        for j in range(m):
            print(arr[i][j + (m -1 -2*j) * (i%2)])

        # i가 짝수이면 arr[i][j] (앞 부터 탐색)
        # i가 홀수이면 arr[i][m-1-j] (뒤 부터 탐색)
 
    