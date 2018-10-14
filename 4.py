largest=0
def PalindromeTest(num):
    num=str(num)
    prev_char=num[1]
    for char in num:
        if char==prev_char:
            pass
        else:
            return False
            break
        prev_char=char
    return True
numbers=range(100,1000)
for i in numbers:
    for x in numbers:
        if PalindromeTest(x*i)==True:
            if x*i>largest:
                largest=x*i
print(largest)
