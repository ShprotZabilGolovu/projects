def fib_num(n):
    if n <= 1:
        return n
    else:
        return (fib_num(n-1) + fib_num(n-2))
    
n = 22

for i in range(n):
    print(fib_num(i))