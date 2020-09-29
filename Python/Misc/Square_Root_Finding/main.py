# Problem Statement:
# Compute sqrt using various methods in Python3

import math

def sqrt_math(val):
    return math.sqrt(val)

def sqrt_operator(val):
    return val ** (1/2)

def sqrt_newtons_method(t_val, x=.1e-20, it=.1e-20, tol=.1e-20):
    while True:
        x = (1/2) * (x + (t_val / x))
        if abs(((x**2) - t_val) / t_val) < tol:
            return x
        x += it

def main():
    val = 55555 * 7777777
    print('~ Testing square root methods for value: ' + str(val) + ' ~\n')
    print('Built in math.sqrt:')
    print(sqrt_math(val))
    print('Using ** operator:')
    print(sqrt_operator(val))
    print('Using Newton\'s Method:')
    print(sqrt_newtons_method(val))

if __name__ == '__main__':
    main()
