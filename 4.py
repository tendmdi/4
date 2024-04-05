#замыкание
def fibonacci():
    a, b = 0, 1
    def fibonaccinext():
        nonlocal a, b
        a, b = b, a + b
        return a
    return fibonaccinext
zamikanie = fibonacci()
for _ in range(10):
    print(zamikanie())


#Декоратор для кэширования   
def decorator(zamikanie):  
    k = {}
    def func(n):
        def fibonacci(n):
            if n in k:
                return k[n]
            result = zamikanie(n)
            k[n] = result
            print(k)
            return result
        return fibonacci(n)
    return func
@decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(fibonacci(3))
print(fibonacci(6))

