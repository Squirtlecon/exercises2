def check_if_symmetric(string):
  reverse = string[::-1]
  return reverse == string

def convert_to_numbers(word):
  d = {
      " ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,   "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "k": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "x": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
  }
  numbers = []
  for letter in word:
    num = d[letter]
    numbers.append(num)
  print(numbers)
  return word
def convert_to_letters(array):
  d = {
    0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "x", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"
  }
  letters = []
  for num in array:
    lett = d[num]
    letters.append(lett)
  print(letters)
  return letters
def get_intersection(array1, array2):
    array3 = [value for value in array1 if value in array2]
    print(array3)
    return array3
def get_union(array1, array2):
  array3 = array1 +array2
  final_list = []
  for num in array3:
        if num not in final_list:
            final_list.append(num)
  print(final_list)
  return final_list
def count_characters(string):
    string = string.lower()
    d = {}
    for n in string:
        char = d.keys()
        if n in char:
            d[n] += 1
        else:
            d[n] = 1
    return d
def is_prime(N):
  import math
  half = math.floor(N/2)
  for possible_divsor in range(2, half+1):
    if N%possible_divsor==0:
      print("false")
      return False
  print("true")
  return True

def binary_to_decimal(string):
  string = list(string)
  string = string[::-1]
  total = 0
  for exponent in range(len(string)):
    cofficent = int(string[exponent])
    value=cofficent*2**exponent
    total=total + value
  print(total)
  return total
def hexadecimal_to_decimal(string):
  string = list(string)
  string = string[::-1]
  total = 0
  for exponent in range(len(string)):
    cofficent = int(string[exponent])
    value=cofficent*16**exponent
    total=total + value
  print(total)
  return total
def decimal_to_binary(string):
  string = int(string)
  if string >= 1:
    decimal_to_binary(string // 2)
    print(string % 2, end = '')
decimal_to_binary('35')