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
  for h in word:
    if h == "a":
      i = word.index("a")
    word = word[:i]+['1']+word[i+1:]
  for h in word:
    if h == "b":
      i = word.index("b")
      word = word[:i]+['2']+word[i+1:]
  for h in word:
    if h == "c":
      i = word.index("c")
      word = word[:i]+['3']+word[i+1:]


  for h in word:
    if h == "d":
      i = word.index("d")
      word = word[:i]+['4']+word[i+1:]
  for h in word:
    if h == "e":
      i = word.index("e")
      word = word[:i]+['5']+word[i+1:]
  for h in word:
    if h == "f":
      i = word.index("f")
      word = word[:i]+['6']+word[i+1:]
  for h in word:
    if h == "g":
      i = word.index("g")
      word = word[:i]+['7']+word[i+1:]
  for h in word:
    if h == "h":
      i = word.index("h")
      word = word[:i]+['8']+word[i+1:]
  for h in word:
    if h == "i":
      i = word.index("i")
      word = word[:i]+['9']+word[i+1:]
  for h in word:
    if h == "j":
      i = word.index("j")
      word = word[:i]+['10']+word[i+1:]
  print(word)
    
convert_to_numbers("a b c d e f g h i j k l m n o p")