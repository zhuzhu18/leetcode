def getLeastNumbers(arr, k: int):
    return quickSearch(arr, k, 0, len(arr) - 1)

def partition(arr, start, end):
    pivot = arr[start]
    l = start + 1
    r = end
    while l <= r:
        if arr[l] >= pivot and arr[r] <= pivot:
            arr[l], arr[r] = arr[r], arr[l]
        if arr[l] <= pivot:
            l += 1
        if arr[r] >= pivot:
            r -= 1
    arr[r], arr[start] = arr[start], arr[r]
    return r


def quickSearch(arr, k, start, end):
    tmp = partition(arr, start, end)
    if tmp == k - 1:
        return arr[:k]
    elif tmp < k - 1:
        return quickSearch(arr, k, tmp + 1, end)
    else:
        return quickSearch(arr, k, start, tmp - 1)

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
k = 3
c = getLeastNumbers(a, k)
print(c)