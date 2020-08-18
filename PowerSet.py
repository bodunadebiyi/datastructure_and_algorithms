def generate_starting_bitstring(size):
  starting = []
  for i in range(size):
    starting.append(0)
  return starting


def generate_bitstring(size):
  starting_bitstring = generate_starting_bitstring(size)
  bitstrings = []
  bitstring_generator(0, starting_bitstring, bitstrings)
  return bitstrings


def convert_binary_to_set(single_set, binary):
  result = ''
  set_size = len(single_set)

  for i in range(set_size):
    if binary[i] == 1:
      result += single_set[i]

  return result


def powerset(arr):
  set_size = len(arr)
  binary_counter = generate_bitstring(set_size)
  power_set = list(map(lambda x: convert_binary_to_set(arr, x), binary_counter))

  return power_set


def bitstring_generator(n, B, bitstrings):
  if n == len(B):
    bitstrings.append(list(B))
  else:
    B[n] = 1
    bitstring_generator(n+1, B, bitstrings)
    B[n] = 0
    bitstring_generator(n+1, B, bitstrings)


def multiply_set(string):
  product = 1
  for char in string:
    product *= int(char)
  return product


def colorful_string(number_to_check):
  str_arr = list(str(number_to_check))
  power_set = powerset(str_arr)
  set_hash = {}
  for item in power_set:
    multiplied = multiply_set(item)
    if multiplied in set_hash:
      return False
    else:
      set_hash[multiplied] = 1
  return True


print(colorful_string(3245))
print(colorful_string(123))
print(colorful_string(326))

 