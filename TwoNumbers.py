def numbers_possible(arr, added):
  arr_map = {}
  arr_size = len(arr)
  for i in range(arr_size):
    arr_map[arr[i]] = i
  
  for i in range(arr_size):
    value = arr[i]
    difference = added - value
    if (difference in arr_map) and (i != arr_map[difference]):
      return (value, difference)

print(numbers_possible([10, 15, 3, 7], 10))