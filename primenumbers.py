n = 100

def PrimeFind(n):
    primes = []
    for num in range(2, n):
        div = 0
        for i in range(2, num):
            if (num % i == 0):
                div += 1
        
        if div == 0:
            primes.append(num)
    return len(primes)

print(PrimeFind(n))