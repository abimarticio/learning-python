import math

class TaylorSeries(object):
    def __init__(self, num_terms: int):
        self.num_terms = num_terms

    def compute_series(self, x: float) -> float:
        raise NotImplementedError

    def __call__(self, x: float) -> float:
    # make taylor series callable
        return self.compute_series(x)

class Sine(TaylorSeries):
    def compute_series(self, x: float) -> float:
        x = math.radians(x)
        approximation = 0
        for index in range(self.num_terms):
            coefficient = ((-1) ** index)
            numerator = x ** (2 * index + 1)
            denominator = math.factorial(2 * index + 1)
            approximation += (coefficient * (numerator / denominator))
        return approximation

class Exponential(TaylorSeries):
    def compute_series(self, x: float) -> float:
        approximation = 0
        for index in range(self.num_terms):
            numerator = x ** index
            denominator = math.factorial(index)
            approximation += (numerator / denominator)
        return approximation

class Cosine(TaylorSeries):
    def compute_series(self, x: float) -> float:
        x = math.radians(x)
        approximation = 0
        for index in range(self.num_terms):
            coefficient = ((-1) ** index)
            numerator = x ** (2 * index)
            denominator = math.factorial(2 * index)
            approximation += (coefficient * (numerator / denominator))
        return approximation

def main():
    x = float(input("Enter value of x: "))
    sine = Sine(num_terms=10)
    print(f"sin{x} = {sine(x)}")

    x = float(input("Enter value of x: "))
    cosine = Cosine(num_terms=10)
    print(f"cosin{x} = {cosine(x)}")

    x = float(input("Enter value of x: "))
    exponential = Exponential(num_terms=10)
    Exponential_value = exponential.compute_series(x)
    print(f"exponential{x} = {Exponential_value}")

if __name__ == "__main__":
    main()