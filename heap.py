class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        while True:
            smallest = i
            l = self.left(i)
            r = self.right(i)

            if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
                smallest = l

            if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest != i:
                self.swap(i, smallest)
                i = smallest
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

# Example usage:
heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(4)
heap.insert(5)
print(heap.extract_min())  # Output: 1
print(heap.extract_min())  # Output: 2
print(heap.extract_min())  # Output: 3
print(heap.extract_min())  # Output: 4
print(heap.extract_min())  # Output: 5
print(heap.extract_min())  # Output: None (heap is empty)
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        while True:
            smallest = i
            l = self.left(i)
            r = self.right(i)

            if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
                smallest = l

            if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest != i:
                self.swap(i, smallest)
                i = smallest
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

# Example usage:
heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(4)
heap.insert(5)
print(heap.extract_min())  # Output: 1
print(heap.extract_min())  # Output: 2
print(heap.extract_min())  # Output: 3
print(heap.extract_min())  # Output: 4
print(heap.extract_min())  # Output: 5
print(heap.extract_min())  # Output: None (heap is empty)
