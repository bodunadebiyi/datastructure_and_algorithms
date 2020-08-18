'''
K = Number of houses
N = Numnber of colours
Cost array = Cost to paint house a certain compile
i.e K = 5
N = 4
Cost array = [
  [4, 8, 9],
  [11, 1, 20],
  [33, 21, 7],
  [44, 18, 22, 3],
  [92, 99, 20, 80]
]
'''

def get_best_cost(cost_options, index_to_exclude=-1):
  best_cost = None
  best_index = -1

  for index in range(len(cost_options)):
    current_cost = cost_options[index]
    if index == index_to_exclude:
      continue
    if best_cost == None or best_cost > current_cost:
      best_cost = current_cost
      best_index = index

  return best_cost, best_index

def get_best_cost_for_houses(cost_array):
  total_cost = 0
  index_to_exclude = -1

  for list_of_cost in cost_array:
    best_cost, best_index = get_best_cost(list_of_cost, index_to_exclude)
    total_cost += best_cost
    index_to_exclude = best_index

  return total_cost

cost_array = [
  [4, 8, 9, 2],
  [11, 1, 20, 16],
  [33, 21, 7, 25],
  [44, 18, 22, 3],
  [92, 99, 20, 80]
]

print(get_best_cost_for_houses(cost_array))