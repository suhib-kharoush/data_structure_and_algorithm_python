def quick_sort(arr, i, j):
    if i < j:
        pivot = partition(arr, i, j)
        quick_sort(arr, i, pivot-1)
        quick_sort(arr, pivot + 1, j)

    return arr
def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right-=1
        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    return right

test_quick_list = [8,4,23,42,16,15]
print(quick_sort(test_quick_list, 0, len(test_quick_list) - 1))