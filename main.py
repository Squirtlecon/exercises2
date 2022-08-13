def check_if_symmetric(string):
  s = string
  t1 = s[::-1]
  if t1 == s:
    print("true")
    return True
  else:
    print("false")
    return False
check_if_symmetric("1231")

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
convert_to_numbers("a b c d e f g h i j k l m n o p q r s t u v w x y z")