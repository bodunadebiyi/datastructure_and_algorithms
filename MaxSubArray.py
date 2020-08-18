def max_of_sub_array(arr, n):
  counter = 0
  size = len(arr)

  while counter + (n - 1) < size:
    print(highest_value(arr[counter: counter+n]))
    counter += 1

def highest_value(arr):
  largest = None

  for item in arr:
    if largest == None or item > largest:
      largest = item

  return largest

max_of_sub_array([10, 5, 2, 7, 8, 7], 3)