n=float(input())
a=str(n)
m=len(a)
if a==a[::-1]:
  print("palindrome")
else:
  print("not palindrome")
