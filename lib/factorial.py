# File: lib/factorial.py

def factorial(n):
    product = 1
    while n > 0:
        print("n is: ", n)
        n -= 1
        print("n - 1 is: ", n)
        product *= n
        print("product is: ", product)
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 0
