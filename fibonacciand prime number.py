def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    print(f"Primes up to {n}: {primes}")

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    print(f"Fibonacci series up to {n}: {fib_series}")

# Example
prime=int(input("enter number of prime number  upto print:"))
fib=int(input("enter number of  fibonacci number upto print:"))
generate_primes(prime)
fibonacci(fib)
