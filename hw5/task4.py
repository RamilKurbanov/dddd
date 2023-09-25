def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования:
fib_gen = fibonacci_generator()
for _ in range(10):  # Генерировать первые 10 чисел Фибоначчи
    print(next(fib_gen))