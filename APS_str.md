# 문자열

### 컴퓨터에서의 문자 표현
1. ASCII 코드
2. 유니코드

Python 3.x 버전은 유니코드 UTF-8

## Python에서 문자열 처리

: 시퀀스 자료형으로 분류되고 별도의 데이터 타입(char) 없음. 
시퀀스 자료형에서 사용하는 인덱싱, 슬라이싱 연산 전부 사용

1. Concatenation (연결) : 문자열 + 문자열

2. Repetition (반복) : 문자열 * 숫자

list 와 string 을 넘나들며 다양한 메서드나 연산 활용

- str -> list : s = list(str)
- list -> str : "".join(s)

### n진수
: int (str, n) = string 형태의 숫자를 n진수 형태라고 입력하면 10진수 자연수로 출력

## 패턴 매칭

### 고지식한 패턴 검색 알고리즘

: 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식

    def BruteForce(p, t):
        i = 0
        j = 0
        len(p) = M
        len(t) = N

        while j < M and i < N:
            if t[i] != p[j]:
                i = i - j
                j = -1
            i += 1
            j += 1
        if j == M:
            return i - M
        else:
            return -1
시간 복잡도 = O(MN)

### KMP 알고리즘
: 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로,
불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭 수행

- 패턴을 전처리해 불일치 발생 시 이동할 다음 위치 저장
  
- 시간 복잡도 = O(M+N)


    def kmp(p, t):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)

    j = 0                   # 일치한 개수 = 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j

    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        if j==-1 or t[i]== p[j]:     # 첫글자자 불일치했거나, 일치하면
            i += 1
            j += 1
        else:                        # 불일치
            j = lps[j]
        if j==M:                     # 패턴을 찾을 경우
            print(i-M, end = ' ')    # 패턴의 인덱스 출력
            j = lps[j]

    print()
    return

