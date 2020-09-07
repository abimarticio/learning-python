from functools import reduce

# compute sum using loop

numbers = list(range(10))
total = 0
for number in numbers:
    total+= number
print(total)

# compute using function
print(sum(numbers))

# add 2 to each value in numbers
for number in numbers:
    print(number + 2)

def add_two(number):
    return number + 2

print()

for number in numbers:
    print(add_two(number))

print()

#using lambda function
# using map,
# 0 + 2
# 1 + 2
# 2 + 2
print(list(map(lambda number: number + 2, numbers)))

people_age = {"Roger": 32, "Hersha": 32, "Jamie": 40}
print(list(map(lambda value: value[1] + 2, people_age.items())))
print([value + 2 for key, value in people_age.items()])