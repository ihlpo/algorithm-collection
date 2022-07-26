def generate_primes(number):
    primes = []
    is_prime = [False, False] + [True] * (number - 1)

    for prime in range(2, number + 1):
        if is_prime[prime]:
            primes.append(prime)
            for i in range(prime, number + 1, prime):
                is_prime[i] = False
    return primes


print(generate_primes(18))