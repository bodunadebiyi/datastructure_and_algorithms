def bubble_sort(arr):
    arr_size = len(arr)
    i = 0
    while i < arr_size:
        j = 0
        while j < arr_size - 1 - i:
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            j += 1
        i += 1