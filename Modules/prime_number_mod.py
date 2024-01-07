"""Finding Prime Numbers"""
def count_primes(num):
    """Checking For Prime Numbers"""
    # Check for 0 or 1 input
    if num < 2:
        return 0
    ##############
    # 2 or greater
    ##############
    # Store our prime numbers
    primes = [2]
    # Counter going up to the input number
    x = 3
    # x is going going through every number up to input number
    while x <= num:
        # Check if x is prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))

count_primes(10)
