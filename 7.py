i=3
def PrimeTest(number):
    potential_prime=True
    for i in range(2,number):
        if number%i==0:
            potential_prime=False
            break
    return potential_prime
primes=[2]
while len(primes)<10001:
    if PrimeTest(i)==True:
        primes.append(i)
    i+=2
print(primes[-1])
