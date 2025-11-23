def fib(n):
    a = 1
    b = 1
    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(str(a)+"\n")
            yield a
            a,b = b, a+b

fib200 = list(fib(200))
print(fib200[-1])