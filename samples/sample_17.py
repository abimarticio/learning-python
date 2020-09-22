from sample_16 import Cosine, Exponential, Sine

def main():
    x = float(input("Enter value of x: "))
    cos = Cosine(num_terms=10)
    exp = Exponential(num_terms=10)
    sin = Sine(num_terms=10)
    print(f"cos({x}) = {cos(x)}")
    print(f"exp({x}) = {exp(x)}")
    print(f"sin({x}) = {sin(x)}")

if __name__ == "__main__":
    main()