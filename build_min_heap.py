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
            min_index = i
            l = self.left(i)
            r = self.right(i)
            if l < len(self.heap) and self.heap[l] < self.heap[min_index]:
                min_index = l
            if r < len(self.heap) and self.heap[r] < self.heap[min_index]:
                min_index = r
            if min_index != i:
                self.swap(i, min_index)
                i = min_index
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)
        return min_element

    def build_min_heap(self, arr):
        self.heap = arr[:]
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.heapify_down(i)

# Example usage:
arr = [4, 10, 3, 5, 1]
min_heap = MinHeap()
min_heap.build_min_heap(arr)
print(min_heap.heap)  # Output: [1, 4, 3, 10, 5]
