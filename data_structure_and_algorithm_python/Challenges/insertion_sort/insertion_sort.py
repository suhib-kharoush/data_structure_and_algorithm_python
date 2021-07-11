def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp=arr[i]

        while j >= 0and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
    return arr

if __name__=='__main__':
    arr = [8,4,23,42,16,15]
    print(insertion_sort(arr))
    arr2 = [20,18,12,8,5,-2]
    print(insertion_sort(arr2))
    arr3 = [5,12,7,5,5,7]
    print(insertion_sort(arr3))
    arr4 = [2,3,5,7,13,11]
    print(insertion_sort(arr4))


