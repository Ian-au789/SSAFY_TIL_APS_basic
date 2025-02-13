# Stack

: 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다. (탑 쌓기)

- 선형 구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  
- 후입선출(LIFO) : 마지막에 삽입한 자료를 가장 먼저 꺼낸다.

### Stack 구현하기
1. top : 마지막 삽입된 원소의 위치 (자료구조로 배열 사용)

2. push : 저장소에 자료를 저장하기



    def push(item, size)
        global top
        top += 1
        if top == size:
            print("overflow!")   

        else:
            stack[top] = item

    size = 10
    stack = [0]*stack
    top = -1
   

3. pop : 저장소에서 삽입한 자료의 역순으로 자료를 꺼낸다



    def pop():
        global top
        if top == -1:
            pritn("underflow")
            return 0
        else:
            top -= 1
            return stack[top+1]


4. isEmpty : 스택이 공백인지 아닌지를 확인

5. peek : 스택의 top에 있는 항목을 반환하는 연산

<참고 사항>
- pop, append 메서드는 사용할 수 있지만 시간이 오래 걸림 (할당에 비교해서)

- 1차원 배열을 사용하여 구현하면 편하지만 스택의 크기를 변경하기가 어려움

- 동적 연결리스트를 이용해 단점을 해결하고 메모리를 효율적으로 사용 가능. 단 구현이 복잡함

### Function Call

: 프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리 
(가장 마지막에 호출된 함수가 제일 먼저 실행을 완료하고 복귀하는 후입선출 구조)

- 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 
주소 등이 정보를 스택 프레임(stack frame)에 저장하여 **시스템 스택**에 삽입
  
- 함수의 실행이 끝나면 시스템 스택의 top원소(스택 프레임)를 삭제(pop)하면서 프레임에 저장되어
있던 복귀주소를 확인하고 복귀
  
## 재귀 호출

: 필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조 (특정 작업의 효율성, 최적화 가능)

ex) factorial, fibonacci


    def f(i, N):      # 크기가 N인 배열 arr[i]의 모든 원소에 접근
        if i == N:
            return
        else:
            print(arr[i])
            f(i+1, N)
