# taylor series

from math import factorial
from math import pi
from math import radians

def get_sin_x(x, num_terms):
    result = 0
    for n in range(num_terms):
        sin_x = (((-1) ** n) * (x ** (2 * n + 1))) / factorial(2 * n + 1)
        result += sin_x
    return result

def main():
    x = int(input("Value of x: "))
    x = radians(x)
    num_terms = int(input("Number of terms: "))
    sin_x = get_sin_x(x=x, num_terms=num_terms)
    print(sin_x)

main()