def get_sum(numbers: list) -> float:
    total = 0
    for index in range(len(numbers)):
        total += numbers[index]
    return total

def compute_circumference(radius: float) -> float:
    pi = 3.14159265
    diameter = 2 * radius
    circumference = pi * diameter
    return circumference

def main():
    radius = int(input("Give me a radius: "))
    circumference = compute_circumference(radius = radius)
    print(circumference)
    numbers = [1, 3, 5, 7]
    total_numbers = get_sum(numbers=numbers)
    print(total_numbers)

main()