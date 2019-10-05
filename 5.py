i=1
def DivsiableCheck(num):
    for i in range(1,21):
        if num%i!=0:
            return False
    return True
while DivsiableCheck(i)!=True:
    i+=1
print(i)
