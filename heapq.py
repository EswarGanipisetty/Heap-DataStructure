import heapq

class GenericHeap:
    def __init__(self):
        self._heap = []

    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        if self._heap:
            return heapq.heappop(self._heap)
        else:
            raise IndexError("pop from an empty heap")

    def peek(self):
        if self._heap:
            return self._heap[0]
        else:
            return None

    def __len__(self):
        return len(self._heap)

# Example usage:
if __name__ == "__main__":
    # Example with integers
    integer_heap = GenericHeap()
    integer_heap.push(10)
    integer_heap.push(5)
    integer_heap.push(15)
    print("Integer Heap:")
    while len(integer_heap) > 0:
        print(integer_heap.pop(), end=' ')
    print()

    # Example with floats
    float_heap = GenericHeap()
    float_heap.push(10.5)
    float_heap.push(5.2)
    float_heap.push(15.7)
    print("\nFloat Heap:")
    while len(float_heap) > 0:
        print(float_heap.pop(), end=' ')
    print()

    # Example with custom data structures (tuples)
    custom_heap = GenericHeap()
    custom_heap.push((3, 'apple'))
    custom_heap.push((1, 'banana'))
    custom_heap.push((2, 'orange'))
    print("\nCustom Heap:")
    while len(custom_heap) > 0:
        print(custom_heap.pop(), end=' ')
    print()
  
