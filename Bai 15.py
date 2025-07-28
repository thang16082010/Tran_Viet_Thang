import math
kt=0
n=int(input())
if n<2:
    print("no")
else:
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            print("no")
            kt=1
    if kt==0:
        print("yes")