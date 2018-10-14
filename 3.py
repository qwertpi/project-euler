highest_prime=0
n=600851475143
def PrimeTest(number):
    potential_prime=True
    for i in range(2,number):
        if number%i==0:
            potential_prime=False
            break
    return potential_prime
while PrimeTest(n)!=True:
    for p in range(3,n,2):
        potential_prime=PrimeTest(p)
        if potential_prime:
            if n%p==0:
                n=int(n/p)
                if p>highest_prime:
                    highest_prime=p
                break
if n>highest_prime:
    highest_prime=n
print(highest_prime)
