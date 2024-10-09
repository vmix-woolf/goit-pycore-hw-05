def caching_fibonacci() -> int:
    def fibonacci(n: int)-> int:
        '''Calculates n-th fibonacci number with memoization technique
        ARGS: n: n-th fibonacci number
        RETURNS: Value of the n-th fibonacci number  
        '''
        cache = {}
        if n <= 0:
            return 0

        if n == 1:
            return 1
        
        if n not in cache:  # if n number isn't yet in cache, calculates it by the formula and save it
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        # if not, immediately return its value
        return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(fib(5))
print(fib(10))
print(fib(15))
print(fib(32))
