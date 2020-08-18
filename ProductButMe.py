def product_but_me_v2(arr):
  total_product = 1
  counter = 0
  arr_size = len(arr)

  while counter < arr_size:
    total_product *= arr[counter]
    counter += 1

  counter = 0

  while counter < arr_size:
    value = arr[counter]
    arr[counter] = int(total_product/value)
    counter += 1

  return arr


def product_but_me(arr):
  result = []
  arr_size = len(arr)
  counter = 0
  
  while counter < arr_size:
    counter2 = 0
    product = 1
    while counter2 < arr_size:
      if counter2 != counter:
        product *= arr[counter2]
      counter2 += 1

    result.append(product)
    counter += 1

  return result