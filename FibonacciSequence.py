# Program to calculate the Fibonacci sequence to the nth number

def fib(n, hash = {}):
    if n in hash: return hash[n]
    if n<=2: return 1
    hash[n] = fib(n-1) + fib(n-2)
    return hash[n]

print(fib(3)) # 2
print(fib(5)) # 5
print(fib(7)) # 13
print(fib(50)) # 12586269025


    