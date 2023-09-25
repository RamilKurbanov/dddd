def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(N):
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Пример использования:
N = 10  # Замените на нужное вам количество простых чисел
prime_generator = generate_primes(N)
for prime in prime_generator:
    print(prime)