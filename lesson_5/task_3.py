def fib(n):
    fib1 = 0
    fib2 = 1
    
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1
        n -= 1


if __name__ == '__main__':
    for number in fib(10):
        print(number)
    