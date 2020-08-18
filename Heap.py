class Heap:
    items = []
    size = 0

    def get_left_child_index(self, parent_index):
        return (parent_index * 2) + 1

    def get_right_child_index(self, parent_index):
        return (parent_index * 2) + 2
    
    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, parent_index):
        return self.get_left_child_index(parent_index) < self.size

    def has_right_child(self, parent_index):
        return self.get_right_child_index(parent_index) < self.size

    def has_parent(self, child_index):
        return self.get_parent_index(child_index) >= 0

    def left_child(self, parent_index):
        return self.items[self.get_left_child_index(parent_index)]

    def right_child(self, parent_index):
        return self.items[self.get_right_child_index(parent_index)]

    def parent(self, child_index):
        return self.items[self.get_parent_index(child_index)]

    def swap(self, index_one, index_two):
        self.items[index_one], self.items[index_two]  = self.items[index_two], self.items[index_one]

    def peek(self):
        if self.size == 0:
            raise Exception('Array is empty')
        return self.items[0]

    def poll(self):
        if self.size == 0:
            raise Exception('Array is empty')

        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item):
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1


        while self.has_parent(index) and self.parent(index) < self.items[index]:
            self.swap(index, self.get_parent_index(index))
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0

        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)
            index = smaller_child_index


def heapify_down(arr, i, size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], a[i]
        heapify_down(arr, largest, size)


def run_heap_sort(arr):
    size = len(arr)
    non_leaf_node_index = size // 2 - 1

    # builds heap
    for i in range(non_leaf_node_index, -1, -1):
        heapify_down(arr, i, size)


    # runs heap sort
    for i in range(size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr, 0, i)

a = [1000, 1201, 10, 30, 3, 45, 1, 78, 101, 16, 98]
run_heap_sort(a)
print(a)

'''
                        1201
                1000                      45
        101              98        10           1     
78            30     16       

'''
[30, 98, 78, 45, 1, 10, 3, 16, 101]
[30, 98, 78, 101, 1, 10, 3, 16, 45]


heap = Heap()
heap.add(10)
heap.add(30)
heap.add(3)
heap.add(45)
heap.add(1)
heap.add(78)
heap.add(101)
heap.add(16)
heap.add(98)

# print(heap.items)