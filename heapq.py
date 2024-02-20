import heapq

class GenericHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

# Example usage:

# Create a heap instance
heap = GenericHeap()

# Push various types of data into the heap
heap.push(10)
heap.push(5.5)
heap.push("hello")
heap.push((1, 2, 3))  # Tuple as custom data structure

# Pop elements from the heap
print(heap.pop())  # Output: 5.5
print(heap.pop())  # Output: 10
print(heap.pop())  # Output: hello
print(heap.pop())  # Output: (1, 2, 3)

# Pushing and popping empty heap
heap.push(3)
print(heap.pop())  # Output: 3

# Trying to pop from an empty heap
print(heap.pop())  # Output: None
