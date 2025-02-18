# Stack

### 계산기

1. 중위표기법 : 연산자를 피연산자의 가운데 표기하는 방법
2. 후위표기법 : 연산자를 피연산자 뒤에 표기하는 방법

스택으로 구현한 중위표기법 -> 후위표기법 변환 -> 계산


    

## 백트레킹

: 해를 찾는 도중에 '막히면' 되돌아가ㅓ 다시 해를 찾아가는 기법 (최적화 문제, 결정 문제)

- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지 여부를 답하는 문제

- DFS 와의 차이 : 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를
따라가지 않음으로써 시도 횟수 줄임 (가지치기) -> 불필요한 정보 조기 차단
  

    def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
        c = [0] * MAXCANDIDATES
    
        if k == n:
            process_solution(a, k)  # 답이면 원하는 작업을 한다
        else:
            ncandidates = construct_candidates(a, k, n, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k + 1, n)
                
    def construct_candidates(a, k, n, c):   # 후보 추천천
        c[0] = True                             # 원소의 포함 여부 
        c[1] = False
        return 2
    
    def process_solution(a, k):
        for i in range(k):
            if a[i]:
                print(num[i], end = ' ')
        print()
    
    MAXCANDIDATES = 2
    NMAX = 4
    a = [0] * NMAX
    num = [1,2,3,4]
    backtrack(a, 0, 3)

  
### 순열

    def f(i, N):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
        if i == N:  #
            print(p)
        else:
            for j in range(i, N):
                p[i], p[j] = p[j], p[i]
                f(i+1, N)   # i+1자리 결정
                p[i], p[j] = p[j], p[i]
    
    p = [0,1,2]
    N = 3
    f(0, N)

백트래킹 사용

    def backtrack(a, k, n):
        c = [0] * MAXCANDIDATES
    
        if k == n:
            for i in range(0, k):
                print(a[i], end=" ")
            print()
        else:
            ncandidates = construct_candidates(a, k, n, c)
            for i in range(ncandidates):
                a[k] = c[i]
                backtrack(a, k + 1, n)
    
    def construct_candidates(a, k, n, c):
        in_perm = [False] * (NMAX + 1)
    
        for i in range(k):
            in_perm[a[i]] = True
    
        ncandidates = 0
        for i in range(1, NMAX + 1):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1
        return ncandidates
    
    MAXCANDIDATES = 3
    NMAX = 3
    a = [0]*NMAX
    backtrack(a, 0, 3)


### 부분집합

    def f(i, N):
        if i == N:
            print(bit)
        else:
            bit[i] = 1
            f(i+1, N)
            bit[i] = 0
            f(i+1, N)
    
    A = [1, 2, 3]
    bit = [0]*len(A)
    f(0, 3)
                