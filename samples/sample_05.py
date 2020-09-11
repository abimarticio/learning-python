# loops

# for (int index = 0; index < someValue; index++) { statements ;}

# simplicitly, declares index = 0
# index < 10
# step_size = 1; index++ or index +=1
for index in range(10):
    print(index, end = " ")

print()

for index in range (0, 10 ,1):
    print(index, end = " ")

print()

for index in range(0, 10, 2):
    print(index, end = " ")

print()

# (starting_value, ending_value, step_size)
# where starting_value is included,
# ending_value is excluded
for index in range(9, -1, -1):
    print(index, end = " ")

print()

index = 0
while index < 10:
    print(index, end = " ")
    index += 1