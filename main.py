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


word = "abc d"
word = list(word)
y= len(word)
z = word.index

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
print(word)