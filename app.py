def count_sort_letters(array, size, col, base, max_len):
  output   = [0] * size
  count    = [0] * (base + 1) 
  min_base = ord('a') - 1 

  for item in array: 
    letter = ord(item[col]) - min_base if col < len(item) else 0
    count[letter] += 1

  for i in range(len(count)-1):  
      count[i + 1] += count[i]

  for item in reversed(array):

    letter = ord(item[col]) - min_base if col < len(item) else 0
    output[count[letter] - 1] = item
    count[letter] -= 1

  return output

def radix_sort_letters(array, max_col = None):
  if not max_col:
    max_col = len(max(array, key = len)) 

  for col in range(max_col-1, -1, -1):
    array = count_sort_letters(array, len(array), col, 26, max_col)

  return array

lst = ['aa', 'a', 'ab', 'abs', 'asd', 'avc', 'axy', 'abid']
print(radix_sort_letters(lst))