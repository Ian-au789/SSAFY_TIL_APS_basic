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
 
## 델타 탐색

: 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

    # arr = N*N matrix 
    
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            for d in range(4):
                around = []
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < N:
                    around.append(arr[ni][nj])

            print(around)

    # 탐색할 가로세로 방향의 범위를 넓히고 싶으면 di*c , dj*c 

### 전치 행렬

    # Transpose

    for i in range(3):
        for j in range(3):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

## 부분 집합

: 완전검색 기법 사용 (모든 부분집합 생성 후 탐색)

**비트**를 사용해서 부분집합 표현 

    set = [1, 2, 3, 4]
    bit = [0, 0, 0, 0]

    for i in range(2):    # 각 원소의 포함 여부 할당
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                for l in range(2):
                    bit[3] = l

                    for m in range(4):
                        if bit[m] == 1:
                            print(a[m], end = "")
                            
### 비트 연산자
- & : 비트 단위 and

- | : 비트 단위 or

- << : 피연산자의 비트 열을 왼쪽으로 이동 (2배)

- \>> : 피연산자의 비트 열을 오른쪽으로 이동 (0.5배)

응용

부분집합 개수 -> 1 << n : 2<sup>n

각 원소 유무 확인 -> i & (1<<j ) : i 의 j 번째 비트가 1인지 아닌지 검사 


    # 비트 연산자 사용해서 n개의 원소를 가지는 집합의 부분집합 만들기 
    
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                print(arr[j], end=", ")

        print()
    print()
    
## 검색
: 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

탐색 키 : 자료를 구별하여 인식할 수 있는 키

### 순차 검색
: 첫 번째 원소부터 순서대로 검색대상과 키 값이 같은 원소가 있는지 비교하며 탐색, 
동일한 원소를 찾으면 그 원소의 인덱스 반환. 자료구조 마지막까지 검색 대상을 찾지 못하면 실패

- 가장 간단하고 직관적인 검색 방법 (단순한 알고리즘)

- 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 유용

- 검색 대상이 많은 경우 수행시간이 급격히 증가하여 비효율적


    i = 0
    while i < n and a[i] != key:
        i += 1

    if i < n : return i             # 인덱스 반환
    else : return -1                # 검색 실패



### 이진 검색
