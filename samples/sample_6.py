# lists - data structure similar to array, mutable (values can be changed)
# tuples - data structure similar to array, immutable (values cannot be changed)
# dictionaries - data structure having <key, value> pairs, mutable

# list of strings
names = ["Lara", "Gab", "Keean", "Carlos", "Francis", "Hazel"]
print(names)

print(names[0])
print(names[0:3])
print(names[5])
print(names[-1])
print(names[-2])
print(names[-3])
print(names[len(names) - 1])
print(names[0:6:2])
print(names[::2])

name = "Lara"
# duplicate name times 3
# as list elements
names = [name] * 3
print(names)

# make a five-zero array
zero_array = [0] * 5
print(zero_array)

number = list(range(5))
print(number)

even_numbers = list(range(0, 11, 2))
print(even_numbers)

names = ["Lara", "Gab", "Keean", "Carlos", "Francis", "Hazel"]
names.append("Abi") # insert a new entry to the list, add to end
print(names)
names.append("Gab")
print(names)
names.remove("Gab") # removes first occurence
print(names)
names.pop() # removes last item in the list
print(names) # just to see

print(names[::-1])

# for(int index = 0; index < names.length; index++)
# use loop for iterating through names
for index in range(len(names)):
    print(names[index])

print()

# use loop to reverse sort
# for (int index = <start>; <conditions>; <increment>) { }
# range(start, stop, step)
# for (int index = names.length; index < 0; index--) { }
for index in range(len(names) - 1, -1, -1):
    print(names[index])

print()

names = names[::-1]
print(names)

print()

# naive reverse sort
# using loop
reversed_names = []
for index in range(len(names) - 1, -1, -1):
    reversed_names.append(names[index])
print(reversed_names)

for index in range(len(names)):
    print(names[index])
    if names[index] == "Carlos":
        names[index] = "Carlo"
print(names)

names_and_numbers = ["John Doe", 36, "Minnesota", 2600.00]
print(names_and_numbers)

names = ("Lara", "Gab", "Keean", "Carlos", "Francis", "Hazel", "Abi")
print(names)

for index in range(len(names)):
    print(names[index])

# # try to change tuple value
# for index in range(len(names)):
#     if names[index] == "Carlos":
#         names[index] = "Carlo"
# print(names)

print()

for name in names:
    print(name)

for index, name in enumerate(names):
    print(f"{index} : {name}")

for index, name in enumerate(names):
    if index % 2 == 0:
        print(f"{index} : {name}")
    elif index % 2 != 0:
            print(f"{name}")

print()

employee_1_information = {"first name": "John", "last name": "Doe", "age": 36, 
                            "salary": 2600.00, "employed": True}

print(employee_1_information["first name"])      

for key, value in employee_1_information.items():
    print(f"{key} : {value}")

employee_1_information["salary"] = 2800.00

print()

print(employee_1_information["salary"])
print(employee_1_information)

employee_1_information["address"] = "Minnesota"

print(employee_1_information)

print(employee_1_information.keys())
print(employee_1_information.values())
employee_1_information.popitem()
print(employee_1_information)

employee_2_information = {"first name": "Jane", "last name": "Doe", "age": 36,
                            "salary": 2800, "employed": True}

employee_3_information = {"first name": "Uncle", "last name": "Sam", "age": 50,
                            "salary": 3500, "employed": True}

employees_information = [employee_1_information, employee_2_information, employee_3_information]
print(employees_information)

for employee_number, employee_information in enumerate(employees_information):
    for key, value in employee_information.items():
        print(f"{key}: {value}")