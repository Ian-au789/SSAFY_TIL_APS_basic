# Queue

: 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소를 먼저 삭제하는 자료구조 (FIFO)

- 삽입 : enQueue
- 삭제 : deQueue
- 생성 : createQueue
- 공백 확인 : isEmpty()
- 포화 확인 : isFull()
- 검색 (원소를 삭제 없이 반환) : Qpeek()

## 선형 큐

1. 1차원 배열 이용
2. 큐의 크기 = 배열의 크기
3. front : 저장된 첫 번째 원소의 인덱스
4. rear : 저장된 마지막 원소의 인덱스

- 초기 상태 : front = rear = -1
- 공백 상태 : front == rear
- 포화 상태 : rear == n - 1 (n : 배열의 크기)

스택은 후입선출이기 때문에 top 하나로 모든 동작 가능, 큐는 선입선출이기 때문에 맨 앞의 위치를 저장할 변수 하나 더 필요

<삽입>

    def enQueue(item):
    global rear
    if isFull() : print("Queue full")
    else:
        rear += 1
        Q[rear] = item

<삭제>
    
    def deQueue:
        if not isEmpty():
            front += 1
            return Q[front]

<공백 확인>

    def isEmpty()
        return front == rear

<포화 확인>

    def isFull():
        return rear == len(Q) - 1

<검색>

    def Qpeek():
        if isEmpty() : print("Queue_Empty)
        else : return Q[front+1]

## 원형 큐

1. 선형 큐를 이용해 원소의 삽입과 삭제를 계속 하면, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고 front = rear = -1인 포화 상태로 인식하여 더 이상 동작 불가. 
2. 매 연산마다 저장된 원소들을 배열의 앞부분으로 이동 시키면 해결되지만 많은 연산과 시간이 소요되어 효율적이지 못함

해결 : 1차원 배열을 사용하되 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태를 이룬다고 가정하고 사용

- 초기 공백 상태 : front = rear = mod
- 논리적 순환을 위해 마지막 인덱스인 n - 1을 가리킨 후 인덱스 0으로 이동 (rear = (rear + 1) % n)
- front가 있는 자리는 사용하지 않고 빈자리로 두면, 공백 상태와 포화 상태 구분 용이

<공백 확인>

    def isEmpty():
        return front == rear

<포화 확인>

    def isFull():
        return (rear + 1) % len(cQ) == front

<삽입>

    def enQueue(item):
        global rear
        if isFull():
            print("Queue_Full")
        else:
            rear = (rear + 1) % len(cQ)
            cQ[rear] = item

<삭제>
    
    def deQueue():
        global front
        if isEmpty():
            print("Queue_Empty")
        else:
            front = (front + 1) % len(cQ)
            return cQ[front]

## 여러 종류의 큐
### 연결 큐

: 단순 연결리스트를 이용한 큐

연결 리스트 : 각 노드가 저장하고 있는 값과 다음 값이 저장된 객체의 레퍼런스를 저장하고 있는 자료구조

배열을 이용한 큐보다 삽입 삭제가 훨씬 빠름

### deque (데크)

: 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트 류 컨테이너

    from collections import deque
        q = deque()
        q.append(1)            # enqueue
        t = q.pop(left)        # dequeue

### 우선순위 큐

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나감

### 큐의 활용

버퍼 : 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역
버퍼링 : 버퍼를 채우는 동작 및 버퍼를 활용하는 방식

