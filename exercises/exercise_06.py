# exercise 6a
# Given a list of names,
# count the occurence of each item
# use the name as the key
# and the number of occurences as the value
names = ["Adam", "Adam", "Eve", "Carl", "Steven", "Steve", "Gavin", "Mark",
        "Samantha", "Hillary", "Josh", "Hillary", "Mary", "Madison", "Stephen"]

name_occurrence = {}
for name in names:
    num_occurrence = names.count(name)
    name_occurrence[name] = num_occurrence

print(name_occurrence)

print()

# exercise 6b
# read the big.txt
# continuation of sample_8
# remove the \n
# Make a list of all the words
# in big.txt

with open("../samples/big.txt", "r") as text_file:
    data = text_file.readlines()

lines = [line.strip("\n") for line in data]
txt = (lines[:100])

list_of_all_words = []
for elements in txt:
    list_of_words = elements.split()
    list_of_all_words += list_of_words

print(list_of_all_words)


# list_of_elements = []
# for elements in txt:
#     list_of_elements.append(elements.split())

# list_of_all_words = []
# for elements in list_of_elements:
#     for index in range(len(elements)):
#         list_of_all_words.append(elements[index])

# print(list_of_all_words)