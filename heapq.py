import heapq

# Example 1: Min-heap with integers
int_heap = []
heapq.heappush(int_heap, 10)
heapq.heappush(int_heap, 5)
heapq.heappush(int_heap, 7)
print("Min element:", int_heap[0])  # Output: 5
print("Heap:", int_heap)  # Output: [5, 10, 7]

# Example 2: Min-heap with floats
float_heap = []
heapq.heappush(float_heap, 3.14)
heapq.heappush(float_heap, 1.2)
heapq.heappush(float_heap, 2.71)
print("Min element:", float_heap[0])  # Output: 1.2
print("Heap:", float_heap)  # Output: [1.2, 3.14, 2.71]

# Example 3: Min-heap with custom data structures (e.g., tuples)
custom_heap = []
heapq.heappush(custom_heap, (3, "Alice"))
heapq.heappush(custom_heap, (1, "Bob"))
heapq.heappush(custom_heap, (2, "Charlie"))
print("Min element:", custom_heap[0])  # Output: (1, 'Bob')
print("Heap:", custom_heap)  # Output: [(1, 'Bob'), (3, 'Alice'), (2, 'Charlie')]
