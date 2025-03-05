class MinHeap:
    def __init__(self):
        self.heap = []  # 힙을 저장할 빈 리스트 초기화

    # 힙에 새로운 요소를 추가
    def heappush(self, item):
        self.heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
        self._siftup(len(self.heap) - 1)  # 힙 속성을 유지하도록 sift-up 연산 수행

    # 힙에서 최소 요소를 제거하고 반환
    def heappop(self):
        if len(self.heap) == 0:
            raise IndexError("힙이 비었습니다.")  # 힙이 비어 있는 경우 예외 발생
        if len(self.heap) == 1:
            return self.heap.pop()  # 힙에 요소가 하나만 있는 경우 그 요소를 반환
        root = self.heap[0]  # 루트 요소 저장
        self.heap[0] = self.heap.pop()  # 마지막 요소를 루트로 이동
        self._siftdown(0)  # 힙 속성을 유지하도록 sift-down 연산 수행
        return root  # 제거된 루트 요소 반환

    # 주어진 리스트을 힙으로 변환
    def heapify(self, array):
        self.heap = array[:]  # 리스트의 복사본을 힙으로 사용
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self._siftdown(i)  # 리스트의 중간부터 시작하여 모든 노드에 대해 sift-down 연산 수행

    # 삽입 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftup(self, idx):
        parent = (idx - 1) // 2  # 부모 노드의 인덱스 계산
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]  # 자식이 부모보다 작은 경우 교환
            idx = parent  # 인덱스를 부모로 업데이트
            parent = (idx - 1) // 2  # 새로운 부모 인덱스 계산

    # 삭제 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
    def _siftdown(self, idx):
        n = len(self.heap)
        smallest = idx  # 가장 작은 요소의 인덱스 초기화
        left = 2 * idx + 1  # 왼쪽 자식의 인덱스 계산
        right = 2 * idx + 2  # 오른쪽 자식의 인덱스 계산

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left  # 왼쪽 자식이 현재 가장 작은 요소보다 작은 경우 업데이트
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right  # 오른쪽 자식이 현재 가장 작은 요소보다 작은 경우 업데이트
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]  # 부모와 자식을 교환
            self._siftdown(smallest)  # 자식 노드에 대해 재귀적으로 sift-down 연산 수행

    def __str__(self):
        return str(self.heap)  # 힙의 문자열 표현 반환

min_heap = MinHeap()
min_heap.heappush(3)
min_heap.heappush(1)
min_heap.heappush(2)

print(min_heap)  # [1, 3, 2]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 3]