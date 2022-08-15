def check_if_symmetric(string):
  reverse = string[::-1]
  return reverse == string

print(check_if_symmetric("ew"))
def convert_to_numbers(word):
  word = list(word)
  d = {
      " ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,   "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "k": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "x": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
  }
  numbers = []
  for h in word:
    numbers.append(d[h])
  print(numbers)
  return word
convert_to_numbers("a v c d e f")

def convert_to_letters(array):
  word = array
  for h in word:
    if h == 0:
      i = word.index(0)
      word = word[:i]+[' ']+word[i+1:]
    if h == 1:
      i = word.index(1)
      word = word[:i]+['a']+word[i+1:]
    if h == 2:
      i = word.index(2)
      word = word[:i]+["b"]+word[i+1:]
    if h == 3:
      i = word.index(3)
      word = word[:i]+['c']+word[i+1:]
    if h == 4:
      i = word.index(4)
      word = word[:i]+['d']+word[i+1:]
    if h == 5:
      i = word.index(5)
      word = word[:i]+['e']+word[i+1:]
    if h == 6:
      i = word.index(6)
      word = word[:i]+['f']+word[i+1:]
    if h == 7:
      i = word.index(7)
      word = word[:i]+['g']+word[i+1:]
    if h == 8:
      i = word.index(8)
      word = word[:i]+['h']+word[i+1:]
    if h == 9:
      i = word.index(9)
      word = word[:i]+['i']+word[i+1:]
    if h == 10:
      i = word.index(10)
      word = word[:i]+['j']+word[i+1:]
    if h == 11:
      i = word.index(11)
      word = word[:i]+['k']+word[i+1:]
    if h == 12:
      i = word.index(12)
      word = word[:i]+["l"]+word[i+1:]
    if h == 13:
      i = word.index(13)
      word = word[:i]+["m"]+word[i+1:]
    if h == 14:
      i = word.index(14)
      word = word[:i]+["n"]+word[i+1:]
    if h == 15:
      i = word.index(15)
      word = word[:i]+['o']+word[i+1:]
    if h == 16:
      i = word.index(16)
      word = word[:i]+['p']+word[i+1:]
    if h == 17:
      i = word.index(17)
      word = word[:i]+['q']+word[i+1:]
    if h == 18:
      i = word.index(18)
      word = word[:i]+['r']+word[i+1:]
    if h == 19:
      i = word.index(19)
      word = word[:i]+['s']+word[i+1:]
    if h == 20:
      i = word.index(20)
      word = word[:i]+['t']+word[i+1:]
    if h == 21:
      i = word.index(21)
      word = word[:i]+['u']+word[i+1:]
    if h == 22:
      i = word.index(22)
      word = word[:i]+['v']+word[i+1:]
    if h == 23:
      i = word.index(23)
      word = word[:i]+['w']+word[i+1:]
    if h == 24:
      i = word.index(24)
      word = word[:i]+['x']+word[i+1:]
    if h == 25:
      i = word.index(25)
      word = word[:i]+['y']+word[i+1:]
    if h == 26:
      i = word.index(26)
      word = word[:i]+['z']+word[i+1:]
  print(word)
  return(word)
convert_to_letters([1,0,3,1,20])
  
