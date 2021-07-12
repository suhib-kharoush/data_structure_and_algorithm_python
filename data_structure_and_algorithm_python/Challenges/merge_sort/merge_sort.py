def mergeSort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j< len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1 
        k += 1
    if i == len(left):
        for item in right[j:]:
            arr[k] = item
            k += 1


if __name__=="__main__":
    list1=[8,4,23,42,16,15]
    print(mergeSort(list1))
    list_2=[20,18,12,8,5,-2]
    print(mergeSort(list_2))
    list_3=[5,12,7,5,5,7]
    print(mergeSort(list_3))
    list_4=[2,3,5,7,13,11]
    print(mergeSort(list_4))