def factorial(n):
    """ Precondicion: n entero >= 0 
     Devuelve : n!"""
    assert n>=0
    print(f"factorial({n})")
    if n == 0:
        return 1
    return n * factorial (n - 1)


print(factorial(3))

print(factorial(8))

def fib(n):
    """ Precondicion: n >= 0.
    Devuelve: el numero de Fibonacci numero n."""
    assert n>=0
    print(f"fib({n})")
    if n == 0 or n == 1:
        return n
    return fib (n - 1) + fib (n - 2)

print("Fibonacci 0")
print(fib(0))
print("")
print("Fibonacci 1")
print(fib(1))
print("")
print("Fibonacci 5")
print(fib(5))