str1=input()
str2=input()
if len(str1)!=len(str2):
  print("not anagram")
else:
  str1=sorted(str1)
  str2=sorted(str2)
  if str1==str2:
    print("anagram")
