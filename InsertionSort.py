def insertion_sort(arr):
  size = len(arr)
  counter = 1

  while counter < size:
    tmp = arr[counter]
    hole = counter

    while hole > 0 and arr[hole - 1] > tmp:
      arr[hole] = arr[hole - 1]
      hole -= 1
    arr[hole] = tmp
    counter += 1

a = [10, 3, 9, 1, 11, 2]
insertion_sort(a)
print(a)


