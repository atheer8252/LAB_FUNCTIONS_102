def find_primes(start, end):
    for num in range(start, end + 1):
        # only consider numbers greater than 1
        if num > 1:
            # assume num is prime
            is_prime = True
            # check divisibility from 2 up to num-1
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)

# Example usage
find_primes(2, 20)