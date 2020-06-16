# Faster implementation of fibonacci
def fib_fast(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib_fast(n-1, computed) + fib_fast(n-2, computed)
    return computed[n]

# Slower implementation of fibonacci
def fib_slow(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_slow(n-1) + fib_slow(n-2)

if __name__ == '__main__':
    # define what nth fibonacci number we want to find and output result
    n = 12
    print("Nth fibonacci number where n=" + str(n) + ": ")
    print("Slower recursive function: " + str(fib_slow(n)))
    print("Faster recursive function: " + str(fib_fast(n)))
