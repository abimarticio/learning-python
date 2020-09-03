# f(input) => output

# f(x, y) = x^2 + 2y
# f(x=10, y=5) = (10)^2 + 2(5) = 110

# def insert_value(list_of_numbers, new_value):
def insert_value(list_of_numbers: list, new_value: int) -> list:
    # pure function
    list_of_numbers.append(new_value)
    return list_of_numbers

numbers = [number for number in range(5)]
print(numbers)
user_input = int(input("Enter new value: "))
new_numbers = insert_value(list_of_numbers = numbers, new_value = user_input)
print(numbers)
print(new_numbers)