# Stack

: 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다. (탑 쌓기)

- 선형 구조 : 자료 간의 관계가 1대1의 관계를 갖는다.
  
- 후입선출(LIFO) : 마지막에 삽입한 자료를 가장 먼저 꺼낸다.

### Stack 구현하기
1. top : 마지막 삽입된 원소의 위치 (자료구조로 배열 사용)

2. push : 저장소에 자료를 저장하기 (append 메서드)


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
   
3. pop : 저장소에서 삽입한 자료의 역순으로 자료를 꺼낸다 (pop 메서드)


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

