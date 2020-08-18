def GetLeastNumbers_Solution(tinput, k):
    heap = [-1]
    heap.extend(tinput[:k])
    adjust(heap)
    for t in tinput[k:]:
        if t < heap[1]:
            heap[1] = t
            adjust(heap)
    return heap[1:]

def adjust(heap):
    for parent in range(len(heap) // 2, 0, -1):
        while parent * 2 <= len(heap)-1:
            child = 2 * parent
            if child + 1 <= len(heap)-1 and heap[child+1] > heap[child]:
                child += 1
            if heap[child] > heap[parent]:
                heap[child], heap[parent] = heap[parent], heap[child]
                parent = child
            else:
                break

a = [4,5,1,6,2,7,3,8]
b = GetLeastNumbers_Solution(a, 4)
print(b)