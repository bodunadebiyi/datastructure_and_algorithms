def Quicksort(A, start=0, stop=None):
    if stop == None:
        stop = len(A)

    if start >= stop:
        return

    pivot_index = run_partitioner(A, start, stop)

    Quicksort(A, start, pivot_index - 1)
    Quicksort(A, pivot_index + 1)

def run_partitioner(A, start, stop):
    counter = start + 1
    pivot_index = start
    pivot_value = A[pivot_index]

    while counter < stop:
        curr_value = A[counter]
        curr_index = counter

        if curr_value < pivot_value and curr_index > pivot_index:
            move(A, pivot_index, curr_index)
            pivot_index += 1

        counter += 1

    return pivot_index

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def move(A, to, frm):
    hole = frm
    hole_value = A[frm]
    counter = frm

    while hole > to:
        A[hole] = A[hole-1]
        hole -= 1
    A[hole] = hole_value



# b = [1000092, 12, 100, 122, 234, 55, 12, 660, 12, 1, 2, 2, 1009, 59]
# Quicksort(b)
# print(b)




# def run_partitioner(A, start, stop):
#     counter = start
#     pivot_index = stop
#     pivot_value = A[pivot_index]

#     while counter < stop:
#         curr_larger_than_pivot = (A[counter] > pivot_value) and counter < pivot_index
#         curr_smaller_than_pivot = (A[counter] < pivot_value) and counter > pivot_index

#         if curr_larger_than_pivot or (curr_smaller_than_pivot and abs(counter - pivot_index) == 1):
#             swap(A, counter, pivot_index)
#             pivot_index = counter
#         elif curr_smaller_than_pivot:
#             swap(A, pivot_index + 1, counter)
#             swap(A, pivot_index, pivot_index + 1)
#             pivot_index = pivot_index + 1

#         counter += 1

#     return pivot_index