import asyncio
import threading
import time
import multiprocessing
import math

# Функции для АТ-04

# запускать с n = 699998
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    start_time = time.time()
    fibonacci(699998)
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)
    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    start_time = time.time()
    thread1 = threading.Thread(target=fibonacci, args=(699998,))
    thread2 = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    start_time = time.time()
    process1 = multiprocessing.Process(target=fibonacci, args=(699998,))
    process2 = multiprocessing.Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def fibonacci_async(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


async def trapezoidal_rule_async(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


async def asyncio_func():
    start_time = time.time()
    await asyncio.gather(
        fibonacci_async(699998),
        trapezoidal_rule_async(math.sin, 0, math.pi, 20000000)
    )
    end_time = time.time()
    print(f'asyncio time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()

    asyncio.run(asyncio_func())

    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 9
        trapezoidal_rule = 2.000000000000087
        sequence time:  4.79
        
        fibonacci = 9
        trapezoidal_rule = 2.000000000000087
        threads time:  4.99 
        
        fibonacci = 9
        trapezoidal_rule = 2.000000000000087
        processes time:  3.01
        
        fibonacci = 9
        trapezoidal_rule = 2.000000000000087
        asyncio time:  4.79
    """
