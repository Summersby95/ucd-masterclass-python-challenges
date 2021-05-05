n = 13

def FizzBuzz(n):
    if ((n % 3 == 0) & (n % 5 == 0)):
        return "FizzBuzz"
    elif (n % 5 == 0):
        return "Buzz"
    elif (n % 3 == 0):
        return "Fizz"
    else:
        return n

print(FizzBuzz(n))
