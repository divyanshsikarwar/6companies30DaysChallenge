import heapq

def findMaxN(n, numbers):
    if n == 0: return []
    heap = numbers[:n]
    heapq.heapify(heap)
    for k in numbers[n:]:
        if heap[0] < k:
            heapq.heapreplace(heap, k)
    return heap
