largest=0
def Reverse(num):
    num=str(num)
    new_num=""
    for i in range(1,(len(num)+1)):
        var=int("-"+str(i))
        new_num=new_num+num[var]
    return str(new_num)
def PalindromeTest(num):
    num=str(num)
    if Reverse(num)==num:
        return True
    else:
        return False
numbers=range(100,1000)
for i in numbers:
    for x in numbers:
        if PalindromeTest(x*i)==True:
            if x*i>largest:
                largest=x*i
print(largest)
