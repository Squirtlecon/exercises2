def check_if_symmetric(string):
  s = string
  s1 = s[:len(s)//2]
  s2 = s[len(s)//2:]
  t1 = s1 [::-1]
  if t1== s2:
    return True
  if t1 != s2:
    return False


word = "abcd"
word = list(word)
y= len(word)
z = word.index
for h in word:
    if h == "a":
      i = word.index("a")
    word = word[:i]+['1']+word[i+1:]
print(word)