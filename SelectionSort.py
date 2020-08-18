def selection_sort(arr, starting_point=0):
    if starting_point == len(arr):
        return
  
    smallest = min(arr[starting_point:len(arr)])
    smallest_index = arr.index(smallest)

    if smallest_index != starting_point:
        tmp = arr[starting_point]
        arr[starting_point] = smallest
        arr[smallest_index] = tmp

    selection_sort(arr, starting_point + 1)

