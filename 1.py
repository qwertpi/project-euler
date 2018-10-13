multiples=[]
for i in range(1,1000):
    if i%3==0 or i%5==0:
        multiples.append(i)
answer=0
for el in multiples:
    answer+=el
print(answer)
