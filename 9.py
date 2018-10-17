from math import sqrt
from time import sleep
x=5000
while True:
    for a in range(1,x):
        for b in range(1,x):
            c=(a**2)+(b**2)
            if a<b and b<c:
                if sqrt(c)%1==0:
                    c=int(sqrt(c))
                    if a+b+c==1000:
                        print(a)
                        print(b)
                        print(c)
                        print(a*b*c)
                        raise Exception("Done!")
    x+=1000
