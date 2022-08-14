def check_if_symmetric(string):
  s = string
  t1 = s[::-1]
  if t1 == s:
    print("true")
    return True
  else:
    print("false")
    return False

def convert_to_numbers(string):
  word = string
  word = list(word)
  for h in word:
    if h == " ":
      i = word.index(" ")
      word = word[:i]+['0']+word[i+1:]
    if h == "a":
      i = word.index("a")
      word = word[:i]+['1']+word[i+1:]
    if h == "b":
      i = word.index("b")
      word = word[:i]+['2']+word[i+1:]
    if h == "c":
      i = word.index("c")
      word = word[:i]+['3']+word[i+1:]
    if h == "d":
      i = word.index("d")
      word = word[:i]+['4']+word[i+1:]
    if h == "e":
      i = word.index("e")
      word = word[:i]+['5']+word[i+1:]
    if h == "f":
      i = word.index("f")
      word = word[:i]+['6']+word[i+1:]
    if h == "g":
      i = word.index("g")
      word = word[:i]+['7']+word[i+1:]
    if h == "h":
      i = word.index("h")
      word = word[:i]+['8']+word[i+1:]
    if h == "i":
      i = word.index("i")
      word = word[:i]+['9']+word[i+1:]
    if h == "j":
      i = word.index("j")
      word = word[:i]+['10']+word[i+1:]
    if h == "k":
      i = word.index("k")
      word = word[:i]+['11']+word[i+1:]
    if h == "l":
      i = word.index("l")
      word = word[:i]+['12']+word[i+1:]
    if h == "m":
      i = word.index("m")
      word = word[:i]+['13']+word[i+1:]
    if h == "n":
      i = word.index("n")
      word = word[:i]+['14']+word[i+1:]
    if h == "o":
      i = word.index("o")
      word = word[:i]+['15']+word[i+1:]
    if h == "p":
      i = word.index("p")
      word = word[:i]+['16']+word[i+1:]
    if h == "q":
      i = word.index("q")
      word = word[:i]+['17']+word[i+1:]
    if h == "r":
      i = word.index("r")
      word = word[:i]+['18']+word[i+1:]
    if h == "s":
      i = word.index("s")
      word = word[:i]+['19']+word[i+1:]
    if h == "t":
      i = word.index("t")
      word = word[:i]+['20']+word[i+1:]
    if h == "u":
      i = word.index("u")
      word = word[:i]+['21']+word[i+1:]
    if h == "v":
      i = word.index("v")
      word = word[:i]+['22']+word[i+1:]
    if h == "w":
      i = word.index("w")
      word = word[:i]+['23']+word[i+1:]
    if h == "x":
      i = word.index("x")
      word = word[:i]+['24']+word[i+1:]
    if h == "y":
      i = word.index("y")
      word = word[:i]+['25']+word[i+1:]
    if h == "z":
      i = word.index("z")
      word = word[:i]+['26']+word[i+1:]
  print(word)
  
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

  

convert_to_letters([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])