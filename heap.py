class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        # Bit manipulation: (i-1) >> 1 is equivalent to (i-1) // 2
        return (i - 1) >> 1

    def left_child(self, i):
        # Bit manipulation: (2*i) + 1 is equivalent to (2*i) << 1 | 1
        return (i << 1) | 1

    def right_child(self, i):
        # Bit manipulation: (2*i) + 2 is equivalent to (2*i) << 1 | 2
        return (i << 1) | 2

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val

    def heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None


heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)

print("Minimum element:", heap.get_min())  
print("Extracted min:", heap.extract_min())  
print("Minimum element:", heap.get_min())  
