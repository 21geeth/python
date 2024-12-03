m=float(input())
a=str(m)
n=len(a)
def is_even(a):
    ds=False
    for i in range(n-1,-1,-1):
        if (a[i]=='0' and ds==False):
            continue
        if (a[i]=='.'):
            ds=True
            continue
        if(a[i].isdigit() and (int(a[i]))%2==0):
            return True
        return False
if is_even(a)==True:
    print("even")
else:
    print("odd")
