evens=[]
def fib_gen(num):
    numbers=[1,2]
    prev_1=2
    prev_2=1
    for i in range(3,num+1):
        numbers.append(prev_1+prev_2)
        prev_2=prev_1
        prev_1=numbers[-1]
    return numbers
numbers=fib_gen(1000)
for num in numbers:
    if num<=4000000:
        if num%2==0:
            evens.append(num)
answer=0
for el in evens:
    answer+=el
print(answer)
