def check_if_symmetric(string):
  reverse = string[::-1]
  return reverse == string

print(check_if_symmetric("ew"))
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
convert_to_numbers("a v c d e f")

def convert_to_letters(word):
  d = {
    0: " ", 1: "a", "b": 2, "c": 3, "d": 4, "e": 5,   "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "k": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "x": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
  }
  numbers = []
  for letter in word:
    num = d[letter]
    numbers.append(num)
  print(numbers)
  return word
convert_to_letters([0, 1])