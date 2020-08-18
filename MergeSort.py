def merge(left, right, A):
  i = 0
  j = 0
  k = 0

  while k < len(A):
    if i >= len(left) and j < len(right):
      A[k] = right[j]
      j += 1
    elif j >= len(right) and i < len(left):
      A[k] = left[i]
      i += 1
    elif left[i] < right[j]:
      A[k] = left[i]
      i += 1
    elif left[i] > right[j]:
      A[k] = right[j]
      j += 1

    k += 1



def mergesort(arr):
    size = len(arr)
    if size < 2:
        return

    midpoint = round(size/2)
    left = arr[:midpoint]
    right = arr[midpoint:]

    mergesort(left)
    mergesort(right)

    merge(left, right, arr)