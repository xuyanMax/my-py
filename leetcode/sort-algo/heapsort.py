def heap_sort(arr):
    n = len(arr)
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


arr = [5, 2, 9, 1, 5, 6]
heap_sort(arr)
print(arr)
